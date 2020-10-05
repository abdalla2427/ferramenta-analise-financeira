class Projeto:
    def __init__ (self, custo, influencia_por_meta, nome=None):
        self.nome = nome
        self.custo = custo
        self.influencia_por_meta = influencia_por_meta

class Empresa:
    def __init__(self, projetos_disponiveis, metas):
        self.projetos_disponiveis = projetos_disponiveis
        self.metas = metas
        self.portifolio = []


