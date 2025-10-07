# Aqui arnazena os gastos
print("🚀 Programa iniciado!")
gastos  = []

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

# * Função para exibição do mebnu de escolhas
def menu():
    while True:
        print("==== Menu ====")
        print('1. Adicionar gasto')
        print('2. Listar gastos')
        print('3. Mostrar total gasto')
        print('4. Sair')
        opcao = input('O que deseja? ')
        
# * opções de escolhas dentro do menu
        if opcao == '1':
            adicionar_gasto()
        elif opcao == '2':
            listar_gastos()
        elif opcao == '3':
            total_gastos()
        elif opcao == '4':
            print('Finalizando consulta')
            break
        else: 
            print('Opção inválida; tente novamente.\n')


menu()

