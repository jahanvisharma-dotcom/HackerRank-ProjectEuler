def confirm_dates(start, end):
    dates = [start, end]
    if date_error(start, end):
        new_dates = exchange(start, end)
        dates = [new_dates[0], new_dates[1]]
    return dates


def date_error(start, end):
    if start[0] > end[0]:
        return True
    elif start[0] == end[0]:
        if start[1] > end[1]:
            return True
        elif start[1] == end[1]:
            if start[2] > end[2]:
                return True
    return False


def exchange(start, end):
    dates = [end, start]
    return dates


def is_sunday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    dv = year // 100
    y = year % 100
    d = (y + (y // 4) + (dv // 4) - (2 * dv) + ((26 * (month + 1)) // 10) + day - 1) % 7
    return d == 0


for _ in range(int(input())):
    start_date = list(map(int, input().split()))
    end_date = list(map(int, input().split()))
    dates = confirm_dates(start_date, end_date)
    start_date = dates[0]
    end_date = dates[1]
    
    count = 0
    while True:
        if start_date[2] == 1:
            if is_sunday(start_date[0], start_date[1], start_date[2]):
                count += 1
        
        start_date[2] = 1
        start_date[1] += 1
        if start_date[1] > 12:
            start_date[1] = 1
            start_date[0] += 1
            
        if date_error(start_date, end_date):
            break
    
    print(count)
