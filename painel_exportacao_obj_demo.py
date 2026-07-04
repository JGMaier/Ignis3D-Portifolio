"""
Exemplo simplificado de Painel de Exportação OBJ.
Mostra como configurar opções e exportar um modelo.
"""

class PainelExportacaoOBJDemo:
    def __init__(self, nome_sugerido="modelo_exportado.obj"):
        self.nome_sugerido = nome_sugerido
        self.caminho_destino = ""
        self.agrupar_texturas = True

    def definir_destino(self, caminho: str):
        """Define o caminho de salvamento"""
        self.caminho_destino = caminho
        print(f"Destino definido: {self.caminho_destino}")

    def configurar_agrupar_texturas(self, agrupar: bool):
        """Ativa ou desativa agrupamento de texturas"""
        self.agrupar_texturas = agrupar
        estado = "ativado" if agrupar else "desativado"
        print(f"Agrupamento de texturas {estado}")

    def exportar(self):
        """Simula exportação para OBJ"""
        if not self.caminho_destino:
            print("Erro: Nenhum destino definido.")
            return False
        print(f"Exportando modelo para {self.caminho_destino}...")
        print(f"Configurações: Agrupar Texturas={self.agrupar_texturas}")
        print("Exportação concluída com sucesso! 🎉")
        return True

# Exemplo de uso
if __name__ == "__main__":
    demo = PainelExportacaoOBJDemo()

    # Definir destino
    demo.definir_destino("meu_modelo.obj")

    # Configurar agrupamento de texturas
    demo.configurar_agrupar_texturas(False)

    # Exportar
    demo.exportar()
