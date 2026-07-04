"""
Exemplo simplificado de Marketplace.
Mostra como buscar modelos e instalar extensões.
"""

class MarketplaceDemo:
    def __init__(self):
        self.modelos = []
        self.extensoes = []
        self.instaladas = []

    def pesquisar_modelos(self, termo: str):
        """Simula busca de modelos no Sketchfab"""
        self.modelos = [f"Modelo_{i}_{termo}" for i in range(1, 4)]
        print(f"Modelos encontrados para '{termo}':", self.modelos)
        return self.modelos

    def listar_extensoes(self):
        """Simula listagem de extensões disponíveis"""
        self.extensoes = ["Extensão_Voxelizer", "Extensão_Render", "Extensão_AI"]
        print("Extensões disponíveis:", self.extensoes)
        return self.extensoes

    def instalar_extensao(self, nome: str):
        """Simula instalação de uma extensão"""
        if nome in self.extensoes:
            self.instaladas.append(nome)
            print(f"Extensão instalada: {nome}")
            return True
        print(f"Extensão não encontrada: {nome}")
        return False

    def desinstalar_extensao(self, nome: str):
        """Simula desinstalação de uma extensão"""
        if nome in self.instaladas:
            self.instaladas.remove(nome)
            print(f"Extensão desinstalada: {nome}")
            return True
        print(f"Extensão não instalada: {nome}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    demo = MarketplaceDemo()

    # Buscar modelos
    demo.pesquisar_modelos("carro")

    # Listar extensões
    demo.listar_extensoes()

    # Instalar extensão
    demo.instalar_extensao("Extensão_AI")

    # Desinstalar extensão
    demo.desinstalar_extensao("Extensão_AI")
