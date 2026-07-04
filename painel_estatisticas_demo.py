"""
Exemplo simplificado de Painel de Estatísticas.
Mostra como exibir mensagens e progresso de carregamento.
"""

class PainelCarregamentoDemo:
    def __init__(self):
        self.mensagem = "Carregando..."
        self.progresso = 0

    def set_mensagem(self, texto: str):
        """Simula atualização da mensagem de status"""
        self.mensagem = texto
        print(f"[Painel] Mensagem: {self.mensagem}")

    def set_progresso(self, valor: int):
        """Simula atualização da barra de progresso"""
        self.progresso = valor
        print(f"[Painel] Progresso: {self.progresso}%")

    def mostrar(self):
        """Simula exibição do painel"""
        print(f"[Painel] {self.mensagem} ({self.progresso}%)")

# Exemplo de uso
if __name__ == "__main__":
    demo = PainelCarregamentoDemo()

    # Mostrar painel inicial
    demo.mostrar()

    # Atualizar mensagem e progresso
    demo.set_mensagem("Carregando modelo 3D...")
    demo.set_progresso(25)
    demo.set_progresso(50)
    demo.set_progresso(75)
    demo.set_progresso(100)

    # Finalizar
    demo.set_mensagem("Carregamento concluído!")
    demo.mostrar()
