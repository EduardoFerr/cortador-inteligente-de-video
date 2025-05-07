FROM python:3.10-slim

# Instala dependências do sistema e fontes
RUN apt-get update && apt-get install -y \
    ffmpeg \
    imagemagick \
    libsm6 \
    libxext6 \
    git \
    fonts-dejavu-core \
    fonts-dejavu-extra \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . /app

# Criar diretórios e permissões
RUN mkdir -p /app/input_videos /app/output_videos /app/tmp && \
    chmod -R 777 /app/input_videos /app/output_videos /app/tmp

# Rodar como root para evitar problemas de permissão
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]