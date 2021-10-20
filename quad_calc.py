import cmath
import matplotlib.pyplot as plt

def quadratic_solver():
    a = float(input("A? "))
    b = float(input("B? "))
    c = float(input("C? "))
    while True:
            switch = int(input("Function=0 Quadratics=1 Main Menu=2 "))
            if switch == 0:
                x = []
                y = []
                #l = lowest number
                l = float(input("Lowest Number? "))
                #h = highest number
                h = float(input("Highest Number? "))
                while True:
                    m = a*(l*l) + b*l + c
                    x.append(l)
                    y.append(m)
                    if values == 1:
                        print("{0} , {1}".format(l,m))
                    else:
                        pass
                    if l == h:
                        if graph == 1:
                            plt.plot(x, y)
                            plt.show()
                            break
                        else:
                            break
                    else:
                        pass
                    l = l + 1
            
            elif switch == 1:
                a = float(input("A? "))
                b = float(input("B? "))
                c = float(input("C? "))
                d = (b**2) - (4*a*c)

                s1 = (-b+cmath.sqrt(d))/(2*a)
                s2 = (-b-cmath.sqrt(d))/(2*a)

                print("The solutions are {0} and {1}".format(s1,s2))
            
            elif switch ==2:
                break
            else:
                pass


graph = 1
values = 1
while True:

    mode = int(input("What mode? Quadratics=0 Settings=1 End=2 "))

    if mode == 0:
        quadratic_solver()

    if mode == 1:
        print("SETTINGS")
        graph = int(input("Show graph? 1 = Yes "))
        values = int(input("Show values? 1 = Yes "))
    elif mode == 2:
        exit()

    else:
        pass
