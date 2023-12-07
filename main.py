# --- Importar o módulo --- #
from iterar_cluster import iterar_cluster


# --- Lista com os termos --- #
termos = [
    'eps',
    'bile',
    'adesao',
    'carbono',
    'estresse',
    'manosidase',
    'fosfolipase',
    'acido_folico',
    'bacteriocinas',
    'tolerancia_acido',
    'betagalactosidase'
    ]

# --- Loop sobre cada proteína --- #
for termo in termos:
    iterar_cluster(termo)
