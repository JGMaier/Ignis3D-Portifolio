"""
Exemplo simplificado de Diálogo de Opções.
Mostra como abrir uma janela de configurações e aplicar alterações.
"""

class DialogoOpcoesDemo:
    def __init__(self):
        # Configurações simuladas
        self.config = {
            "tema": "dark_theme.qss",
            "cor_principal": "#3d98d7",
            "resolucao": "1920x1080",
            "lang": "Português (BR)",
            "autosave": True
        }

    def aplicar_tema(self, tema: str):
        """Simula a troca de tema"""
        self.config["tema"] = tema
        print(f"Tema aplicado: {tema}")

    def alterar_cor_principal(self, cor_hex: str):
        """Simula alteração da cor principal"""
        self.config["cor_principal"] = cor_hex
        print(f"Cor principal alterada para: {cor_hex}")

    def alterar_resolucao(self, resolucao: str):
        """Simula alteração da resolução"""
        self.config["resolucao"] = resolucao
        print(f"Resolução ajustada para: {resolucao}")

    def alterar_idioma(self, idioma: str):
        """Simula alteração do idioma"""
        self.config["lang"] = idioma
        print(f"Idioma alterado para: {idioma}")

    def salvar_configuracoes(self):
        """Simula salvar configurações"""
        print("Configurações salvas:", self.config)

# Exemplo de uso
if __name__ == "__main__":
    demo = DialogoOpcoesDemo()
    demo.aplicar_tema("claro_theme.qss")
    demo.alterar_cor_principal("#FFD700")
    demo.alterar_resolucao("2560x1440")
    demo.alterar_idioma("English")
    demo.salvar_configuracoes()
