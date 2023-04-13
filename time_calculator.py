def add_time(start, duration, dotw=None):
  days = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]

  time_split = start.split(" ")
  moment = time_split[1]
  hour = int(time_split.split(":")[0])
  minutes = int(time_split.split(":")[1])

  add_hours = int(duration.split(":")[0])
  add_minutes = int(duration.split(":")[1])

  n_days = 0

  if add_hours > 24:
    n_days = add_hours / 24
    add_hours = add_hours - (24 * n_days)

  hour = hour + add_hours

  sum_minutes = minutes + add_minutes
  if sum_minutes > 60:
    minutes = sum_minutes - 60
    hour += 1

  if hour > 12:
    hour = hour - 12
    if moment == 'AM':
      moment = 'PM'
    elif moment == 'PM':
      moment = 'AM'
      n_days += 1

  new_time = str(hour) + ":" + str(minutes) + " " + moment

  elem = 0
  final_day = None
  if not dotw == None:
    i = 0
    aux_n_days = 0
    if n_days > 7:
      sub = n_days / 7
      aux_n_days = n_days - sub * 7

    while i < len(days):
      if dotw.casefold() == days[i].casefold():
        elem = i
        break
      i += 1

    if aux_n_days > (len(days) - (elem + 1)):
      aux_n_days = aux_n_days - (len(days) - (elem + 1))
      final_day = days[aux_n_days]

  if not final_day == None and n_days > 0:
    new_time += ", " + final_day

  new_time += " ("

  if n_days == 1:
    new_time += "next day)"
  else:
    new_time += str(n_days) + " days later)"

  return new_time