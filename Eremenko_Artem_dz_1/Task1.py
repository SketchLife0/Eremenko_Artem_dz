def convert_time(duration):
    answer = []
    for i in duration:
        day = i // 86400
        days = day * 86400
        hour = (i - days) // 3600
        hours = hour * 3600
        minute = (i - days - hours) // 60
        minuts = minute * 60
        second = i - days - hours - minuts
        if i < 60:
            result = f'{second} сек'
        elif i >=60 and i < 3600:
            result = f'{minute} мин {second} сек'
        elif i >= 3600 and i < 86400:
            result = f'{hour} час {minute} мин {second} сек'
        else:
            result = f'{day} дн {hour} час {minute} мин {second} сек'
        answer.append(result)
    return answer

duration = 60, 8515, 405405
result = convert_time(duration)
print(*result, sep='\n')