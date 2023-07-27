def isvalid_time(time):
    return isinstance(time, int) and 0 <= time < 24


def study_schedule(permanence_period, target_time):
    """Faça o código aqui Lutti."""
    number_of_students = 0

    if isvalid_time(target_time) is False:
        return None

    for student_session in permanence_period:
        if not all((
            isinstance(student_session, tuple),
            isinstance(student_session[0], int),
            isinstance(student_session[1], int)
        )):
            return None
        if student_session[0] <= target_time <= student_session[1]:
            number_of_students += 1

    return number_of_students
