"""
Exemplo simplificado de Sistema de Comandos.
Mostra como executar, desfazer e refazer ações de edição.
"""

class ComandoBase:
    """Classe base para comandos com suporte a undo/redo."""
    def execute(self):
        raise NotImplementedError
    def undo(self):
        raise NotImplementedError

class ComandoTransformacao(ComandoBase):
    def __init__(self, ator, posicao_anterior, posicao_nova):
        self.ator = ator
        self.posicao_anterior = posicao_anterior
        self.posicao_nova = posicao_nova

    def execute(self):
        self.ator["posicao"] = self.posicao_nova
        print(f"Transformação aplicada: {self.posicao_nova}")

    def undo(self):
        self.ator["posicao"] = self.posicao_anterior
        print(f"Transformação desfeita: {self.posicao_anterior}")

class ComandoVisibilidade(ComandoBase):
    def __init__(self, ator, estado_anterior, estado_novo):
        self.ator = ator
        self.estado_anterior = estado_anterior
        self.estado_novo = estado_novo

    def execute(self):
        self.ator["visivel"] = self.estado_novo
        print(f"Visibilidade alterada para: {self.estado_novo}")

    def undo(self):
        self.ator["visivel"] = self.estado_anterior
        print(f"Visibilidade restaurada para: {self.estado_anterior}")

class HistoricoEdicao:
    """Gerencia histórico de comandos com suporte a undo/redo."""
    def __init__(self):
        self.pilha_undo = []
        self.pilha_redo = []

    def executar(self, comando: ComandoBase):
        comando.execute()
        self.pilha_undo.append(comando)
        self.pilha_redo.clear()

    def desfazer(self):
        if not self.pilha_undo:
            print("Nada para desfazer.")
            return
        comando = self.pilha_undo.pop()
        comando.undo()
        self.pilha_redo.append(comando)

    def refazer(self):
        if not self.pilha_redo:
            print("Nada para refazer.")
            return
        comando = self.pilha_redo.pop()
        comando.execute()
        self.pilha_undo.append(comando)

# Exemplo de uso
if __name__ == "__main__":
    ator = {"nome": "Peça 1", "posicao": (0,0,0), "visivel": True}
    historico = HistoricoEdicao()

    # Executar transformação
    cmd1 = ComandoTransformacao(ator, ator["posicao"], (10,5,0))
    historico.executar(cmd1)

    # Alterar visibilidade
    cmd2 = ComandoVisibilidade(ator, ator["visivel"], False)
    historico.executar(cmd2)

    # Desfazer última ação
    historico.desfazer()

    # Refazer última ação
    historico.refazer()
