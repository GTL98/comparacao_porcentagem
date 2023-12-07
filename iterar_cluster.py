# --- Importar as bibliotecas --- #
from Bio import SeqIO
from clusters_50 import *
from clusters_70 import *
from comparacao import comparacao

# --- Pasta com os clusters --- #
caminho_50 = '../rafts3g_50/RAFTS3GClusters'
caminho_70 = '../rafts3g_70/RAFTS3GClusters'


# --- Função para iterar sobre os clusters --- #
def iterar_cluster(clusters:str):
    """
    Função responsável por iterar sobre os clusters.
    :param clusters: Cluster informado.
    """
    # --- Tratar a entrada --- #
    item_50 = f'{clusters}_50'
    item_70 = f'{clusters}_70'

    # --- Listas de cada função 50% --- #
    dic_eps_50 = {}
    dic_bile_50 = {}
    dic_adesao_50 = {}
    dic_carbono_50 = {}
    dic_estresse_50 = {}
    dic_manosidase_50 = {}
    dic_fosfolipase_50 = {}
    dic_acido_folico_50 = {}
    dic_bacteriocinas_50 = {}
    dic_betagalactosidase_50 = {}

    # --- Listas de cada função 70% --- #
    dic_eps_70 = {}
    dic_bile_70 = {}
    dic_adesao_70 = {}
    dic_carbono_70 = {}
    dic_estresse_70 = {}
    dic_manosidase_70 = {}
    dic_fosfolipase_70 = {}
    dic_acido_folico_70 = {}
    dic_bacteriocinas_70 = {}
    dic_betagalactosidase_70 = {}
    
    
    # --- Iterar sobre cada cluster 50 % --- #
    if item_50 == 'eps_50':
        for cluster in eps_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('EPS', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_eps_50[cluster] = proteinas

    if item_50 == 'bile_50':
        for cluster in bile_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('acido biliar', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_bile_50[cluster] = proteinas

    if item_50 == 'adesao_50':
        for cluster in adesao_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('adesao', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_adesao_50[cluster] = proteinas

    if item_50 == 'carbono_50':
        for cluster in carbono_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('metabolismo carbono', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_carbono_50[cluster] = proteinas

    if item_50 == 'estresse_50':
        for cluster in estresse_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('metabolismo carbono', '').replace('resistencia estresse', '').replace('estresse calor', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_estresse_50[cluster] = proteinas

    if item_50 == 'manosidase_50':
        for cluster in manosidase_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('Alpha-mannosidase manosidase', 'Alpha-mannosidase').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_manosidase_50[cluster] = proteinas

    if item_50 == 'fosfolipase_50':
        for cluster in fosfolipase_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('fosfolipase', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_fosfolipase_50[cluster] = proteinas

    if item_50 == 'acido_folico_50':
        for cluster in acido_folico_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('acido folico', '').replace('cido folico', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_acido_folico_50[cluster] = proteinas

    if item_50 == 'bacteriocinas_50':
        for cluster in bacteriocinas_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('bacteriocina', '').replace('cido folico', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_bacteriocinas_50[cluster] = proteinas

    if item_50 == 'betagalactosidase_50':
        for cluster in betagalactosidase_50:
            registro = SeqIO.parse(f'{caminho_50}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('beta galactosidase', '').replace('cido folico', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_betagalactosidase_50[cluster] = proteinas

    # --- Iterar sobre cada cluster 50 % --- #
    if item_70 == 'eps_70':
        for cluster in eps_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('EPS', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_eps_70[cluster] = proteinas
                    
        comparacao(dic_eps_50, dic_eps_70, 'EPS')

    if item_70 == 'bile_70':
        for cluster in bile_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('acido biliar', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_bile_70[cluster] = proteinas
        comparacao(dic_bile_50, dic_bile_70, 'Sais biliares')

    if item_70 == 'adesao_70':
        for cluster in adesao_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('adesao', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_adesao_70[cluster] = proteinas
        comparacao(dic_adesao_50, dic_adesao_70, 'Proteína de adesão')

    if item_70 == 'carbono_70':
        for cluster in carbono_50:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('metabolismo carbono', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_carbono_70[cluster] = proteinas
        comparacao(dic_carbono_50, dic_carbono_70, 'Metabolismo do carbono')

    if item_70 == 'estresse_70':
        for cluster in estresse_50:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('metabolismo carbono', '').replace('resistencia estresse', '').replace('estresse calor', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_estresse_70[cluster] = proteinas
        comparacao(dic_estresse_50, dic_estresse_70, 'Resistência ao estresse')

    if item_70 == 'manosidase_70':
        for cluster in manosidase_50:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('Alpha-mannosidase manosidase', 'Alpha-mannosidase').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_manosidase_70[cluster] = proteinas
        comparacao(dic_manosidase_50, dic_manosidase_70, 'Manosidase')

    if item_70 == 'fosfolipase_70':
        for cluster in fosfolipase_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('fosfolipase', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_fosfolipase_70[cluster] = proteinas
        comparacao(dic_fosfolipase_50, dic_fosfolipase_70, 'Fosfolipase')

    if item_70 == 'acido_folico_70':
        for cluster in acido_folico_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('acido folico', '').replace('cido folico', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_acido_folico_70[cluster] = proteinas
        comparacao(dic_acido_folico_50, dic_acido_folico_70, 'Ácido fólico')

    if item_70 == 'bacteriocinas_70':
        for cluster in bacteriocinas_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('bacteriocina', '').replace('cido folico', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_bacteriocinas_70[cluster] = proteinas
        comparacao(dic_bacteriocinas_50, dic_bacteriocinas_70, 'Bacteriocinas')

    if item_70 == 'betagalactosidase_70':
        for cluster in betagalactosidase_70:
            registro = SeqIO.parse(f'{caminho_70}/Cluster_{cluster}.fasta', 'fasta')
            proteinas = []
            for entrada in registro:
                cabecalho = entrada.description.split('|')[1].split('.1')[1].split('[')[0].strip()
                cabecalho = cabecalho.replace('MULTISPECIES: ', '').replace('beta galactosidase', '').replace('cido folico', '').strip()
                if cabecalho not in proteinas:
                    proteinas.append(cabecalho)
                    dic_betagalactosidase_70[cluster] = proteinas
        comparacao(dic_betagalactosidase_50, dic_betagalactosidase_70, 'Betagalactosidase')
        
