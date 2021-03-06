#!/usr/bin/env python

import cmath
import matplotlib.pyplot as plt

def quadratic_solver():
    while True:
            switch1 = int(input("Function=0 Quadratics=1 Main Menu=2 "))
            if switch1 == 0:
                a = float(input("A? "))
                b = float(input("B? "))
                c = float(input("C? "))
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
            
            elif switch1 == 1:
                a = float(input("A? "))
                b = float(input("B? "))
                c = float(input("C? "))
                d = (b**2) - (4*a*c)

                s1 = (-b+cmath.sqrt(d))/(2*a)
                s2 = (-b-cmath.sqrt(d))/(2*a)

                print("The solutions are {0} and {1}".format(s1,s2))
            
            elif switch1 ==2:
                break
            else:
                pass

def DST_solver():
    while True:
        switch2 = int(input("Distance=0 Speed=1 Time=2 Main Menu=3 "))
        if switch2 == 0:
            s0 = float(input("Speed? "))
            t0 = float(input("Time?(Decimal Format) "))
            d0 = s0*t0
            print("Distance is " + str(d0))
        elif switch2 == 1:
            d1 = float(input("Distance? "))
            t1 = float(input("Time?(Decimal Format) "))
            s1 = d1/t1
            print("Speed is " + str(s1))
        elif switch2 == 2:
            d2 = float(input("Distance? "))
            s2 = float(input("Speed? "))
            t2 = d2/s2
            print("Time is " + str(t2))
        elif switch2 == 3:
            break
        else:
            pass


graph = 1
values = 1
while True:

    mode = int(input("What mode? Quadratics=0 Distance/Speed/Time=1 Settings=2 End=3 "))

    if mode == 0:
        quadratic_solver()

    elif mode == 1:
        DST_solver()

    elif mode == 2:
        print("SETTINGS")
        graph = int(input("Show graph? 1 = Yes "))
        values = int(input("Show values? 1 = Yes "))

    elif mode == 3:
        exit()

    else:
        pass
