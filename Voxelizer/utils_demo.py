"""
Exemplo simplificado de Utils.
Mostra funções auxiliares para voxelização e exportação.
"""

from PIL import Image

class UtilsDemo:
    def garantir_pasta(self, caminho):
        print(f"📁 Garantindo que a pasta '{caminho}' exista.")

    def caminho_normalizado(self, caminho):
        print(f"📄 Caminho normalizado: {caminho}")
        return caminho

    def arredondar_coords(self, coords, casas_decimais=2):
        arredondado = [round(c, casas_decimais) for c in coords]
        print(f"🔢 Coordenadas arredondadas: {arredondado}")
        return arredondado

    def centro_entre(self, from_coord, to_coord):
        centro = [(f + t) / 2 for f, t in zip(from_coord, to_coord)]
        print(f"🧠 Centro entre pontos: {centro}")
        return centro

    def calcular_escala_uniforme(self, extents, resolucao_voxel):
        escala = resolucao_voxel / max(extents)
        print(f"📐 Escala uniforme calculada: {escala}")
        return escala

    def gerar_imagem_textura(self, caminho_textura):
        """Simula geração de uma textura simples"""
        imagem = Image.new("RGBA", (64, 64), (255, 0, 0, 255))  # Quadrado vermelho
        imagem.save(caminho_textura)
        print(f"🖼️ Textura gerada e salva em: {caminho_textura}")

# Exemplo de uso
if __name__ == "__main__":
    demo = UtilsDemo()

    # Garantir pasta
    demo.garantir_pasta("modelos")

    # Normalizar caminho
    demo.caminho_normalizado("modelos/exemplo.json")

    # Arredondar coordenadas
    demo.arredondar_coords([1.23456, 7.89123])

    # Calcular centro
    demo.centro_entre([0, 0, 0], [2, 2, 2])

    # Calcular escala
    demo.calcular_escala_uniforme([10, 20, 30], 32)

    # Gerar textura
    demo.gerar_imagem_textura("atlas_textura.png")
