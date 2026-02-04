    #COMO TESTAR TODAS AS OPÇÕES DE UMA VEZ????
    #LIBERAR PARA REPETIÇÃO
    #FOR WHILE

print("\nOpções")
print("\n1 - Par ou Impar")
print("\n2 - Verifique o número")
print("\n3 - Dobro")

continuar = "s"
while continuar == "s":
    op = int(input("Digite uma opção:"))
    match op:
        case 1:
            print("\n1 - Par ou Impar")
            num = int(input("Digite um número: "))
            if num % 2 == 0:
                print(f"\n{num} é par")
            else:
                print(f"\n{num} é impar")

        case 2:  
            print("\n2 - Verifique o número")             
            valor1 = float(input("Insira o 1º número: "))
            valor2 = float(input("Insira o 2º número: "))
            if valor1 > valor2:
                print("\nO maior é: ", valor1)
            elif valor2 > valor1:
                print("\nO maior é: ", valor2)
            else:
                print("\nOs valores são iguais")

        case 3:
            print("\n3 - Dobro")
            num = float(input("Digite um número: "))
            print(f"O dobro do número é: {num*2}")

        case _:
            print("Opção inválida!")
    continuar = input("Deseja continuar? (s/n) ").lower().strip() #apaga os espaços _s
    if continuar != "s":
        print("\nPrograma Encerrado")
        break #interromper a linha de comando do case