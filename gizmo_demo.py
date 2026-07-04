"""
Exemplo simplificado de Gizmo.
Mostra como ativar e usar um gizmo para mover atores 3D.
"""

class GizmoDemo:
    def __init__(self):
        self.atores = [{"id": 0, "posicao": (0,0,0)}, {"id": 1, "posicao": (5,0,0)}]
        self.gizmo_ativo = False
        self.atores_alvo = []

    def ativar_para_ator(self, indices):
        """Simula ativação do gizmo para atores selecionados"""
        self.atores_alvo = [self.atores[i] for i in indices if i < len(self.atores)]
        if self.atores_alvo:
            self.gizmo_ativo = True
            print(f"Gizmo ativado para {len(self.atores_alvo)} ator(es).")
        else:
            print("Nenhum ator válido selecionado.")

    def mover_atores(self, delta):
        """Simula movimento dos atores via gizmo"""
        if not self.gizmo_ativo:
            print("Gizmo não está ativo.")
            return
        for ator in self.atores_alvo:
            x, y, z = ator["posicao"]
            dx, dy, dz = delta
            ator["posicao"] = (x+dx, y+dy, z+dz)
            print(f"Ator {ator['id']} movido para {ator['posicao']}")

    def desativar(self):
        """Simula desativação do gizmo"""
        self.gizmo_ativo = False
        self.atores_alvo = []
        print("Gizmo desativado.")

# Exemplo de uso
if __name__ == "__main__":
    demo = GizmoDemo()
    demo.ativar_para_ator([0,1])
    demo.mover_atores((2,0,0))
    demo.desativar()
