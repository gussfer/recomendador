# Dados dos pratos do restaurante (exemplo)
    # cria uma lista de dicionarios Python contendo informações relevantes para as recomendações
pratos = [
    {
        'nome': 'Lasanha',
        'descricao': 'Deliciosa lasanha de carne com molho de tomate.',
        'ingredientes': ['carne', 'massa', 'queijo', 'molho de tomate'],
        'categorias': ['massas', 'carnes']
    },
    {
        'nome': 'Sopa de legumes',
        'descricao': 'Sopa reconfortante feita com diversos legumes.',
        'ingredientes': ['cenoura', 'batata', 'abóbora', 'ervilha'],
        'categorias': ['sopas', 'vegetariano']
    },
    {
        'nome': 'Pudim de chocolate',
        'descricao': 'Sobremesa irresistível de pudim de chocolate.',
        'ingredientes': ['leite condensado', 'cacau em pó', 'ovos', 'açúcar'],
        'categorias': ['sobremesas', 'chocolate']
    },
    {
        'nome': 'Salada Caesar',
        'descricao': 'Salada clássica com alface, croutons, queijo parmesão e molho Caesar.',
        'ingredientes': ['alface', 'croutons', 'queijo parmesão', 'molho Caesar'],
        'categorias': ['saladas', 'leve']
    },
    {
        'nome': 'Frango à parmegiana',
        'descricao': 'Frango empanado coberto com molho de tomate e queijo derretido.',
        'ingredientes': ['frango', 'molho de tomate', 'queijo', 'farinha de trigo'],
        'categorias': ['carnes', 'frango']
    },
    {
        'nome': 'Risoto de cogumelos',
        'descricao': 'Risoto cremoso preparado com cogumelos frescos.',
        'ingredientes': ['arroz arbóreo', 'cogumelos', 'cebola', 'caldo de legumes'],
        'categorias': ['risotos', 'vegetariano']
    },
    {
        'nome': 'Mousse de limão',
        'descricao': 'Sobremesa refrescante com sabor cítrico de limão.',
        'ingredientes': ['leite condensado', 'suco de limão', 'creme de leite', 'raspas de limão'],
        'categorias': ['sobremesas', 'frutas']
    },
    {
        'nome': 'Hambúrguer vegetariano',
        'descricao': 'Delicioso hambúrguer vegetariano feito com legumes e grãos.',
        'ingredientes': ['grão-de-bico', 'cenoura', 'aveia', 'temperos'],
        'categorias': ['sanduíches', 'vegetariano']
    },
    {
        'nome': 'Torta de maçã',
        'descricao': 'Torta doce de maçã com massa crocante e recheio suculento.',
        'ingredientes': ['maçãs', 'açúcar', 'canela', 'massa folhada'],
        'categorias': ['sobremesas', 'frutas']
    },

    # Adicione mais pratos aqui
]


# Função para coletar informações do usuário
def coletar_preferencias():
    print('Bem-vindo ao nosso sistema de recomendação de pratos!')
    print('Por favor, responda algumas perguntas para obtermos suas preferências.')

    preferencias = {}

    categorias_list = ['• sobremesas', '• massas', '• carnes', '• sanduíches', '• risotos', '• sopas', '• vegetariano']
    preferencias['categoria'] = input('Qual categoria de prato você prefere?\n' + '\n'.join(categorias_list) + '\n')
    
    ingredientes_list = ['• limão', '• chocolate', '• molho de tomate', '• sal', '• queijo', '• pimenta', '• açucar']
    preferencias['ingrediente'] = input('Qual ingrediente você gosta?\n' + '\n'.join(ingredientes_list) + '\n')

    return preferencias


# Função para calcular a similaridade entre pratos
def calcular_similaridade(prato, preferencias):
    ingredientes_prato = prato['ingredientes']
    categoria_prato = prato['categorias']

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



