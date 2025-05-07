import os
os.environ["TMPDIR"] = "/app"

from faster_whisper import WhisperModel
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

model = WhisperModel("base", compute_type="int8")

def transcrever(video_path):
    try:
        segments, _ = model.transcribe(video_path)
        trechos = []
        for segment in segments:
            start, end, texto = segment.start, segment.end, segment.text.strip()
            if 30 <= end - start <= 60:
                trechos.append((start, end, texto))
        return trechos
    except Exception as e:
        print(f"Erro ao transcrever vídeo: {e}")
        return []

def cortar_video(video_path, start, end, texto, index):
    try:
        output_dir = "/app/output_videos"
        os.makedirs(output_dir, exist_ok=True)

        clip = (
            VideoFileClip(video_path)
            .subclipped(start, end)
            .resized(height=1920)
        )

        w, h = clip.size
        zoom = clip.cropped(
            x_center=w / 2, y_center=h / 2,
            width=min(w, 720), height=min(h, 1280)
        )

        legenda = (
            TextClip(
                font="DejaVuSans.ttf",  # Fonte compatível com Debian
                text=texto,
                font_size=60,
                color='white',
                bg_color='black',
                method='caption',
                size=(720, None)
            )
            .with_duration(zoom.duration)
            .with_position(("center", "bottom"))
        )

        final = CompositeVideoClip([zoom, legenda])
        output_path = os.path.join(output_dir, f"corte_{index}.mp4")
        final.write_videofile(output_path, fps=30, codec="libx264")
    except Exception as e:
        print(f"Erro ao cortar o vídeo: {e}")

def processar_video(path, num_cortes=5):
    os.makedirs("output_videos", exist_ok=True)
    trechos = transcrever(path)
    for i, (start, end, texto) in enumerate(trechos[:num_cortes]):
        cortar_video(path, start, end, texto, i)
