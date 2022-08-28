import math
start_time = '11:43 PM'
duration = '24:20'
day_of_week = 'Tuesday'
args = [
  ('3:00 PM', '3:10', ""),
  ('11:30 AM', '2:32', "Monday"),
  ('11:43 AM', '0:20', ""),
  ("10:10 PM", '3:30', ""),
  ('11:43 PM', '24:20', 'Tuesday'),
  ('6:30 PM', '205:12', ""),
  ("2:59 AM", "24:00", "saturday"),
  ("11:59 PM", "24:05", 'wednesday'),
  ("8:16 PM", "466:02", "tuesday")
]

def get_hours_and_minutes(time):
  if time[-2:] == 'AM' or time[-2:] == 'PM':
    status = time[-2:]
    h, m = time[:-2].split(":")
    return h, m, status
  h, m = time.split(":")
  return h, m

def get_formated_hs_and_ms_and_status(start_h, hours, minutes, status):
  h = int(hours)
  m = int(minutes)
  
  start_h = int(start_h)
  if status == 'PM':
    h += 12
  if m > 60:
    h += int(m // 60)
    m %= 60

  n_days = math.ceil((h - start_h - 12) / 24)
  
  formated_h_24 = h % 24
  status = 'PM' if formated_h_24 >= 12 else 'AM'
  formated_h_12 = 12 if formated_h_24 % 12 == 0 else formated_h_24 % 12
  next_day = False
  if h >= 24 and h < 48:
    next_day = True
  if m < 10:
    m = "0" + str(m)
  return formated_h_12, m, status, n_days, next_day

def add_time(start_time, duration, day_of_week=''):
  day_of_week = day_of_week.title()
  days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
  
  start_h, start_m, status = get_hours_and_minutes(start_time)
  duration_h, duration_m = get_hours_and_minutes(duration)

  total_h = str(int(start_h) + int(duration_h))
  total_m = str(int(start_m) + int(duration_m))

  result_h, result_m, result_status, n_days, next_day = get_formated_hs_and_ms_and_status(start_h, total_h, total_m, status)

  result = f'{result_h}:{result_m} {result_status}'
  if day_of_week == '':
    if (next_day):
      result += ' (next day)'
    elif n_days > 1:
      result += f' ({n_days} days later)'
  else:
    if next_day:
      indx = days_of_week.index(day_of_week)
      d_of_w = days_of_week[(indx+1)%7]
      result += f', {d_of_w} (next day)'
    elif n_days > 1:
      indx = days_of_week.index(day_of_week)
      d_of_w = days_of_week[(indx+(n_days%7))%7]
      result += f', {d_of_w} ({n_days} days later)'
    else:
      result += ", " + day_of_week
  return result

for i, j, k in args:  
  result = add_time(i, j, k)
  print(result)
# 6:10 PM
# 2:02 PM, Monday
# 12:03 PM
# 1:40 AM (next day)
# 12:03 AM, Thursday (2 days later)
# 7:42 AM (9 days later)
