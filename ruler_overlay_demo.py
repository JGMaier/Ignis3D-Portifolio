"""
Exemplo simplificado de Ruler Overlay.
Mostra como exibir uma régua lateral para medir em centímetros.
"""

class RulerOverlayDemo:
    def __init__(self, side="left"):
        self.side = side
        self.cm_to_pixels = 10
        self.max_cm_display = 50  # reduzido para simplificação

    def desenhar_regua(self, altura_px: int):
        """Simula desenho da régua"""
        print(f"Régua ({self.side}) - Altura: {altura_px}px")
        center_y = altura_px / 2

        for cm in range(-self.max_cm_display, self.max_cm_display + 1, 1):
            y_pos = int(center_y - cm * self.cm_to_pixels)
            if 0 <= y_pos <= altura_px:
                if cm % 10 == 0:
                    print(f"[{self.side}] Marca longa em {y_pos}px -> {cm} cm")
                elif cm % 5 == 0:
                    print(f"[{self.side}] Marca média em {y_pos}px")
                else:
                    print(f"[{self.side}] Marca curta em {y_pos}px")

# Exemplo de uso
if __name__ == "__main__":
    demo_left = RulerOverlayDemo(side="left")
    demo_right = RulerOverlayDemo(side="right")

    # Simula desenho em uma janela de 400px de altura
    demo_left.desenhar_regua(400)
    demo_right.desenhar_regua(400)
