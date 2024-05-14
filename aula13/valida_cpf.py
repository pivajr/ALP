def valida_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Verificar o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verificar o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    return True
