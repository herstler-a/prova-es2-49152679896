MAXIMO = 26  # TROQUE pelo seu LIMITE


def desconto_valido(percentual):
    if percentual <= 0:
        return False
    return percentual < MAXIMO
