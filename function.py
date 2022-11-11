# def print_seconds(hours, minutes, seconds):
#     print(hours*3600, minutes*60, seconds*1)
# print_seconds(1,2,3)

# def area_triangle(base, height):
#     return  (base*height)/2
# area_1=area_triangle(6,7)
# area_2=area_triangle(2,8)
# print(int(area_1 + area_2))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds

# hours, minutes, seconds = convert_seconds(5000)
# print(hours, minutes, seconds)
print(convert_seconds(5000))

# def month_days(month, days):
#     print (month + " has " + str(days) + " days.")
# month_days("june", 30)
# month_days("july", 31)

def is_positive(number):
  if number > 0:
    return (bool(number))
print(is_positive(13))

print("big" > "small")