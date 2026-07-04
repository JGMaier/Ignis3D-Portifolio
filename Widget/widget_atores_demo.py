"""
Exemplo simplificado de Widget de Atores.
Mostra como gerenciar lista de atores e grupos.
"""

class WidgetAtoresDemo:
    def __init__(self):
        self.grupos = {}
        self.selecao_atual = []

    def adicionar_modelo(self, nome_modelo, lista_atores):
        """Adiciona um modelo com seus atores"""
        self.grupos[nome_modelo] = lista_atores
        print(f"Modelo '{nome_modelo}' adicionado com atores: {lista_atores}")

    def selecionar_ator(self, indice):
        """Seleciona um ator pelo índice"""
        self.selecao_atual = [indice]
        print(f"Atores selecionados: {self.selecao_atual}")

    def selecionar_atores(self, indices):
        """Seleciona múltiplos atores"""
        self.selecao_atual = indices
        print(f"Atores selecionados: {self.selecao_atual}")

    def mover_ator(self, indice, origem, destino):
        """Simula mover ator entre grupos"""
        if origem in self.grupos and destino in self.grupos:
            atores_origem = self.grupos[origem]
            if indice < len(atores_origem):
                ator = atores_origem.pop(indice)
                self.grupos[destino].append(ator)
                print(f"Ator '{ator}' movido de '{origem}' para '{destino}'")

    def renomear_pasta(self, nome_antigo, nome_novo):
        """Renomeia um grupo/pasta"""
        if nome_antigo in self.grupos:
            self.grupos[nome_novo] = self.grupos.pop(nome_antigo)
            print(f"Pasta renomeada: {nome_antigo} -> {nome_novo}")

# Exemplo de uso
if __name__ == "__main__":
    demo = WidgetAtoresDemo()

    # Adicionar modelo com atores
    demo.adicionar_modelo("Carro", ["Roda", "Porta", "Motor"])

    # Selecionar ator
    demo.selecionar_ator(1)

    # Selecionar múltiplos atores
    demo.selecionar_atores([0, 2])

    # Adicionar outro grupo
    demo.adicionar_modelo("Casa", ["Parede", "Telhado"])

    # Mover ator entre grupos
    demo.mover_ator(0, "Carro", "Casa")

    # Renomear pasta
    demo.renomear_pasta("Casa", "Residência")
