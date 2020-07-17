def add_time(start, duration,startDay=''):
    time, period = start.split()
    hour, minutes = map(int, time.split(":"))
    if period == 'PM':
        hour = hour + 12

    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    newDay = ''
    hourAdded, minutesAdded = map(int, duration.split(":"))

    finalminutes = minutes + minutesAdded
    hourAdded = hourAdded + (finalminutes // 60)
    finalminutes = finalminutes % 60


    finalHour = hour + hourAdded

    days = finalHour // 24
    finalHour = finalHour % 24

    if finalHour < 12:
        period = 'AM'

    else:
        period = 'PM'
        if finalHour > 12:
            finalHour = finalHour - 12


    if finalHour == 0:
        finalHour = 12

    msg = ''

    if days != 0:
        if days == 1:
            msg = ' (next day)'
        else:
            msg = ' (' + str(days) + ' days later)'

    if startDay != '':
        currentDay = startDay.title()
        newDay = ', ' + daysOfWeek[(daysOfWeek.index(currentDay) + days) % 7]


    return str(finalHour) + ':' + str(finalminutes).rjust(2,'0') + ' ' + period + newDay + msg