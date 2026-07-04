"""
Exemplo simplificado de Malha Utils.
Mostra como carregar um arquivo de modelo 3D em uma cena trimesh.
"""

class MalhaUtilsDemo:
    def __init__(self):
        self.scene = None

    def carregar_malha_voxel(self, caminho_arquivo):
        """Simula carregamento de um modelo 3D"""
        print(f"🔄 Carregando arquivo de modelo: {caminho_arquivo}")
        # Simulação de carregamento
        self.scene = {"arquivo": caminho_arquivo, "geometrias": 3, "texturas": True}
        return self.scene

    def mostrar_info(self):
        """Exibe informações da cena carregada"""
        if not self.scene:
            print("Nenhuma cena carregada.")
            return
        print("=== Informações da Cena ===")
        print(f"Arquivo: {self.scene['arquivo']}")
        print(f"Geometrias: {self.scene['geometrias']}")
        print(f"Texturas carregadas: {self.scene['texturas']}")

# Exemplo de uso
if __name__ == "__main__":
    demo = MalhaUtilsDemo()

    # Carregar modelo
    demo.carregar_malha_voxel("exemplo_modelo.glb")

    # Mostrar informações
    demo.mostrar_info()
