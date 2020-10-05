from pandas import *
from model import *

def ler_metas_empresa_csv(nome_arquivo):
    metas_df = pandas.read_csv(nome_arquivo, delimiter=";", encoding='latin-1')
    metas = {}

    for i_meta in metas_df.itertuples():
        metas.update({i_meta[1] : int(i_meta[2])})
    return metas

def ler_projetos_csv(nome_arquivo):
    projetos_disponiveis_df = pandas.read_csv(nome_arquivo, delimiter=";", encoding='latin-1')
    projetos_disponiveis = []

    for projeto in projetos_disponiveis_df.itertuples():
        projetos_disponiveis.append(Projeto(float(projeto[-1].replace(".","").replace(",",".")), [int(p) for p in projeto[1:-2]], projeto[-2]))   

    return projetos_disponiveis
