from flask import Flask, request, send_file
from flaskwebgui import FlaskUI 
from model import *

app = Flask(__name__)

ui = FlaskUI(app)

@app.route("/")
def index():
  return send_file("index.html")

ui.run()

projetos_disponiveis = [Projeto(100, [10, 20, 30, 40]),
        Projeto(200, [20, 20, 40, 10]),
        Projeto(100, [30, 20, 30, 20]),
        Projeto(200, [20, 10, 0, 70])]

metas = {
    "Meta1": 20,
    "Meta2": 40,
    "Meta3": 30,
    "Meta4": 10
    }

empresa = Empresa(projetos_disponiveis, metas)

OtimizarPortifolio(empresa)
empresa.portifolio