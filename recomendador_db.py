# Dados dos pratos do restaurante (exemplo)
    # cria uma lista de dicionarios Python contendo informações relevantes para as recomendações
pratos = [
    # Carnes 
     {
        'nome': 'Bife à Parmegiana',
        'descricao': 'Bife empanado coberto com molho de tomate e queijo derretido.',
        'ingredientes': ['bife', 'molho de tomate', 'queijo', 'farinha de trigo'],
        'categorias': ['carnes', 'frango']
    },
    {
        'nome': 'Churrasco de Picanha',
        'descricao': 'Suculento churrasco de picanha com temperos especiais.',
        'ingredientes': ['picanha', 'sal grosso', 'temperos'],
        'categorias': ['carnes', 'churrasco']
    },
    {
        'nome': 'Costelinha de Porco Assada',
        'descricao': 'Costelinha de porco assada com molho barbecue.',
        'ingredientes': ['costelinha de porco', 'molho barbecue'],
        'categorias': ['carnes', 'porco']
    },
    {
        'nome': 'Filé Mignon ao Molho Madeira',
        'descricao': 'Tender filé mignon grelhado servido com molho madeira.',
        'ingredientes': ['filé mignon', 'molho madeira'],
        'categorias': ['carnes', 'bovina']
    },
    {
        'nome': 'Frango à Cordon Bleu',
        'descricao': 'Peito de frango recheado com presunto e queijo, empanado e frito.',
        'ingredientes': ['frango', 'presunto', 'queijo', 'farinha de trigo'],
        'categorias': ['carnes', 'frango']
    },
    {
        'nome': 'Carne de Panela',
        'descricao': 'Carne cozida lentamente em molho de tomate com legumes.',
        'ingredientes': ['carne', 'molho de tomate', 'legumes'],
        'categorias': ['carnes', 'cozidos']
    },
    {
        'nome': 'Espetinho de Carne',
        'descricao': 'Espetinho de carne bovina grelhado com temperos.',
        'ingredientes': ['carne bovina', 'temperos'],
        'categorias': ['carnes', 'churrasco']
    },
    {
        'nome': 'Ribs de Porco ao Molho Barbecue',
        'descricao': 'Costelas de porco assadas e cobertas com molho barbecue.',
        'ingredientes': ['costelas de porco', 'molho barbecue'],
        'categorias': ['carnes', 'porco']
    },
    {
        'nome': 'Risoto de Camarão',
        'descricao': 'Risoto cremoso preparado com camarões frescos.',
        'ingredientes': ['arroz arbóreo', 'camarões', 'cebola', 'caldo de legumes'],
        'categorias': ['carnes', 'frutos do mar']
    },
    {
        'nome': 'Lombo de Porco Assado',
        'descricao': 'Lombo de porco assado com temperos e especiarias.',
        'ingredientes': ['lombo de porco', 'temperos'],
        'categorias': ['carnes', 'porco']
    },
    # Massas 
    {
        'nome': 'Lasanha',
        'descricao': 'Deliciosa lasanha de carne com molho de tomate.',
        'ingredientes': ['carne', 'massa', 'queijo', 'molho de tomate'],
        'categorias': ['massas', 'carnes']
    },
    {
        'nome': 'Spaghetti à Carbonara',
        'descricao': 'Massa de spaghetti com molho à base de ovos, queijo parmesão e bacon.',
        'ingredientes': ['ovos', 'queijo parmesão', 'bacon'],
        'categorias': ['massas', 'bacon']
    },
    {
        'nome': 'Fettuccine Alfredo',
        'descricao': 'Massa de fettuccine com molho cremoso à base de queijo parmesão e manteiga.',
        'ingredientes': ['queijo parmesão', 'manteiga'],
        'categorias': ['massas', 'molho branco']
    },
    {
        'nome': 'Ravióli de Queijo',
        'descricao': 'Deliciosos raviólis recheados com queijo e servidos com molho de tomate.',
        'ingredientes': ['queijo', 'molho de tomate'],
        'categorias': ['massas', 'vegetariano']
    },
    {
        'nome': 'Macarrão com Frutos do Mar',
        'descricao': 'Macarrão com frutos do mar, como camarões, lulas e mexilhões, em molho de tomate.',
        'ingredientes': ['camarões', 'lulas', 'mexilhões', 'molho de tomate'],
        'categorias': ['massas', 'frutos do mar']
    },
    {
        'nome': 'Tortellini de Espinafre e Ricota',
        'descricao': 'Tortellinis recheados com espinafre e ricota, servidos com molho de tomate.',
        'ingredientes': ['espinafre', 'ricota', 'molho de tomate'],
        'categorias': ['massas', 'vegetariano']
    },
    {
        'nome': 'Penne à Puttanesca',
        'descricao': 'Massa de penne com molho à base de tomates, azeitonas, alcaparras e anchovas.',
        'ingredientes': ['tomates', 'azeitonas', 'alcaparras', 'anchovas'],
        'categorias': ['massas', 'molho de tomate']
    },
    {
        'nome': 'Tagliatelle ao Pesto',
        'descricao': 'Tagliatelle com molho pesto, feito com manjericão, alho, pinhões, queijo parmesão e azeite de oliva.',
        'ingredientes': ['manjericão', 'alho', 'pinhões', 'queijo parmesão'],
        'categorias': ['massas', 'pesto']
    },
    # Sobremesas
    {
        'nome': 'Torta de Limão',
        'descricao': 'Torta doce de limão com massa crocante e recheio cítrico.',
        'ingredientes': ['limão', 'açúcar', 'massa folhada'],
        'categorias': ['sobremesas', 'cítrico']
    },
    {
        'nome': 'Mousse de Chocolate',
        'descricao': 'Sobremesa leve e cremosa de mousse de chocolate.',
        'ingredientes': ['chocolate', 'creme de leite', 'açúcar'],
        'categorias': ['sobremesas', 'chocolate']
    },
    {
        'nome': 'Pudim de Leite Condensado',
        'descricao': 'Clássico pudim de leite condensado com calda de caramelo.',
        'ingredientes': ['leite condensado', 'açúcar', 'ovos'],
        'categorias': ['sobremesas', 'pudins']
    },
    {
        'nome': 'Cheesecake de Morango',
        'descricao': 'Cheesecake com base de biscoito e cobertura de morangos frescos.',
        'ingredientes': ['biscoito', 'cream cheese', 'morangos'],
        'categorias': ['sobremesas', 'cheesecakes']
    },
    {
        'nome': 'Tiramisu',
        'descricao': 'Sobremesa italiana clássica com camadas de biscoitos embebidos em café e creme de queijo.',
        'ingredientes': ['biscoitos', 'café', 'queijo mascarpone'],
        'categorias': ['sobremesas', 'italiano']
    },
    {
        'nome': 'Pavê de Chocolate',
        'descricao': 'Delicioso pavê de chocolate com camadas de biscoito e creme.',
        'ingredientes': ['chocolate', 'biscoito', 'creme de leite'],
        'categorias': ['sobremesas', 'chocolate']
    },
    {
        'nome': 'Sorvete de Baunilha',
        'descricao': 'Sorvete cremoso de baunilha com diversos acompanhamentos.',
        'ingredientes': ['baunilha', 'leite', 'açúcar'],
        'categorias': ['sobremesas', 'sorvetes']
    },
    {
        'nome': 'Brownie',
        'descricao': 'Delicioso brownie de chocolate com nozes.',
        'ingredientes': ['chocolate', 'nozes', 'açúcar'],
        'categorias': ['sobremesas', 'chocolate']
    },
    {
        'nome': 'Tarte Tatin',
        'descricao': 'Torta francesa de maçã caramelizada com massa crocante.',
        'ingredientes': ['maçãs', 'açúcar', 'massa folhada'],
        'categorias': ['sobremesas', 'frutas']
    },
    
    # Adicione mais pratos aqui
]
