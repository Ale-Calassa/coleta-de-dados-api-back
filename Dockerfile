# Usa uma imagem oficial do Python 3.11
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do seu projeto para dentro do container
COPY . .

# Instala as dependências do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8080 (que o Railway usa)
EXPOSE 8080

# Comando para iniciar o Flask com Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]