# Função para coletar e converter 10 números inteiros digitados pelo usuário em uma lista de inteiros
def inteiros():
    # Solicita ao usuário que digite 10 números inteiros separados por vírgula
    entrada_usuario = input("Digite 10 números inteiros separados por vírgula: ")
    # Divide a entrada do usuário em uma lista de strings, separando por vírgula
    inteiros_str = entrada_usuario.split(",")
    # Converte cada string na lista para um inteiro e armazena em uma nova lista
    inteiros = [int(i) for i in inteiros_str]
    return inteiros

# Função para encontrar o maior número em uma lista de inteiros
def maior(inteiros):
    # Retorna o maior número na lista de inteiros
    return max(inteiros)

# Função para encontrar o menor número em uma lista de inteiros
def menor(inteiros):
    # Retorna o menor número na lista de inteiros
    return min(inteiros)

# Função para calcular a média de uma lista de inteiros
def media(inteiros):
    # Calcula a média dos números na lista de inteiros e arredonda para 2 casas decimais
    return round(sum(inteiros) / len(inteiros), 2)

# Chama a função inteiros para coletar e converter os números digitados pelo usuário
inteiros = inteiros()
# Imprime o resultado, incluindo a quantidade de números, o maior, o menor e a média
print(f"Você digitou {len(inteiros)} números. O maior número é {maior(inteiros)}, o menor número é {menor(inteiros)} e a média é {media(inteiros)}")