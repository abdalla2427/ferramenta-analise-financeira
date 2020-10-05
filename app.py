from model import *
from leitura import *
from otimizar import *
from pandas import *


if __name__ == '__main__':
    empresa = Empresa(ler_projetos_csv("entradas/GUT-projetos-1.csv"), ler_metas_empresa_csv("entradas/GUT-metas-1.csv"))
    otimizacao = OtimizarPortifolio(empresa)
    print(empresa.portifolio)