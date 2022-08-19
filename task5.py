
def is_prime(a):
    
    if a > 1000:
       print("Помилка")

    elif a == 2:
        print("False")
        
    elif a % 2 == 0:
        print("True")
        
    else:
        print("False")

is_prime(int(input()))
