continuar = True


while continuar == True:
    nome = input("Digite seu nome: ")
    nota1 = float(input("Informe sua primeira nota: "))
    nota2 = float(input("Informe sua segunda nota: "))
    nota3 = float(input("Informe sua terceira nota: "))

    with open("notas.txt", "a") as arquivo:
        arquivo.write(f'{nome};')
        arquivo.write(f'{nota1};')
        arquivo.write(f'{nota2};')
        arquivo.write(f'{nota3};\n')

    continuidade = str(input("Deseja continuar? (S/N)")).upper()
    if continuidade == "S":
        continuar = True
    else:
        continuar = False


with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

arquivoAprovados = open("aprovados.txt", "w")
arquivoExame = open("exame.txt", "w")
arquivoReprovados = open("reprovados.txt", "w")

for linha in linhas:
    dados = linha.strip().split(";")
    notasMap = list(map(float, dados[1:4]))
    sumNotas = sum(notasMap)
    mediaFinal = round(sumNotas / 3, 2)

    if mediaFinal >= 7:
        situacao = "Aprovado"
        arquivoAprovados.write(f'{dados[0]};{mediaFinal};{situacao};\n')
    elif mediaFinal >= 5:
        situacao = "Exame"
        arquivoExame.write(f'{dados[0]};{mediaFinal};{situacao};\n')
    else:
        situacao = "Reprovado"
        arquivoReprovados.write(f'{dados[0]};{mediaFinal};{situacao};\n')

    print(f'Aluno: ', dados[0])
    print(f'Soma das Notas: ', sumNotas)
    print(f'Média final: ', mediaFinal)
    print(f'Situação: ', situacao)
    print()

arquivoAprovados.close()
arquivoExame.close()
arquivoReprovados.close()


with open("exame.txt", "r") as arquivo:
    linhasExame = arquivo.readlines()

for linha in linhasExame:
    dados = linha.strip().split(";")
    nome = dados[0]
    mediaAnterior = float(dados[1])

    notaExame = float(input(f'Informe a nota do exame de {nome}: '))
    novaMedia = round((mediaAnterior + notaExame) / 2, 2)

    if novaMedia >= 5:
        with open("aprovados.txt", "a") as arquivo:
            arquivo.write(f'{nome};{novaMedia};Aprovado após exame;\n')
    else:
        with open("reprovados.txt", "a") as arquivo:
            arquivo.write(f'{nome};{novaMedia};Reprovado após exame;\n')


print("\n===== APROVADOS =====")
with open("aprovados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        dados = linha.strip().split(";")
        print(f'Aluno: ', dados[0], '| Média: ', dados[1], '| Situação: ', dados[2])

print("\n===== REPROVADOS =====")
with open("reprovados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        dados = linha.strip().split(";")
        print(f'Aluno: ', dados[0], '| Média: ', dados[1], '| Situação: ', dados[2])