"""
Exemplo simplificado de Visualizador JSON.
Mostra como carregar modelos Minecraft (Java/Bedrock) e controlar a cena.
"""

class VisualizadorJSONDemo:
    def __init__(self):
        self.modelo_atual = None
        self.formato = None
        self.camera_posicao = (0, 0, 10)
        self.camera_foco = (0, 0, 0)

    def carregar_modelo(self, caminho: str):
        """Simula carregamento de um modelo JSON"""
        if caminho.endswith(".json"):
            # Detecta formato fictício
            if "bedrock" in caminho.lower():
                self.formato = "Bedrock"
            else:
                self.formato = "Java"
            self.modelo_atual = caminho
            print(f"Modelo JSON carregado: {caminho} (Formato: {self.formato})")
        else:
            print("Arquivo inválido. Apenas .json suportado.")

    def aplicar_escala(self, fator: float):
        """Simula aplicação de escala global"""
        if not self.modelo_atual:
            print("Nenhum modelo carregado.")
            return
        print(f"Escala aplicada ao modelo '{self.modelo_atual}': {fator}x")

    def resetar_camera(self):
        """Reseta a câmera para posição padrão"""
        self.camera_posicao = (30, 30, 30)
        self.camera_foco = (0, 0, 0)
        print(f"Câmera resetada para posição {self.camera_posicao}, foco {self.camera_foco}")

    def executar_animacao_apresentacao(self):
        """Simula animação de apresentação (fly-in + órbita)"""
        print("Executando animação de apresentação...")
        print("Fly-in concluído. Orbitando em torno do modelo.")

# Exemplo de uso
if __name__ == "__main__":
    demo = VisualizadorJSONDemo()

    # Carregar modelo Java
    demo.carregar_modelo("exemplo_modelo_java.json")

    # Aplicar escala
    demo.aplicar_escala(1.2)

    # Resetar câmera
    demo.resetar_camera()

    # Executar animação de apresentação
    demo.executar_animacao_apresentacao()

    # Carregar modelo Bedrock
    demo.carregar_modelo("exemplo_modelo_bedrock.json")
