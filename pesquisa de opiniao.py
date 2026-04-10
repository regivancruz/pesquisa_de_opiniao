# regivancruzAg8DSI
# sistema de pesquisa de Opinião sobre
# Inicialização dos contadores
excelente = 0
bom = 0 
ruim = 0

# definição da quantidade de entrevistados (usei 10 para teste e 50 para oficial)
total_entrevistados = 50  
# Laço de repetição FOR
for i in range(total_entrevistados):
    print(f"\nEntrevistado {i+1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Avaliação do atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção (1/2/3): "))

    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida! Esta resposta não será contabilizada.")

# Resultado final
print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas BOM: {bom}")
print(f"Quantidade de respostas RUIM: {ruim}")
