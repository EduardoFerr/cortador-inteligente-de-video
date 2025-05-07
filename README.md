# Cortador Inteligente de Vídeo

## Descrição

Este projeto permite realizar cortes automáticos em vídeos verticais usando IA. Ele aplica transcrição de áudio para dividir o vídeo em trechos e gerar cortes com legendas, zoom e outras manipulações. A solução roda localmente usando MoviePy para processamento de vídeo e Faster Whisper para transcrição.

---

## Funcionalidades

- **Corte automático**: Extração de trechos de vídeos com base na transcrição do áudio.
- **Legendas automáticas**: Geração de legendas em tempo real, utilizando a transcrição do áudio.
- **Zoom dinâmico**: Adição de zoom automático para tornar os cortes mais focados e atraentes.
- **Interface com Streamlit**: Interface gráfica para facilitar o upload de vídeos e o controle dos cortes.

---

## Tecnologias Utilizadas

- **Python 3.10**: Linguagem de programação utilizada.
- **MoviePy 2.1.2**: Biblioteca para manipulação de vídeos.
- **Faster Whisper**: Modelo de transcrição de áudio para texto.
- **Streamlit**: Framework para criação da interface gráfica.
- **Docker**: Para garantir que o ambiente de desenvolvimento e produção sejam consistentes.

---

## Instalação e Execução

### Requisitos

- Docker
- Docker Compose

### Passo a Passo

1. **Clonar o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/cortador-inteligente-de-video.git
    cd cortador-inteligente-de-video
    ```

2. **Construir e rodar os containers:**

    Certifique-se de que o Docker e o Docker Compose estão instalados. Execute o comando abaixo para construir a imagem e iniciar os containers:

    ```bash
    docker-compose up --build
    ```

    Isso irá criar a imagem do Docker e iniciar o servidor Streamlit na porta `8501`.

3. **Acessar a aplicação:**

    Após o Docker Compose ser iniciado, abra o navegador e acesse [http://localhost:8501](http://localhost:8501) para começar a usar a aplicação.

---

## Como Usar

1. **Upload de Vídeo**: Faça o upload de um arquivo `.mp4` através da interface do Streamlit.
2. **Escolher o Número de Cortes**: Selecione quantos cortes o sistema deve gerar a partir do vídeo.
3. **Gerar Cortes**: Clique no botão "Gerar cortes". O sistema irá processar o vídeo e gerar os cortes automaticamente.
4. **Visualizar os Cortes**: Após o processamento, os cortes estarão disponíveis para visualização na interface.

---

## Estrutura de Diretórios

```plaintext
.
├── input_videos/        # Vídeos enviados para processamento
├── output_videos/       # Vídeos gerados com os cortes
├── app.py               # Código principal para a interface Streamlit
├── processador.py       # Funções de processamento de vídeo (corte e transcrição)
├── Dockerfile           # Arquivo para construção da imagem Docker
├── docker-compose.yml   # Arquivo para rodar o Docker com o Compose
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo de documentação
