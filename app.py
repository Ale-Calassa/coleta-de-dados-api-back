from flask import Flask, request, jsonify
from flask_cors import CORS
from database import SessionLocal, engine, Base
from models import DadosComerciais
from datetime import datetime
import os

app = Flask(__name__)
CORS(app, origins=["https://ale-calassa.github.io"] )

Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    return jsonify({"mensagem": "API Coleta de Dados está rodando com sucesso!"})

@app.route('/dados', methods=['POST'])
def receber_dados():
    data = request.get_json()
    valor_total = int(data["quantidade"]) * float(data["valor_unitario"])
    session = SessionLocal()

    novo_registo = DadosComerciais(
        nome_cliente = data["nome_cliente"],
        produto = data["produto"],
        categoria = data["categoria"],
        valor_unitario = float(data["valor_unitario"]),
        quantidade = int(data["quantidade"]),
        valor_total = valor_total,
        data_venda = datetime.strptime(data["data_venda"], "%Y-%m-%d").date(),
        canal_venda = data.get("canal_venda"),
        observacoes = data.get("observacoes")
    )

    session.add(novo_registo)
    session.commit()
    session.close()

    return jsonify({"mensagem": "Dados salvos com sucesso!!!"}), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
