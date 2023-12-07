def comparacao(proteinas_50: dict, proteinas_70: dict, tipo: str):
    """
    Função responsável por comparar as listas de proteínas.
    :param proteinas_50: Dicionário com as proteínas de 50%.
    :param proteinas_70: Dicionário com as proteínas de 70%.
    :param tipo: Qual proteína está sendo comparada.
    """
    # --- Separar as proteínas em listas --- #
    lista_proteinas_50 = []
    for proteinas in proteinas_50.values():
        for proteina in proteinas:
            if proteina not in lista_proteinas_50:
                lista_proteinas_50.append(proteina)

    lista_proteinas_70 = []
    for proteinas in proteinas_70.values():
        for proteina in proteinas:
            if proteina not in lista_proteinas_70:
                lista_proteinas_70.append(proteina)


    # --- Colocar todas as informações dentro de um documento --- #
    with open('comparacao.txt', 'a') as txt:
        # --- Comparar as listas (50% a 59%) --- #
        proteinas = ''  # se não retornar nenhum valor, indica que as proteínas tem semelhança de >=50%
        for proteina in lista_proteinas_50:
            if proteina not in lista_proteinas_70:
                proteinas += f'{proteina}%'

        txt.write(f'{tipo}\n')
        txt.write('\tProteínas de 50% a 69%:\n')
        proteinas_split = proteinas.split('%')
        for proteina in proteinas_split:
            if proteina != '':
                for cluster, proteinas in proteinas_50.items():
                    if proteina in proteinas:
                        txt.write(f'\t\t- {proteina} (Cluster: {cluster})\n')

        # --- Comparar as listas (>=70%) --- #
        proteinas = ''
        for proteina in lista_proteinas_70:
            if proteina not in lista_proteinas_50:
                proteinas += f'{proteina}%'
                
        txt.write('\tProteínas >= 70%:\n')
        proteinas_split = proteinas.split('%')
        for proteina in proteinas_split:
            if proteina != '':
                for cluster, proteinas in proteinas_70.items():
                    if proteina in proteinas:
                        txt.write(f'\t\t- {proteina} (Cluster: {cluster})\n')
        txt.write('\n\n')

    print('Arquivo criado!')
    
