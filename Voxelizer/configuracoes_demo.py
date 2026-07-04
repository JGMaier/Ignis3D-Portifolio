"""
Exemplo simplificado de Configurações.
Mostra como carregar parâmetros de voxelizer.yml.
"""

from configuracoes import carregar_configuracoes

class ConfiguracoesDemo:
    def __init__(self):
        self.config = {}

    def carregar(self, caminho=None):
        """Carrega configurações do arquivo YAML"""
        self.config = carregar_configuracoes(caminho)
        if self.config:
            print("Configurações carregadas com sucesso!")
        else:
            print("Nenhuma configuração encontrada.")

    def mostrar_parametros(self):
        """Exibe parâmetros principais"""
        if not self.config:
            print("Configurações não carregadas.")
            return
        print("=== Parâmetros do voxelizer.yml ===")
        for chave, valor in self.config.items():
            print(f"{chave}: {valor}")

# Exemplo de uso
if __name__ == "__main__":
    demo = ConfiguracoesDemo()

    # Carregar configurações (simulação)
    demo.carregar("voxelizer.yml")

    # Mostrar parâmetros
    demo.mostrar_parametros()
