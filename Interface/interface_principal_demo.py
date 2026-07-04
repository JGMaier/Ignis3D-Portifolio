"""
Exemplo simplificado da Interface Principal.
Mostra como iniciar a janela principal, criar e abrir projetos.
"""

class JanelaPrincipalDemo:
    def __init__(self):
        self.usuario_logado = None
        self.token_sessao = None
        self.recentes = []

    def criar_novo_projeto(self, nome: str):
        """Simula criação de um novo projeto"""
        print(f"Novo projeto criado: {nome}")
        self.recentes.append(nome)

    def abrir_projeto(self, caminho: str):
        """Simula abertura de um projeto existente"""
        print(f"Projeto aberto: {caminho}")
        self.recentes.append(caminho)

    def abrir_modelo(self, caminho: str):
        """Simula abertura de um modelo 3D"""
        print(f"Modelo 3D aberto: {caminho}")
        self.recentes.append(caminho)

    def listar_recentes(self):
        """Lista os arquivos recentes"""
        print("Arquivos recentes:")
        for item in self.recentes:
            print("-", item)

# Exemplo de uso
if __name__ == "__main__":
    demo = JanelaPrincipalDemo()

    # Criar novo projeto
    demo.criar_novo_projeto("Projeto Ignis3D")

    # Abrir projeto existente
    demo.abrir_projeto("meu_projeto.i3d")

    # Abrir modelo 3D
    demo.abrir_modelo("modelo_exemplo.glb")

    # Listar recentes
    demo.listar_recentes()
