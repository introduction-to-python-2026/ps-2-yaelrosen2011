def find_max_number(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    elif num3>num2 and num3>num1:
        return num3

def find_mean(num1, num2, num3):
  avarage=(num1+num2+num3)/3
  return avarage

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    mean_num1=(num1-mean)**2
    mean_num2=(num2-mean)**2
    mean_num3=(num3-mean)**2
    std=(mean_num1+mean_num2+mean_num3)/3
    return std

