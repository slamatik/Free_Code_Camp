def add_time(start, duration, day=None):
    answer = ""

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    half = start[-2:]

    current_time = start[:-3]
    current_min = int(current_time[-2:])
    current_hours = int(current_time[:-3])

    to_add_min = int(duration[-2:])
    to_add_hours = int(duration[:-3])
    new_days = 0

    minutes_half = False

    while to_add_min > 0:
        current_min += 1
        to_add_min -= 1
        if current_min >= 60:
            current_hours += 1
            current_min -= 60
        if current_hours == 12 and not minutes_half:
            half = change_half(half)
            minutes_half = True
            if half == "AM":
                new_days += 1
        if current_hours > 12:
            current_hours -= 12

    while to_add_hours > 0:
        current_hours += 1
        to_add_hours -= 1
        if current_hours == 12:
            half = change_half(half)
            if half == "AM":
                new_days += 1
        if current_hours > 12:
            current_hours -= 12

    current_hours = str(current_hours)
    current_min = str(current_min)
    if len(current_min) != 2:
        current_min = "0" + current_min

    answer = current_hours + ":" + current_min + " " + half

    if day:
        day_index = week_days.index(day.lower())
        new_day_index = new_days + day_index
        while new_day_index > 7:
            new_day_index %= 7
        answer += f", {week_days[new_day_index].capitalize()}"

    if new_days == 1:
        answer += " (next day)"

    if new_days > 1:
        answer += f" ({new_days} days later)"

    return answer


def change_half(half):
    if half == "AM":
        return "PM"
    else:
        return "AM"