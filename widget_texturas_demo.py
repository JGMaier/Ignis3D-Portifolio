"""
Exemplo simplificado de Widget de Texturas.
Mostra como gerenciar texturas com miniaturas.
"""

class WidgetTexturasDemo:
    def __init__(self):
        self.texturas = {}
        self.selecionada = None

    def carregar_texturas(self, lista_texturas):
        """Carrega lista de texturas"""
        for caminho, tid in lista_texturas:
            self.texturas[tid] = caminho
        print("Texturas carregadas:")
        for tid, caminho in self.texturas.items():
            print(f"- {tid}: {caminho}")

    def selecionar_textura(self, tid):
        """Seleciona uma textura"""
        if tid in self.texturas:
            self.selecionada = tid
            print(f"Textura selecionada: {tid} ({self.texturas[tid]})")
        else:
            print("Textura não encontrada.")

    def remover_textura(self, tid):
        """Remove uma textura"""
        if tid in self.texturas:
            print(f"Textura removida: {tid} ({self.texturas[tid]})")
            del self.texturas[tid]
            if self.selecionada == tid:
                self.selecionada = None
        else:
            print("Textura não encontrada.")

    def destacar_textura(self, tid):
        """Destaca uma textura (simulação de borda amarela)"""
        if tid in self.texturas:
            print(f"Textura destacada: {tid} ({self.texturas[tid]})")

# Exemplo de uso
if __name__ == "__main__":
    demo = WidgetTexturasDemo()

    # Carregar texturas
    demo.carregar_texturas([
        ("madeira.png", "tex1"),
        ("metal.png", "tex2"),
        ("vidro.png", "tex3")
    ])

    # Selecionar textura
    demo.selecionar_textura("tex2")

    # Destacar textura
    demo.destacar_textura("tex3")

    # Remover textura
    demo.remover_textura("tex1")
