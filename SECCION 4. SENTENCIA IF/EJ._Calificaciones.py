
calificaion = float(input("Ingrese la calificacion del alumno (0-10): "))

if calificaion > 9 and calificaion == 10:
    print("La calificacion es A")
else:
    if calificaion > 8 and calificaion <=9:
        print("La calificacion es B")
    else:
        if calificaion > 7 and calificaion <=8:
            print("La calificacion es C")
        else:
            if calificaion > 6 and calificaion <= 7:
                print("La calificacion es D ")
            else:
                if calificaion >= 0 and calificaion <= 6:
                    print("La calificacion es F")
