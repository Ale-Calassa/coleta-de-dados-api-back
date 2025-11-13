from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class DadosComerciais(Base):
    __tablename__ = "dados_vendas"

    id = Column(Integer, primary_key=True, index=True)
    nome_cliente = Column(String(50), nullable=False)
    produto = Column(String(50), nullable=False)
    categoria = Column(String(50), nullable=False)
    valor_unitario = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_total = Column(Float) # Calculo no app.py
    data_venda = Column(Date, nullable=False)
    canal_venda = Column(String(50), nullable=True)
    observacoes = Column(String(255))