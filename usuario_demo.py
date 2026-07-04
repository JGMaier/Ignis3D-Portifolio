"""
Exemplo simplificado de Painel de Usuário.
Mostra como exibir informações de perfil, licença e configurações.
"""

class UsuarioDemo:
    def __init__(self, usuario_info=None):
        self.usuario_info = usuario_info or {
            "nickname": "Convidado",
            "email": "demo@ignis3d.com",
            "tipo_conta": "Demo"
        }

    def mostrar_perfil(self):
        """Exibe informações do perfil"""
        print("=== Perfil do Usuário ===")
        print(f"Nickname: {self.usuario_info.get('nickname')}")
        print(f"Email: {self.usuario_info.get('email')}")
        print(f"Tipo de Conta: {self.usuario_info.get('tipo_conta')}")

    def mostrar_licenca(self):
        """Exibe informações da licença"""
        print("=== Licença ===")
        print("Informações sobre a licença do usuário virão aqui.")

    def mostrar_configuracoes(self):
        """Exibe configurações do usuário"""
        print("=== Configurações ===")
        print("Configurações específicas do usuário virão aqui.")

# Exemplo de uso
if __name__ == "__main__":
    demo = UsuarioDemo({
        "nickname": "João",
        "email": "joao@ignis3d.com",
        "tipo_conta": "Premium"
    })

    demo.mostrar_perfil()
    demo.mostrar_licenca()
    demo.mostrar_configuracoes()
