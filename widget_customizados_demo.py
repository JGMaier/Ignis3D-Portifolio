"""
Exemplo simplificado de Widgets Customizados.
Mostra como usar um QSlider com detecção de duplo clique.
"""

class ClickableSliderDemo:
    def __init__(self):
        self.valor = 50

    def mover_slider(self, novo_valor):
        """Simula movimentação do slider"""
        self.valor = novo_valor
        print(f"Slider movido para: {self.valor}")

    def duplo_clique(self):
        """Simula ação ao dar duplo clique no handle"""
        self.valor = 0
        print("Duplo clique detectado! Slider resetado para 0.")

# Exemplo de uso
if __name__ == "__main__":
    demo = ClickableSliderDemo()

    # Mover slider
    demo.mover_slider(75)

    # Duplo clique no handle
    demo.duplo_clique()
