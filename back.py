def calculadora():
    print("Bem-vindo à calculadora!")
    print("Escolha uma das operações abaixo:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    while True:
        try:
            opcao = int(input("Digite o número da operação desejada (1-4): "))
            if opcao not in [1, 2, 3, 4]:
                print("Por favor, escolha uma opção válida!")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == 2:
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == 3:
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == 4:
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")

            continuar = input("Deseja realizar outra operação? (s/n): ").lower()
            if continuar != 's':
                print("Encerrando a calculadora. Até mais!")
                break

        except ValueError:
            print("Entrada inválida. Por favor, tente novamente!")

if __name__ == "__main__":
    calculadora()
