def study_schedule(permanence_period, target_time):
    """
    permanence_period é uma lista de tuplas representa o horário de
    entrada e de saída.
    O objetivo é descobrir o horário com mais estudantes presentes de
    acordo com o target_time.
    Caso target_time ou algum valor de permanence_period for inválid, será
    retornado None.
    """
    students = 0

    if not target_time:
        return None

    for enter_time, leave_time in permanence_period:
        if not isinstance(enter_time, int) or not isinstance(leave_time, int):
            return None

        if enter_time <= target_time <= leave_time:
            students = students + 1

    return students
