"""
Exemplo simplificado de Autenticação.
Mostra como validar login, gerar token e cadastrar usuários.
"""

class AutenticacaoDemo:
    def __init__(self):
        self.usuarios = {}
        self.tokens = {}

    def validar_login(self, email: str, senha: str) -> dict | None:
        """Simula validação de login"""
        if email in self.usuarios and self.usuarios[email]["senha"] == senha:
            return {"email": email, "nickname": self.usuarios[email]["nickname"]}
        return None

    def gerar_token(self, id_usuario: str) -> str:
        """Simula geração de token"""
        token = f"TOKEN-{id_usuario}"
        self.tokens[id_usuario] = token
        return token

    def cadastrar_usuario(self, email: str, senha: str, nickname: str) -> dict:
        """Simula cadastro de usuário"""
        if email in self.usuarios:
            raise Exception("Usuário já cadastrado.")
        self.usuarios[email] = {"senha": senha, "nickname": nickname}
        return {"message": "Usuário cadastrado com sucesso.", "email": email}

# Exemplo de uso
if __name__ == "__main__":
    auth = AutenticacaoDemo()

    # Cadastro
    print(auth.cadastrar_usuario("joao@example.com", "1234", "João"))

    # Login
    login = auth.validar_login("joao@example.com", "1234")
    print("Login:", login)

    # Token
    token = auth.gerar_token("joao@example.com")
    print("Token gerado:", token)
