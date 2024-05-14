def valida_data(data_nascimento):
    # Verificar o formato da data
    if len(data_nascimento) != 10 or data_nascimento[2] != '/' or data_nascimento[5] != '/':
        return False

    # Extrair dia, mês e ano
    dia_str, mes_str, ano_str = data_nascimento.split('/')
    dia, mes, ano = int(dia_str), int(mes_str), int(ano_str)

    # Verificar se o dia, mês e ano estão dentro dos limites válidos
    if not (1 <= dia <= 31) or not (1 <= mes <= 12) or not (1900 <= ano <= 9999):
        return False

    # Verificar a idade mínima de 18 anos
    from datetime import datetime
    hoje = datetime.now().date()
    data_nasc = datetime(ano, mes, dia).date()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

    return idade >= 18
