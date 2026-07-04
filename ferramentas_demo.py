"""
Exemplo simplificado de Ferramentas.
Mostra como aplicar transformações básicas em modelos 3D.
"""

class FerramentasDemo:
    def __init__(self):
        self.modelo = {"escala": 1.0, "rotacao": (0,0,0), "posicao": (0,0,0)}

    def aplicar_escala(self, fator: float):
        """Simula alteração de escala"""
        self.modelo["escala"] = fator
        print(f"Escala aplicada: {fator:.2f}")

    def aplicar_rotacao(self, eixo: str, angulo: int):
        """Simula rotação em um eixo"""
        self.modelo["rotacao"] = (eixo, angulo)
        print(f"Rotação aplicada: {angulo}° no eixo {eixo.upper()}")

    def aplicar_espelhamento(self, eixo: str):
        """Simula espelhamento"""
        print(f"Espelhamento aplicado no eixo {eixo.upper()}")

    def centralizar(self, eixo: str = "xyz"):
        """Simula centralização"""
        self.modelo["posicao"] = (0,0,0)
        print(f"Modelo centralizado no eixo {eixo.upper()}")

# Exemplo de uso
if __name__ == "__main__":
    demo = FerramentasDemo()
    demo.aplicar_escala(1.5)
    demo.aplicar_rotacao("x", 90)
    demo.aplicar_espelhamento("y")
    demo.centralizar()
