"""
Exemplo simplificado de Gerenciador de Projeto.
Mostra como salvar e carregar projetos no formato .i3d.
"""

import zipfile
import tempfile
import os
import json

EXTENSAO_PROJETO = ".i3d"

class GerenciadorProjetoDemo:
    def __init__(self):
        self.projeto = {"versao": "3.0", "texturas_ocultas": []}

    def salvar_projeto(self, caminho_pacote: str) -> bool:
        """Simula salvar projeto em um arquivo .i3d"""
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                # Cria arquivos fictícios
                caminho_glb = os.path.join(temp_dir, "scene.glb")
                with open(caminho_glb, "w") as f:
                    f.write("Simulação de cena 3D")

                caminho_json = os.path.join(temp_dir, "project.json")
                with open(caminho_json, "w", encoding="utf-8") as f:
                    json.dump(self.projeto, f, indent=4)

                # Compacta em .i3d
                with zipfile.ZipFile(caminho_pacote, "w", zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(caminho_glb, arcname="scene.glb")
                    zipf.write(caminho_json, arcname="project.json")
            print(f"Projeto salvo em {caminho_pacote}")
            return True
        except Exception as e:
            print(f"Erro ao salvar projeto: {e}")
            return False

    def carregar_projeto(self, caminho_pacote: str):
        """Simula carregar projeto de um arquivo .i3d"""
        try:
            with zipfile.ZipFile(caminho_pacote, "r") as zipf:
                zipf.extractall("projeto_temp")
            print(f"Projeto carregado de {caminho_pacote}")
            return True
        except Exception as e:
            print(f"Erro ao carregar projeto: {e}")
            return False

# Exemplo de uso
if __name__ == "__main__":
    demo = GerenciadorProjetoDemo()
    arquivo = "meu_projeto.i3d"

    # Salvar projeto
    demo.salvar_projeto(arquivo)

    # Carregar projeto
    demo.carregar_projeto(arquivo)
