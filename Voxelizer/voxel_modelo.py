"""
Exemplo simplificado de Voxel Modelo.
Mostra como gerar modelos Java e Bedrock a partir de elementos voxel.
"""

from voxel_modelo import gerar_modelo_java, gerar_modelo_bedrock

class VoxelModeloDemo:
    def __init__(self):
        self.elementos = [
            {"from":[0,0,0],"to":[1,1,1],"color":"#ff0000","uv":[0.1,0.2],"exposed_faces":{"north","south"}},
            {"from":[1,0,0],"to":[2,1,1],"color":"#00ff00","uv":[0.3,0.4],"exposed_faces":{"east","west"}},
            {"from":[0,1,0],"to":[1,2,1],"color":"#0000ff","uv":[0.5,0.6],"exposed_faces":{"up","down"}}
        ]
        self.config = {"fator_encolhimento_uv":0.1}

    def gerar_java(self):
        """Simula geração de modelo Java"""
        modelo_java = gerar_modelo_java("exemplo_modelo", self.elementos, 64, 64, self.config)
        print("🎮 Modelo Java gerado:")
        print(modelo_java)
        return modelo_java

    def gerar_bedrock(self):
        """Simula geração de modelo Bedrock"""
        modelo_bedrock = gerar_modelo_bedrock("exemplo_modelo", self.elementos, 64, 64)
        print("🎮 Modelo Bedrock gerado:")
        print(modelo_bedrock)
        return modelo_bedrock

# Exemplo de uso
if __name__ == "__main__":
    demo = VoxelModeloDemo()

    # Gerar modelo Java
    demo.gerar_java()

    # Gerar modelo Bedrock
    demo.gerar_bedrock()
