from random import randint

# Pense em um número que o computador ira adivinhar


def computador_adivinha(x):
    global advinha
    minimo = 1
    maximo = x
    retorno = ''
    while retorno != 'c':
        if minimo != maximo:
            advinha = randint(minimo, maximo)
        else:
            advinha = minimo
        retorno = str(input(f"""
        Computador escolheu: {advinha}
        Muito grande (>)
        Muito pequeno (<)
        Caso estiver correto digite (c)
        """)).lower().strip()
        if retorno == '>':
            maximo = advinha - 1
        elif retorno == '<':
            minimo = advinha + 1

    print(f"Parabens computador! o numero que eu pensei era  {advinha}")


computador_adivinha(1000)