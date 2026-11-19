from cupom import desconto_valido, MAXIMO


def test_percentual_exatamente_no_limite_e_aceito():
    # Preparar
    percentual = MAXIMO  # 26
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is True


def test_percentual_acima_do_limite_e_rejeitado():
    # Preparar
    percentual = MAXIMO + 1  # 27
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is False


def test_percentual_zero_e_rejeitado():
    # Preparar
    percentual = 0
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is False
