from pulp import *

class Projeto:
    def __init__ (self, custo, influencia_por_meta):
        self.custo = custo
        self.influencia_por_meta = influencia_por_meta

class Empresa:
    def __init__(self, projetos_disponiveis, metas):
        self.projetos_disponiveis = projetos_disponiveis
        self.metas = metas
        self.portifolio = []

class OtimizarPortifolio:
    def __init__(self, empresa):
        self.empresa = empresa
        self.capital_disponivel = 0
        self.beneficio_por_projeto = []
        self.peso_por_meta = [self.empresa.metas[meta] for meta in self.empresa.metas]
        self.calcular_capital_disponivel()
        self.calcular_beneficio_por_projeto()
        empresa.portifolio = self.otimizar_portifolio()

    def calcular_capital_disponivel(self):
        self.capital_disponivel = (sum([projeto.custo for projeto in self.empresa.projetos_disponiveis])) * 0.65

    def calcular_beneficio_por_projeto(self):
        beneficio_por_projeto = []

        for i in range(len(self.empresa.projetos_disponiveis)):
            beneficio_projeto = []
            soma = 0
            for j in range(len(self.peso_por_meta)):
                peso_por_meta = self.peso_por_meta[j]
                peso_do_projeto = self.empresa.projetos_disponiveis[i].influencia_por_meta[j]
                
                soma += (peso_por_meta * peso_do_projeto)
            beneficio_por_projeto.append([soma, self.empresa.projetos_disponiveis[i].custo])

        self.beneficio_por_projeto = beneficio_por_projeto

    def otimizar_portifolio(self):
        prob = LpProblem("Otimizar Beneficio Empresa", LpMaximize)
        n = [i for i in range(len(self.beneficio_por_projeto))]

        variaveis_binarias_projeto = [LpVariable(str(i), 0, 1, LpBinary) for i in n]

        prob += lpSum([variaveis_binarias_projeto[i]*self.beneficio_por_projeto[i][0] for i in n]), "Beneficio"
        prob += lpSum([variaveis_binarias_projeto[i]*self.beneficio_por_projeto[i][1] for i in n]) <= self.capital_disponivel, "Restricao capital"
        prob.solve()
        return prob.variables()



