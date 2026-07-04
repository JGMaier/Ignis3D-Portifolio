"""
Exemplo simplificado de Painel de Login.
Mostra como simular login, cadastro e troca de idioma/tema.
"""

class PainelLoginDemo:
    def __init__(self):
        self.usuario_logado = None
        self.idioma = "Português (BR)"
        self.tema = "Dark"

    def fazer_login(self, email, senha):
        """Simula login"""
        if email == "joao@ignis3d.com" and senha == "12345678":
            self.usuario_logado = {"nickname": "João", "email": email, "tipo_conta": "Premium"}
            print(f"Login realizado com sucesso! Bem-vindo, {self.usuario_logado['nickname']}.")
        else:
            print("Credenciais inválidas.")

    def cadastrar(self, nick, email, senha, repetir):
        """Simula cadastro"""
        if senha != repetir:
            print("Erro: As senhas não coincidem.")
            return
        if len(senha) < 8:
            print("Erro: A senha deve ter pelo menos 8 caracteres.")
            return
        print(f"Usuário '{nick}' cadastrado com sucesso! Um código de ativação foi enviado para {email}.")

    def finalizar_cadastro(self, token):
        """Simula finalização de cadastro"""
        if token == "ABC123":
            print("Cadastro concluído com sucesso! Você já pode fazer login.")
        else:
            print("Token inválido ou expirado.")

    def mudar_tema(self, tema):
        """Simula troca de tema"""
        self.tema = tema
        print(f"Tema alterado para: {tema}")

    def mudar_idioma(self, idioma):
        """Simula troca de idioma"""
        self.idioma = idioma
        print(f"Idioma alterado para: {idioma}")

# Exemplo de uso
if __name__ == "__main__":
    demo = PainelLoginDemo()

    # Simular login
    demo.fazer_login("joao@ignis3d.com", "12345678")

    # Simular cadastro
    demo.cadastrar("João", "novo@ignis3d.com", "SenhaForte1!", "SenhaForte1!")

    # Finalizar cadastro
    demo.finalizar_cadastro("ABC123")

    # Trocar tema
    demo.mudar_tema("Claro")

    # Trocar idioma
    demo.mudar_idioma("English")
