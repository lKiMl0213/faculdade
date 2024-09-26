# Função para converter temperatura de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter temperatura de Celsius para Kelvin
def celsius_para_kelvin(celsius):
    return celsius + 273.15

# Função para converter temperatura de Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para converter temperatura de Fahrenheit para Kelvin
def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Função para converter temperatura de Kelvin para Celsius
def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

# Função para converter temperatura de Kelvin para Fahrenheit
def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Função principal para converter temperatura
def temperatura():
    # Loop para garantir que o usuário digite uma temperatura válida
    while True:
        try:
            temperatura = float(input("Digite a temperatura: "))
            break
        except ValueError:
            print("A temperatura deve ser um número.")
    
    # Loop para garantir que o usuário digite uma unidade válida
    while True:
        unidade = input("Digite a unidade (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
        if unidade in ['C', 'F', 'K']:
            break
        else:
            print("Unidade inválida. Digite C para Celsius, F para Fahrenheit ou K para Kelvin.")
    
    # Converte a temperatura de acordo com a unidade escolhida
    if unidade == 'C':
        print(f"A temperatura em Fahrenheit é {celsius_para_fahrenheit(temperatura)}")
        print(f"A temperatura em Kelvin é {celsius_para_kelvin(temperatura)}")
    elif unidade == 'F':
        print(f"A temperatura em Celsius é {fahrenheit_para_celsius(temperatura)}")
        print(f"A temperatura em Kelvin é {fahrenheit_para_kelvin(temperatura)}")
    elif unidade == 'K':
        print(f"A temperatura em Celsius é {kelvin_para_celsius(temperatura)}")
        print(f"A temperatura em Fahrenheit é {kelvin_para_fahrenheit(temperatura)}")
    else:
        print("Unidade inválida.")

# Chama a função temperatura para iniciar o programa
temperatura()
