"""
Exemplo simplificado de Painel de Exportação NIF.
Mostra como configurar opções e exportar um modelo.
"""

class PainelExportacaoNIFDemo:
    def __init__(self, nome_sugerido="modelo_exportado.nif"):
        self.nome_sugerido = nome_sugerido
        self.caminho_destino = ""
        self.versao = "Skyrim"
        self.preservar_glb = False

    def definir_destino(self, caminho: str):
        """Define o caminho de salvamento"""
        self.caminho_destino = caminho
        print(f"Destino definido: {self.caminho_destino}")

    def escolher_versao(self, versao: str):
        """Escolhe a versão do jogo para exportação"""
        if versao not in ["Skyrim", "Oblivion", "Morrowind"]:
            print("Versão inválida.")
            return
        self.versao = versao
        print(f"Versão selecionada: {self.versao}")

    def ativar_preservacao_glb(self, ativar: bool):
        """Ativa ou desativa preservação de dados GLB"""
        self.preservar_glb = ativar
        estado = "ativada" if ativar else "desativada"
        print(f"Preservação GLB {estado}")

    def exportar(self):
        """Simula exportação para NIF"""
        if not self.caminho_destino:
            print("Erro: Nenhum destino definido.")
            return False
        print(f"Exportando modelo para {self.caminho_destino}...")
        print(f"Configurações: Versão={self.versao}, Preservar GLB={self.preservar_glb}")
        print("Exportação concluída com sucesso! 🎉")
        return True

# Exemplo de uso
if __name__ == "__main__":
    demo = PainelExportacaoNIFDemo()

    # Definir destino
    demo.definir_destino("meu_modelo.nif")

    # Escolher versão
    demo.escolher_versao("Oblivion")

    # Ativar preservação GLB
    demo.ativar_preservacao_glb(True)

    # Exportar
    demo.exportar()
