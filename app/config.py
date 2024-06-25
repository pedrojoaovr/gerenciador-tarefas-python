import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///task.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.urandom(24)  # Gera uma chave secreta aleatória
