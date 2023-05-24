
def trata_cpf(cpf):
    cpf_valido = ''
    if len(cpf) != 11:
        for c in cpf:
            if (c == '.') or (c == '-') or (c == ' '):
                c = ''
            cpf_valido += c
        return cpf_valido
    else:
        return cpf

def retorna_username(nome):
    nome_minusculo = nome.lower()
    nomes_divididos = nome_minusculo.split()
    if len(nomes_divididos) > 1:
        username = nomes_divididos[0] + '.' + nomes_divididos[-1]
        return username
    else:
        return nome_minusculo