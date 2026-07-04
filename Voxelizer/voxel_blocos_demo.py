"""
Exemplo simplificado de Voxel Blocos.
Mostra como calcular limites, criar elementos e gerar cubos Bedrock.
"""

from voxel_blocos import calcular_voxel_bounds, gerar_faces_voxel, criar_elemento_voxel, gerar_cubo_bedrock

class VoxelBlocosDemo:
    def __init__(self):
        self.elementos = []

    def criar_voxel(self, x, y, z):
        """Simula criação de um voxel"""
        from_coord, to_coord = calcular_voxel_bounds(
            x, y, z,
            largura=1, altura_bloco=1, profundidade=1,
            origem=(0,0,0), pitch_x=1, pitch_y=1, pitch_z=1,
            escala=1, altura=0, fator_voxel=1
        )
        elemento = criar_elemento_voxel(from_coord, to_coord, "#ff0000", [x,y,z], len(self.elementos))
        self.elementos.append(elemento)
        print(f"🧱 Voxel criado: de {from_coord} até {to_coord}, cor {elemento['color']}")

    def gerar_faces(self, ref_textura="#layer0"):
        """Simula geração de faces de voxel"""
        faces = gerar_faces_voxel(ref_textura)
        print(f"🎨 Faces geradas: {faces}")
        return faces

    def gerar_cubo_bedrock(self, indice=0):
        """Simula geração de cubo para Bedrock"""
        if not self.elementos:
            print("Nenhum elemento voxel criado.")
            return None
        cubo = gerar_cubo_bedrock(self.elementos[indice])
        print(f"🎮 Cubo Bedrock gerado: {cubo}")
        return cubo

# Exemplo de uso
if __name__ == "__main__":
    demo = VoxelBlocosDemo()

    # Criar voxel
    demo.criar_voxel(0,0,0)

    # Gerar faces
    demo.gerar_faces()

    # Gerar cubo Bedrock
    demo.gerar_cubo_bedrock()
