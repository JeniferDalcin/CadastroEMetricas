nome = sexo = ''
idade = somaidade = 0
cad = {'nome': nome,
       'idade': idade,
       'sexo': sexo}
dados = list()
mulheres = list()
acimaidade = list()
while True:
    cad['nome'] = str(input('Nome: '))
    cad['idade'] = int(input('Idade: '))
    while True:
        cad['sexo'] = str(input('Sexo (F/M): ')).upper().strip()[0]
        if cad['sexo'] in 'MF':
            break
        print('ERRO. Por favor digite M ou F.')
    dados.append(cad.copy())
    somaidade += cad['idade']
    if 'F' in cad['sexo']:
        mulheres.append(cad['nome'])
    while True:
        sair = str(input('Deseja continuar? (S/N) ')).upper().strip().split()[0]
        if sair in 'SN':
            break
        print('ERRO. Por favor digite S ou N.')
    if sair == 'N':
        break
media = somaidade / len(dados)
print(f'A) No total {len(dados)} pessoas foram cadastradas.')
print(f'B) A média de idade das pessoas cadastradas foi: {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print(f'D) Esses foram os cadastrados acima da média de idade encontrados...')
for p in dados:
    if p['idade'] > media:
        print(p['nome'], end='|')
print()
print('>>> ENCERRADO <<<')