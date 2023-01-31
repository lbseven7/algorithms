def study_schedule(permanence_period, target_time):
    """Ajuda do Arlisson"""
    if not target_time or target_time < 0:
        return None
    contador = 0
    for entrada, saida in permanence_period:
        if not isinstance(entrada, int) or not isinstance(saida, int):
            return None
        if entrada <= target_time <= saida:
            contador += 1
    return contador
