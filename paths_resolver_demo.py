"""
Exemplo simplificado de Paths Resolver.
Mostra como acessar diretórios e recursos da aplicação Ignis3D.
"""

import os
from pathlib import Path

class PathsResolverDemo:
    def __init__(self):
        self.base_dir = Path(os.getcwd())
        self.user_dir = Path.home() / "Documents" / "Ignis3D"

    def get_base_dir(self):
        """Retorna diretório base"""
        print(f"Base Dir: {self.base_dir}")
        return self.base_dir

    def get_user_dir(self):
        """Retorna diretório do usuário"""
        print(f"User Dir: {self.user_dir}")
        return self.user_dir

    def get_packs_dir(self):
        """Retorna pasta de packs"""
        packs = self.user_dir / "packs"
        print(f"Packs Dir: {packs}")
        return packs

    def get_cenary_dir(self):
        """Retorna pasta de cenários"""
        cenary = self.user_dir / "cenary"
        print(f"Cenary Dir: {cenary}")
        return cenary

    def get_skybox_dir(self):
        """Retorna pasta de skybox"""
        skybox = self.user_dir / "skybox"
        print(f"Skybox Dir: {skybox}")
        return skybox

    def get_settings_path(self):
        """Retorna arquivo de configurações"""
        settings = self.user_dir / "settings.json"
        print(f"Settings Path: {settings}")
        return settings

    def get_recentes_path(self):
        """Retorna arquivo de recentes"""
        recentes = self.user_dir / "recentes.txt"
        print(f"Recentes Path: {recentes}")
        return recentes

# Exemplo de uso
if __name__ == "__main__":
    demo = PathsResolverDemo()

    demo.get_base_dir()
    demo.get_user_dir()
    demo.get_packs_dir()
    demo.get_cenary_dir()
    demo.get_skybox_dir()
    demo.get_settings_path()
    demo.get_recentes_path()
