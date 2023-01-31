def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    if permanence_period is None:
        return None
    contador = {}
    for entrada, saida in permanence_period:
        if entrada <= target_time <= saida:
            if target_time in contador:
                contador[target_time] += 1
            else:
                contador[target_time] = 1
    return max(contador, key=contador.get)
# raise NotImplementedError
