"""
Exemplo simplificado de Painel de Compra.
Mostra como selecionar planos de assinatura e iniciar checkout.
"""

class PainelCompraDemo:
    def __init__(self, usuario_info=None):
        self.usuario_info = usuario_info or {"id_usuario": 1, "email": "demo@example.com"}
        self.planos = {
            "mensal": {"titulo": "Mensal", "preco": "R$ 9,99/mês"},
            "semestral": {"titulo": "Semestral", "preco": "R$ 54/6 meses"},
            "anual": {"titulo": "Anual", "preco": "R$ 99,90/ano"}
        }
        print("Painel de Compra inicializado.")

    def listar_planos(self):
        """Lista os planos disponíveis"""
        print("Planos disponíveis:")
        for chave, plano in self.planos.items():
            print(f"- {plano['titulo']}: {plano['preco']}")

    def selecionar_plano(self, plano_id: str):
        """Simula seleção de um plano e início do checkout"""
        if plano_id not in self.planos:
            print("Plano inválido.")
            return
        plano = self.planos[plano_id]
        print(f"Plano selecionado: {plano['titulo']} ({plano['preco']})")
        self.iniciar_checkout(plano_id)

    def iniciar_checkout(self, plano_id: str):
        """Simula processo de checkout"""
        print(f"Iniciando checkout para o plano '{plano_id}' do usuário {self.usuario_info['email']}...")
        print("Checkout concluído com sucesso! 🎉")

# Exemplo de uso
if __name__ == "__main__":
    demo = PainelCompraDemo()

    # Listar planos
    demo.listar_planos()

    # Selecionar e comprar plano anual
    demo.selecionar_plano("anual")
