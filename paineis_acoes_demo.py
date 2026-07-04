"""
Exemplo simplificado de Painéis de Ações.
Mostra como abrir painéis de ações para atores e pastas.
"""

class PaineisAcoesDemo:
    def __init__(self):
        self.ator_selecionado = None
        self.pasta_selecionada = None

    def toggle_painel_ator(self, indice: int, visivel: bool = True):
        """Simula abrir/fechar painel de ações do ator"""
        self.ator_selecionado = indice if visivel else None
        if visivel:
            print(f"Painel de ações aberto para ator {indice}")
        else:
            print("Painel de ações do ator fechado")

    def toggle_painel_pasta(self, nome: str, visivel: bool = True):
        """Simula abrir/fechar painel de ações da pasta"""
        self.pasta_selecionada = nome if visivel else None
        if visivel:
            print(f"Painel de ações aberto para pasta '{nome}'")
        else:
            print("Painel de ações da pasta fechado")

    def executar_acao_ator(self, acao: str):
        """Simula execução de ação sobre ator"""
        if self.ator_selecionado is None:
            print("Nenhum ator selecionado.")
            return
        print(f"Ação '{acao}' executada no ator {self.ator_selecionado}")

    def executar_acao_pasta(self, acao: str):
        """Simula execução de ação sobre pasta"""
        if self.pasta_selecionada is None:
            print("Nenhuma pasta selecionada.")
            return
        print(f"Ação '{acao}' executada na pasta '{self.pasta_selecionada}'")

# Exemplo de uso
if __name__ == "__main__":
    demo = PaineisAcoesDemo()

    # Abrir painel de ator e executar ações
    demo.toggle_painel_ator(1, visivel=True)
    demo.executar_acao_ator("Duplicar")
    demo.executar_acao_ator("Excluir")
    demo.toggle_painel_ator(1, visivel=False)

    # Abrir painel de pasta e executar ações
    demo.toggle_painel_pasta("Grupo_A", visivel=True)
    demo.executar_acao_pasta("Duplicar")
    demo.executar_acao_pasta("Excluir")
    demo.toggle_painel_pasta("Grupo_A", visivel=False)
