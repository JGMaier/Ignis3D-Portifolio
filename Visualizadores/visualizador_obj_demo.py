"""
Exemplo simplificado de Visualizador OBJ.
Mostra como carregar modelos OBJ, aplicar transformações e controlar a câmera.
"""

class VisualizadorOBJDemo:
    def __init__(self):
        self.modelo_atual = None
        self.camera_posicao = (0, 0, 10)
        self.camera_foco = (0, 0, 0)
        self.textura_aplicada = None

    def carregar_modelo(self, caminho: str):
        """Simula carregamento de um modelo OBJ"""
        if not caminho.endswith(".obj"):
            print("Arquivo inválido. Apenas .obj suportado.")
            return False
        self.modelo_atual = caminho
        print(f"Modelo OBJ carregado: {caminho}")
        return True

    def aplicar_textura(self, caminho_textura: str):
        """Simula aplicação de textura ao modelo"""
        if not self.modelo_atual:
            print("Nenhum modelo carregado.")
            return
        self.textura_aplicada = caminho_textura
        print(f"Textura aplicada ao modelo '{self.modelo_atual}': {caminho_textura}")

    def aplicar_escala(self, fator: float):
        """Simula aplicação de escala global"""
        if not self.modelo_atual:
            print("Nenhum modelo carregado.")
            return
        print(f"Escala aplicada ao modelo '{self.modelo_atual}': {fator}x")

    def resetar_camera(self):
        """Reseta a câmera para posição padrão"""
        self.camera_posicao = (50, 50, 50)
        self.camera_foco = (0, 0, 0)
        print(f"Câmera resetada para posição {self.camera_posicao}, foco {self.camera_foco}")

    def executar_animacao_apresentacao(self):
        """Simula animação de apresentação (fly-in + órbita)"""
        print("Executando animação de apresentação...")
        print("Fly-in concluído. Orbitando em torno do modelo OBJ.")

# Exemplo de uso
if __name__ == "__main__":
    demo = VisualizadorOBJDemo()

    # Carregar modelo
    if demo.carregar_modelo("exemplo_modelo.obj"):
        # Aplicar textura
        demo.aplicar_textura("textura_madeira.png")

        # Aplicar escala
        demo.aplicar_escala(1.5)

        # Resetar câmera
        demo.resetar_camera()

        # Executar animação de apresentação
        demo.executar_animacao_apresentacao()
