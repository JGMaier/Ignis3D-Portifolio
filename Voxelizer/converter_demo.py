"""
Exemplo simplificado de Converter.
Detecta extensão do modelo e chama o conversor correto.
"""

class ConverterDemo:
    def __init__(self):
        pass

    def converter_modelo(self, caminho_modelo):
        """Detecta extensão e chama conversor correspondente"""
        extensao = caminho_modelo.split(".")[-1].lower()

        if extensao == "glb":
            return self._converter_glb(caminho_modelo)
        elif extensao == "gltf":
            return self._converter_gltf(caminho_modelo)
        elif extensao == "obj":
            return self._converter_obj(caminho_modelo)
        elif extensao == "fbx":
            return self._converter_fbx(caminho_modelo)
        else:
            print(f"❌ Extensão '{extensao}' não suportada.")
            return False

    def _converter_glb(self, caminho):
        print(f"Convertendo modelo GLB: {caminho}")
        return True

    def _converter_gltf(self, caminho):
        print(f"Convertendo modelo GLTF: {caminho}")
        return True

    def _converter_obj(self, caminho):
        print(f"Convertendo modelo OBJ: {caminho}")
        return True

    def _converter_fbx(self, caminho):
        print(f"Convertendo modelo FBX: {caminho}")
        return True

# Exemplo de uso
if __name__ == "__main__":
    demo = ConverterDemo()

    # Testar com diferentes formatos
    demo.converter_modelo("exemplo_modelo.glb")
    demo.converter_modelo("exemplo_modelo.gltf")
    demo.converter_modelo("exemplo_modelo.obj")
    demo.converter_modelo("exemplo_modelo.fbx")
    demo.converter_modelo("exemplo_modelo.3ds")
