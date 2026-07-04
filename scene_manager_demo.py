"""
Exemplo simplificado de Scene Manager.
Mostra como carregar cenários e definir skyboxes.
"""

class SceneManagerDemo:
    def __init__(self):
        self.cenario_atual = None
        self.skybox_atual = "default"

    def carregar_cenario(self, nome: str):
        """Simula carregamento de um cenário"""
        self.cenario_atual = nome
        print(f"Cenário carregado: {nome}")
        print("Transformações aplicadas: escala, rotação e translação.")

    def remover_cenario(self):
        """Simula remoção do cenário atual"""
        if self.cenario_atual:
            print(f"Cenário '{self.cenario_atual}' removido.")
            self.cenario_atual = None
        else:
            print("Nenhum cenário para remover.")

    def definir_skybox(self, nome: str):
        """Simula definição de um skybox"""
        self.skybox_atual = nome
        print(f"Skybox definido: {nome}")

# Exemplo de uso
if __name__ == "__main__":
    demo = SceneManagerDemo()

    # Carregar cenário
    demo.carregar_cenario("CityCenary")

    # Definir skybox
    demo.definir_skybox("Céu Noturno HDR")

    # Remover cenário
    demo.remover_cenario()
