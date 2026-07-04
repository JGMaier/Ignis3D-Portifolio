"""
Exemplo simplificado de Google Listener.
Mostra como processar dados de login recebidos de serviços externos.
"""

class GoogleListenerDemo:
    def __init__(self):
        self.usuario_logado = None

    def validar_token(self, token: str) -> bool:
        """Simula validação de token"""
        return token == "TOKEN_VALIDO"

    def processar_login_google(self, dados: dict):
        """Simula processamento de login do Google"""
        if not self.validar_token(dados.get("token", "")):
            print("[Google Login] Token inválido.")
            return {"status": "error", "message": "Token inválido"}

        self.usuario_logado = {
            "id_usuario": dados.get("id_usuario"),
            "nickname": dados.get("nickname"),
            "email": dados.get("email"),
            "tipo_conta": dados.get("tipo_conta"),
            "token": dados.get("token")
        }
        print("[Google Login] Usuário autenticado com sucesso:", self.usuario_logado)
        return {"status": "success", "message": "Login concluído"}

    def processar_login_facebook(self, dados: dict):
        """Simula processamento de login do Facebook"""
        self.usuario_logado = {
            "id_usuario": dados.get("id_usuario"),
            "nickname": dados.get("nickname"),
            "email": dados.get("email"),
            "tipo_conta": dados.get("tipo_conta"),
            "token": dados.get("token")
        }
        print("[Facebook Login] Usuário autenticado com sucesso:", self.usuario_logado)
        return {"status": "success", "message": "Login concluído"}

# Exemplo de uso
if __name__ == "__main__":
    demo = GoogleListenerDemo()

    # Simulação de login Google
    dados_google = {
        "id_usuario": "123",
        "nickname": "João",
        "email": "joao@example.com",
        "tipo_conta": "normal",
        "token": "TOKEN_VALIDO"
    }
    print(demo.processar_login_google(dados_google))

    # Simulação de login Facebook
    dados_fb = {
        "id_usuario": "456",
        "nickname": "Maria",
        "email": "maria@example.com",
        "tipo_conta": "demo",
        "token": "TOKEN_FB"
    }
    print(demo.processar_login_facebook(dados_fb))
