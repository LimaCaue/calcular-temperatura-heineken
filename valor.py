print("=== VALORES HEINEKEN ===")
print("1 - Heineken Lata: R$ 5,00")
print("2 - Heineken Long Neck: R$ 7,00")
print("3 - Heineken Garrafa: R$ 12,00")

opcao = int(input("Escolha o modelo: "))

if opcao == 1:
    print("Valor: R$ 5,00")
elif opcao == 2:
    print("Valor: R$ 7,00")
elif opcao == 3:
    print("Valor: R$ 12,00")
else:
    print("Opção inválida!")