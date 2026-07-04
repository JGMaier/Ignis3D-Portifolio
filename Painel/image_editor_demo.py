"""
Exemplo simplificado de Editor de Imagens.
Mostra como selecionar cores, configurar pincel e adicionar texto.
"""

class ImageEditorDemo:
    def __init__(self):
        self.cor_atual = (255, 255, 255, 255)  # Branco opaco
        self.pincel = {"tamanho": 50, "dureza": 80, "tipo": "Pincel", "estilo": "Redondo"}
        self.textos = []

    def set_cor_rgb(self, r: int, g: int, b: int):
        """Simula seleção de cor RGB"""
        self.cor_atual = (r, g, b, self.cor_atual[3])
        print(f"Cor selecionada: RGB({r}, {g}, {b})")

    def set_cor_alpha(self, alpha: int):
        """Simula ajuste de transparência"""
        self.cor_atual = (self.cor_atual[0], self.cor_atual[1], self.cor_atual[2], alpha)
        print(f"Transparência ajustada: {alpha}/255")

    def configurar_pincel(self, tamanho: int = None, dureza: int = None, tipo: str = None, estilo: str = None):
        """Simula configuração do pincel"""
        if tamanho: self.pincel["tamanho"] = tamanho
        if dureza: self.pincel["dureza"] = dureza
        if tipo: self.pincel["tipo"] = tipo
        if estilo: self.pincel["estilo"] = estilo
        print("Configuração do pincel:", self.pincel)

    def adicionar_texto(self, posicao: tuple, conteudo: str, fonte: str = "Arial", cor: tuple = (0,0,0)):
        """Simula adição de texto na imagem"""
        texto = {"posicao": posicao, "conteudo": conteudo, "fonte": fonte, "cor": cor}
        self.textos.append(texto)
        print(f"Texto adicionado: '{conteudo}' em {posicao} com fonte {fonte} e cor {cor}")

# Exemplo de uso
if __name__ == "__main__":
    demo = ImageEditorDemo()

    # Seleção de cor
    demo.set_cor_rgb(255, 0, 0)  # Vermelho
    demo.set_cor_alpha(128)      # Semi-transparente

    # Configuração de pincel
    demo.configurar_pincel(tamanho=30, dureza=60, tipo="Caneta", estilo="Quadrado")

    # Adição de texto
    demo.adicionar_texto((100, 200), "Ignis3D Demo", fonte="Arial", cor=(0,0,255))
