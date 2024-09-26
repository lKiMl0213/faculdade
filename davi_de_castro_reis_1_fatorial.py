def fatorial():
    # Solicita ao usuário que digite um número e converte para inteiro
    n = int(input("Digite um número: "))
    # Verifica se o número digitado é negativo e, se sim, informa ao usuário que o número deve ser positivo
    if n < 0:
        print("O número deve ser positivo.")
    else:
        # Inicializa o fatorial com o valor 1
        fatorial = 1
        # Utiliza um loop para calcular o fatorial do número digitado
        for i in range(1, n + 1):
            # Multiplica o fatorial pelo número atual no loop
            fatorial *= i
        # Imprime o resultado do fatorial do número digitado
        print(f"O fatorial de {n} é {fatorial}.")

# Chama a função fatorial para iniciar o cálculo do fatorial
fatorial()
