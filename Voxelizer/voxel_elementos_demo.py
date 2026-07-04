"""
Exemplo simplificado de Voxel Elementos.
Mostra como gerar elementos voxel e aplicar otimização.
"""

from voxel_elementos import gerar_elementos_voxel

class VoxelElementosDemo:
    def __init__(self):
        self.voxel_grid = {"matrix": [[[1,0],[0,1]]], "pitch":[1], "transform":[[0,0,0,0],[0,0,0,0],[0,0,0,0]]}
        self.centro_modelo = [0,0,0]
        self.cores_voxel = {(0,0,0): "#ff0000", (0,1,0): "#00ff00"}
        self.uvs_voxel = {(0,0,0): [0.1,0.2], (0,1,0): [0.3,0.4]}
        self.config = {"modo_otimizacao":"none","escala":1.0,"altura":0.0,"fator_voxel":1.0}

    def gerar_elementos(self):
        """Simula geração de elementos voxel"""
        elementos = gerar_elementos_voxel(
            self.voxel_grid,
            self.centro_modelo,
            self.cores_voxel,
            self.uvs_voxel,
            self.config
        )
        print("🧱 Elementos gerados:")
        for el in elementos:
            print(f"De {el['from']} até {el['to']} | Cor: {el['color']} | UV: {el['uv']}")
        return elementos

# Exemplo de uso
if __name__ == "__main__":
    demo = VoxelElementosDemo()

    # Gerar elementos voxel
    demo.gerar_elementos()
