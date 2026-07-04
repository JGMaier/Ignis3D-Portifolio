"""
Exemplo simplificado de Compactação Greedy Meshing.
Mostra como reduzir voxels adjacentes em blocos maiores.
"""

from compactacao_greedy import compactar_greedy

# Exemplo de voxels brutos
elementos_brutos = [
    {"voxel_coord": (0,0,0), "color": "red", "pitch": 1, "from": [0,0,0]},
    {"voxel_coord": (1,0,0), "color": "red", "pitch": 1, "from": [1,0,0]},
    {"voxel_coord": (0,1,0), "color": "red", "pitch": 1, "from": [0,1,0]},
    {"voxel_coord": (1,1,0), "color": "red", "pitch": 1, "from": [1,1,0]},
    {"voxel_coord": (0,0,1), "color": "blue", "pitch": 1, "from": [0,0,1]},
]

# Aplica compactação
elementos_otimizados = compactar_greedy(elementos_brutos)

# Exibe resultado
print("=== Elementos Otimizados ===")
for el in elementos_otimizados:
    print(f"De {el['from']} até {el['to']} | Cor: {el['color']} | Faces expostas: {el['exposed_faces']}")
