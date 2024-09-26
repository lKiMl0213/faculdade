def juros():
    # Solicita ao usuário que digite o valor inicial da aplicação e converte para float
    valor_presente = float(input("Digite o valor inicial da aplicação: "))
    # Solicita ao usuário que digite a taxa de juros por mês em porcentagem, substitui vírgula por ponto e converte para float
    taxa_juros = float(input("Digite a taxa de juros por mês em porcentagem: ").replace(',', '.'))
    # Solicita ao usuário que digite o período em meses e converte para int
    periodo = int(input("Digite o período em meses: "))
    # Calcula o valor futuro da aplicação utilizando a fórmula de juros compostos
    valor_futuro = valor_presente * (1 + taxa_juros/100) ** periodo
    # Imprime o valor futuro da aplicação, arredondado para 2 casas decimais
    print(f"O valor futuro da aplicação é {round(valor_futuro, 2)}")

# Chama a função juros para iniciar o cálculo dos juros
juros()