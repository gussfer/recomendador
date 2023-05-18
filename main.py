from recomendador_db import pratos

# Função para coletar informações do usuário
def coletar_preferencias():
    print('Bem-vindo ao nosso sistema de recomendação de pratos!')
    print('Por favor, responda algumas perguntas para obtermos suas preferências.')

    preferencias = {}

    categorias_list = ['• sobremesas', '• massas', '• carnes']
    preferencias['categoria'] = input('Qual categoria de prato você prefere?\n' + '\n'.join(categorias_list) + '\n')
    
    #ingredientes_list = ['• limão', '• chocolate', '• molho de tomate', '• sal', '• queijo', '• pimenta', '• açucar']
    preferencias['ingrediente'] = input('Qual ingrediente você gosta?\n')#\n' + '\n'.join(ingredientes_list) + '\n'

    return preferencias


# Função para calcular a similaridade entre pratos
def calcular_similaridade(prato, preferencias):
    ingredientes_prato = prato['ingredientes'] #[ingredientes[2] for ingredientes in pratos]
    categoria_prato = prato['categorias'] #[categorias[3] for categorias in pratos]

    ingrediente_preferido = preferencias['ingrediente']
    categoria_preferida = preferencias['categoria']

    # Calcula a similaridade baseado nos ingredientes e categorias
    ingrediente_similaridade = 0
    if ingrediente_preferido in ingredientes_prato:
        ingrediente_similaridade = 1

    categoria_similaridade = 0
    if categoria_preferida in categoria_prato:
        categoria_similaridade = 1

    similaridade = (ingrediente_similaridade + categoria_similaridade) / 2
    return similaridade

# Função para gerar recomendações de pratos
def gerar_recomendacoes(pratos, preferencias, quantidade=3):
    recomendacoes = []

    for prato in pratos:
        similaridade = calcular_similaridade(prato, preferencias)
        recomendacoes.append((prato, similaridade))

    # Ordena as recomendações por similaridade (mais similar primeiro)
    recomendacoes = sorted(recomendacoes, key=lambda x: x[1], reverse=True)

    # Retorna apenas os pratos recomendados
    recomendacoes = [rec[0] for rec in recomendacoes]

    return recomendacoes[:quantidade]


# Função para exibir as recomendações
def exibir_recomendacoes(recomendacoes):
    print('\nRecomendações de pratos para você:')
    for i, prato in enumerate(recomendacoes, start=1):
        print(f'{i}. {prato["nome"]}')
        print(f'Descrição: {prato["descricao"]}')
        print('---')

# Fluxo principal do programa
preferencias_usuario = coletar_preferencias() # melhorar a lista contendo as categorias disponíveis
recomendacoes = gerar_recomendacoes(pratos, preferencias_usuario)
exibir_recomendacoes(recomendacoes)



