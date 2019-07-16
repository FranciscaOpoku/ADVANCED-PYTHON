number = int(input("enter your number "))

def even_num(number):
    if number%2==0:
        return True
    else:
        return False
print(even_num(number))