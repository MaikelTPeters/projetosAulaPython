# Programa para verificar se CPF é valido

# Coleta CPF do usuario
cpf_usuario = input("Digite seu CPF: ")

# Tira caracteres '.' e '-' do CPF
lista_numeros_cpf = cpf_usuario.split('-')
try:
    numeros_cpf = lista_numeros_cpf[0].split('.')
    numeros_cpf.append(lista_numeros_cpf[1])
    cpf = ''.join(numeros_cpf)
except:
    try:
        numeros_cpf = cpf_usuario.split('.')
        cpf = ''.join(numeros_cpf)
    except:
        cpf = cpf_usuario

# Verifica se o usuario informou a quantidade correta de numeros
if len(cpf) == 11:
    # Pega os 9 primeiros numeros do CPF
    numeros_cpf = cpf[:9]

    # Define variaveis para auxiliar nos calculos
    calculo = 0
    count = 10

    # Realiza calculos para verificar primeiro digito
    for i in range(len(numeros_cpf)):
        calculo += int(numeros_cpf[i]) * count
        count = count - 1
    calculo = calculo * 10
    calculo = calculo % 11

    # Verifica se o calculo deu mais de 9
    if calculo > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = calculo

    # Pega os 10 primeiros numeros do CPF
    numeros_cpf = cpf[:10]

    # Altera variaveis para auxiliar nos calculos
    calculo = 0
    count = 11

    # Realiza calculos para verificar segundo digito
    for i in range(len(numeros_cpf)):
        calculo += int(numeros_cpf[i]) * count
        count = count - 1
    calculo = calculo * 10
    calculo = calculo % 11

    # Verifica se o calculo deu mais de 9
    if calculo > 9:
        segundo_digito = 0
    else:
        segundo_digito = calculo

    # Formata o CPF
    cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

    # Verifica se o CPF é valido
    if str(primeiro_digito) == cpf[9] and str(segundo_digito) == cpf[10]:
        print(f'O CPF: {cpf_formatado} é valido.')
    else:
        print(f'O CPF: {cpf_usuario} é invalido.')
else:
    print('O CPF deve ter 11 digitos.')
