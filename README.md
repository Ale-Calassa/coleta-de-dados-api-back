# Backend de Registro de Vendas (Didático)
Este projeto é um backend desenvolvido em Python com Flask, responsável por receber e persistir dados enviados por um formulário de vendas criado em React. Os dados são armazenados em um banco de dados MySQL e utilizados para fins didáticos, simulando um cenário real de coleta e análise de informações de consumo.

### ⚠️ Importante: 
Todos os dados registrados são fictícios e utilizados exclusivamente para fins educacionais e de prática de desenvolvimento.

## Funcionalidades
Recebe requisições POST com dados de vendas via JSON

Persiste os dados em um banco de dados relacional MySQL

Retorna mensagens de sucesso ou erro para o frontend

Preparado para deploy em ambientes como Render

## Tecnologias Utilizadas
Python 3.11+

Flask como framework web

Flask-CORS para permitir requisições do frontend

MySQL Connector para integração com o banco de dados

Render como ambiente de hospedagem

## Estrutura dos Dados Recebidos
<br/>
json
{
  "nome_completo": "João da Silva",
  "nome_produto": "Camiseta Polo",
  "categoria": "Vestuário",
  "valor_unitario": 59.90,
  "quantidade": 2,
  "canal_venda": "Online",
  "observacao": "Cliente pediu embalagem para presente"
}

## Como Rodar Localmente
### Clone o repositório:

bash
git clone https://github.com/seu-usuario/seu-backend-repositorio.git
cd seu-backend-repositorio
Crie e ative um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Configure as variáveis de ambiente (ex: conexão com MySQL)

Inicie o servidor Flask:

bash
flask run

## Deploy
O backend está hospedado na plataforma Render, permitindo que o frontend React envie dados diretamente para a API via fetch.

## Objetivo Didático 🎯
### Este backend simula um ambiente real de coleta de dados, permitindo que desenvolvedores pratiquem:

Integração entre frontend e backend

Persistência de dados em banco relacional

Deploy de aplicações web

Boas práticas de estruturação de APIs REST
