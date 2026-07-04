"""
Exemplo simplificado de Visualizador GLB.
Mostra como carregar modelos, aplicar transformações e controlar a câmera.
"""

class VisualizadorGLBDemo:
    def __init__(self):
        self.modelo_atual = None
        self.camera_posicao = (0, 0, 10)
        self.camera_foco = (0, 0, 0)

    def carregar_modelo(self, caminho: str):
        """Simula carregamento de um modelo GLB"""
        self.modelo_atual = caminho
        print(f"Modelo GLB carregado: {caminho}")

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
        print("Fly-in concluído. Orbitando em torno do modelo.")

# Exemplo de uso
if __name__ == "__main__":
    demo = VisualizadorGLBDemo()

    # Carregar modelo
    demo.carregar_modelo("exemplo_modelo.glb")

    # Aplicar escala
    demo.aplicar_escala(1.5)

    # Resetar câmera
    demo.resetar_camera()

    # Executar animação de apresentação
    demo.executar_animacao_apresentacao()
