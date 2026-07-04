"""
Exemplo simplificado de Dependências.
Mostra como verificar e instalar pacotes críticos.
"""

class DependenciasDemo:
    def __init__(self):
        self.instalados = set()

    def verificar_dependencias(self):
        """Simula verificação de dependências críticas"""
        print("--- Verificando dependências críticas ---")
        if "rtree" not in self.instalados:
            print("⚠️ Dependência 'rtree' não encontrada. Essencial para mapeamento UV.")
            self.instalar_pacote("rtree")
        else:
            print("✅ 'rtree' já está instalado.")
        print("--- Verificação concluída ---")

    def instalar_pacote(self, pacote):
        """Simula instalação de um pacote"""
        print(f"📦 Instalando {pacote}...")
        # Simulação de sucesso
        self.instalados.add(pacote)
        print(f"✅ {pacote} instalado com sucesso.")

# Exemplo de uso
if __name__ == "__main__":
    demo = DependenciasDemo()

    # Verificar dependências
    demo.verificar_dependencias()

    # Rodar novamente para mostrar que já está instalado
    demo.verificar_dependencias()
