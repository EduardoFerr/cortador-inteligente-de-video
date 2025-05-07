
import streamlit as st
from processador import processar_video
import os

st.set_page_config(layout="centered", page_title="Cortes IA")

st.title("\U0001F3AC Cortador Inteligente de Vídeo")
st.write("Gere cortes verticais automáticos com legendas, zoom e IA – tudo localmente.")

video_file = st.file_uploader("\U0001F4E4 Envie um vídeo .mp4", type=["mp4"])
num_cortes = st.slider("\U0001F3AF Número de cortes", 1, 10, 3)

if video_file:
    input_path = os.path.join("input_videos", video_file.name)
    with open(input_path, "wb") as f:
        f.write(video_file.read())
    st.success(f"Vídeo enviado: {video_file.name}")

    if st.button("\U0001F680 Gerar cortes"):
        with st.spinner("Processando cortes..."):
            processar_video(input_path, num_cortes)
        st.success("Cortes prontos!")

        for i in range(num_cortes):
            output_path = f"output_videos/corte_{i}.mp4"
            if os.path.exists(output_path):
                st.video(output_path)