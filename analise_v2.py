# * =======Analisador de gastos - versão 2 (com saldo e categorias) ====== * 
# Aqui arnazena os gastos
gastos  = []
saldo_inicial = 0.0

# * Função para adicionar saldo
def Iniciar_saldo():
    global saldo_inicial
    saldo_inicial = float(input('Digite o seu saldo inicial: R$ '))
    print(f'Saldo inicial definido: R$ {saldo_inicial:.2f}\n')

#* Função para adicionar os gastos
def adicionar_gasto():
    descricao = input("Descrição do gasto: ")
    categoria = input("Categoria: ")
    valor = float(input("Valor do gasto: R$ "))
    gastos.append({"descrição": descricao, "categoria": categoria, "valor": valor})
    print("Novo gasto registrado!\n")

# * Função para listar os gastos inseridos
def listar_gastos():
    if not gastos:
        print("Nenhum registro de gasto ainda.\n")
        return
    print("\n=== Lista de gastos ===")
    for g in gastos:
        print(f'{g['descrição']} - {g['categoria']} - {g['valor']:.2f}')
        print("* ***************************************************** *")

# * Função para somar todos os gastos
def total_gastos():
    total = sum(g['valor'] for g in gastos)
    print(f'Total gasto: R$ {total:.2f}\n')
    print(f'Saldo restante: R$ {saldo_inicial - total:.2f}\n')

#  * Criada a função: resumo por categoria
def resumo_por_categoria():
    resumo = {}
    for gasto in gastos:
        cat = gasto['categoria']
        valor = gasto['valor']
        if cat in resumo:
            resumo[cat] += valor
        else:
            resumo[cat] = valor

    print('\n====== Resumo por categoria ======')
    for categoria, total in resumo.items():
        print(f'{categoria}: R$ {total:.2f}')

# * Função para exibição do menu de escolhas
def menu():
    Iniciar_saldo()
    while True:
        print("==== Menu ====")
        print('1. Adicionar gasto')
        print('2. Listar gastos')
        print('3. Mostrar total e saldo restante')
        print('4. Resumo por categoria')
        print('5. Sair')
        opcao = input('O que deseja? ')
        
# * opções de escolhas dentro do menu
        if opcao == '1':
            adicionar_gasto()
        elif opcao == '2':
            listar_gastos()
        elif opcao == '3':
            total_gastos()
        elif opcao == '4':
            resumo_por_categoria()
        elif opcao == '5':
            print('Consulta finalizada')
            break
        else: 
            print('Opção inválida; tente novamente.\n')


menu()

