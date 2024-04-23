from datetime import datetime
def check_control_digit(pesel:str):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = 10 - int(str(control_sum)[-1])
    if str(control_digit) == pesel[-1]:
        return True
    return False

def get_pesel_data(pesel):
    month1 = int(pesel[2])
    if month1 > 1:
        birth_date = '20' + pesel[:2] + '.' + str(month1-2) + pesel[3] + '.' + pesel[4:6]
    else:
        birth_date = '19' + pesel[:2] + '.' + str(month1) + pesel[3] + '.' + pesel[4:6]
    if int(pesel[-2]) % 2 == 0:
        gender = 'K'
    else: gender = 'M'

    return pesel, datetime.strptime(birth_date, '%Y.%m.%d').date(), gender