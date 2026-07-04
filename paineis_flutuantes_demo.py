"""
Exemplo simplificado de Painéis Flutuantes.
Mostra como abrir e interagir com painéis de luz, visualização, ambiente, skybox e IA.
"""

class PaineisFlutuantesDemo:
    def __init__(self):
        self.paineis_visiveis = []

    def toggle_painel(self, nome: str, visivel: bool = True):
        """Simula abrir/fechar um painel flutuante"""
        if visivel:
            self.paineis_visiveis.append(nome)
            print(f"Painel '{nome}' aberto.")
        else:
            if nome in self.paineis_visiveis:
                self.paineis_visiveis.remove(nome)
            print(f"Painel '{nome}' fechado.")

    def atualizar_luz(self, h: int, v: int, intensidade: float):
        """Simula atualização da luz"""
        print(f"Luz ajustada: H={h}, V={v}, Intensidade={intensidade:.1f}")

    def alterar_visualizacao(self, modo: str):
        """Simula alteração do modo de visualização"""
        print(f"Modo de visualização alterado para: {modo}")

    def alterar_wireframe(self, modo: str):
        """Simula alteração do modo wireframe"""
        print(f"Wireframe alterado para: {modo}")

    def alterar_cenario(self, nome: str):
        """Simula troca de cenário"""
        print(f"Cenário alterado para: {nome}")

    def alterar_skybox(self, nome: str):
        """Simula troca de skybox"""
        print(f"Skybox alterado para: {nome}")

    def adicionar_log_ai(self, texto: str):
        """Simula adição de log no painel de IA"""
        print(f"[IA LOG] {texto}")

    def atualizar_progresso_ai(self, valor: int):
        """Simula atualização da barra de progresso da IA"""
        print(f"[IA] Progresso: {valor}%")

# Exemplo de uso
if __name__ == "__main__":
    demo = PaineisFlutuantesDemo()

    # Abrir painel de luz e ajustar
    demo.toggle_painel("luz", True)
    demo.atualizar_luz(45, 30, 2.5)

    # Alterar visualização e wireframe
    demo.toggle_painel("visualizacao", True)
    demo.alterar_visualizacao("textura")
    demo.alterar_wireframe("grade")

    # Alterar cenário e skybox
    demo.toggle_painel("ambiente", True)
    demo.alterar_cenario("Praia")
    demo.toggle_painel("skybox", True)
    demo.alterar_skybox("Céu Noturno")

    # Painel de IA
    demo.toggle_painel("ai", True)
    demo.adicionar_log_ai("Iniciando geração de modelo...")
    demo.atualizar_progresso_ai(50)
    demo.toggle_painel("ai", False)
