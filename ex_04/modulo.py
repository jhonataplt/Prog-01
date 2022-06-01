def aposentadoriaHomem(idade, contribuicao):
    soma = idade + contribuicao;
    if idade >= 65 and contribuicao >= 15 and soma >= 95:
        resultado = 'Pode aposentar.';
    else: resultado = 'Não pode aposentar.'
    return resultado;

def aposentadoriaMulher(idade, contribuicao):
    soma = idade + contribuicao;
    if idade >= 60 and contribuicao >= 15 and soma >= 85:
        resultado = 'Pode aposentar.';
    else: resultado = 'Não pode aposentar.'
    return resultado;
