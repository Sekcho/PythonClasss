#calculate score
mid_term = int(input('กรุณาใส่คะแนน mid_term:'))
final_term = int(input('กรุณาใส่คะแนน fianla_term:'))
homework = int(input('กรุณาใส่คะแนน homework:'))    
def calculate_total_score(mid_term, final_term, homework):
    score = (mid_term*0.4) + (final_term*0.5) + (homework*0.1)
    return score
    
    
total_score = calculate_total_score(mid_term, final_term, homework)
print('คุณได้คะแนนรวม: {} '.format(total_score))

#Calculate grade
def Calculate_grade(total_score):
    if total_score >=80:
        return 'A'
    elif total_score >=70:
        return 'B'
    elif total_score >=60:
        return 'C'
    elif total_score >=50:
        return 'D'
    else:
        return 'E'

grade = Calculate_grade(total_score)

def greeting(grade):
    if grade == 'A':
        return 'Exellent'
    elif grade == 'B':
        return 'Great'
    elif grade == 'C':
        return 'Good'
    elif grade == 'D':
        return 'partial good'
    else:
        return 'Caution'
announce = greeting(grade)
print('คุณได้เกรด: {} ขอพูดว่า {}'.format(grade,announce))

