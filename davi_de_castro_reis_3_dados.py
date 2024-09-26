def dados():
    # Inicializa listas vazias para armazenar os dados coletados
    sexos = []
    alturas = []
    idades = []
    # Loop para coletar dados de 2 pessoas
    for _ in range(2):
        # Solicita o sexo do usuário e verifica se é válido
        sexo = input("Digite o sexo: 0 para feminino e 1 para masculino: ")
        while sexo not in ['0', '1']:
            print("Sexo inválido. Digite 0 para feminino ou 1 para masculino.")
            sexo = input("Digite o sexo: 0 para feminino e 1 para masculino: ")
        # Solicita a altura do usuário e converte para float
        altura = float(input("Digite a altura em centímetros: "))
        # Solicita a idade do usuário e converte para int
        idade = int(input("Digite a idade: "))
        # Adiciona os dados coletados às respectivas listas
        sexos.append(sexo)
        alturas.append(altura)
        idades.append(idade)
    # Retorna as listas de sexos, alturas e idades
    return sexos, alturas, idades

def media_idade(idade):
    # Calcula a média das idades e arredonda para 2 casas decimais
    return round(sum(idade) / len(idade), 2)

def altura_media_mulheres(altura, sexo):
    # Filtra as alturas das mulheres e calcula a média
    alturas_mulheres = [altura[i] for i in range(len(sexo)) if sexo[i] == '0']
    if alturas_mulheres:
        return round(sum(alturas_mulheres) / len(alturas_mulheres), 2)
    else:
        return 0

def altura_media_homens(altura, sexo):
    # Filtra as alturas dos homens e calcula a média
    alturas_homens = [altura[i] for i in range(len(sexo)) if sexo[i] == '1']
    if alturas_homens:
        return round(sum(alturas_homens) / len(alturas_homens), 2)
    else:
        return 0

def porcentagem_idade_18_35(idade):
    # Filtra as idades entre 18 e 35 e calcula a porcentagem
    pessoas_18_35 = [i for i in idade if 18 <= i <= 35]
    return round((len(pessoas_18_35) / len(idade)) * 100, 2)

# Chama a função dados para coletar os dados
sexos, alturas, idades = dados()
# Imprime as estatísticas calculadas
print(f"A média de idade é {media_idade(idades)}")
print(f"A altura média das mulheres é {altura_media_mulheres(alturas, sexos)} cm")
print(f"A altura média dos homens é {altura_media_homens(alturas, sexos)} cm")
print(f"A porcentagem de pessoas com idade entre 18 e 35 anos é {porcentagem_idade_18_35(idades)}%")