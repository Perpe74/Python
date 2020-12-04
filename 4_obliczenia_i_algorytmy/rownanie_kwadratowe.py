import math

def funkcja_kwadratowa(a, b, c):
    delta = b*b - 4*a*c
    if (delta == 0):
        x0 = -b/(2*a)
        print("rownanie ma jedno rozwiazanie: ", x0)
    elif (delta > 0):
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("rownanie ma dwa rozwiazania: ", x1, ", ", x2)
    else:
        print("równanie nie ma rozwiązania w zbiorze liczb rzeczywistych")

funkcja_kwadratowa(2,3,1)