#include <iostream>
#include <cmath>
#include <vector>

void quadratic_solver() {
while (true) {
    int qtype = 0;
    std::cout << "Function=0 Quadratics=1 Main Menu=2 ";
    std::cin >> qtype;

    if (qtype == 0) {

        double bx;
        double cx;
        double ax;
        std::cout << "\n";
        std::cout << "A? ";
        std::cin >> ax;
        std::cout << " \n";
        std::cout << "B? ";
        std::cin >> bx;
        std::cout << " \n";
        std::cout << "C? ";
        std::cin >> cx;
        std::cout << " \n";

        int lx;
        int hx;
        int l;
        int h;
        int count;
        std::cout << "Lowest Number? ";
        std::cin >> lx;
        std::cout << " \n";
        std::cout << "Highest Number? ";
        std::cin >> hx;
        std::cout << " \n";

        if (hx > lx) {
            h = hx;
            l = lx;
        }

        else if (lx > hx) {
            h = lx;
            l = hx;
        }

        else {
            h = hx;
            l = lx;
        }

        while (l != h+1) {
            double m;
            m = ax * (l*l) + bx*l + cx;
            std::cout << l << " , " << m << "\n";
            l++;
        }
    }

    else if (qtype == 1) {

        double bx;
        double cx;
        double ax;
        double d;
        double s1;
        double s2;
        double b;
        double a;

        std::cout << "A? ";
        std::cin >> ax;
        std::cout << " \n";
        std::cout << "B? ";
        std::cin >> bx;
        std::cout << " \n";
        std::cout << "C? ";
        std::cin >> cx;
        std::cout << " \n";

        b = (bx * bx);
        d = (b) - (4*ax*cx);
        a = 2 * ax;

        s1 = (-bx + sqrt(d)) / a;
        s2 = (-bx - sqrt(d)) / a; 

        std::cout << "The solutions are " << s1 << " and " << s2 << "\n";
    }

    else if (qtype == 2) {
        break;
    }

    else {}
}
}

void DST_solver() {
    while (true) {

        int stype;
        std::cout << "Distance=0 Speed=1 Time=2 Main Menu=3 ";
        std::cin >> stype;

        if (stype == 0) {
            double s0;
            double t0;
            double d0;
            std::cout << "\n";
            std::cout << "Speed? ";
            std::cin >> s0;
            std::cout << "Time? ";
            std::cin >> t0;
            d0 = s0*t0;
            std::cout << "Distance is " << d0 << "\n";
            std::cout << "\n";
        }

        else if (stype == 1) {
            double s1;
            double t1;
            double d1;
            std::cout << "\n";
            std::cout << "Distance? ";
            std::cin >> d1;
            std::cout << "Time? ";
            std::cin >> t1;
            s1 = d1/t1;
            std::cout << "Speed is " << s1 << "\n";
            std::cout << "\n";

        }

        else if (stype == 2) {
            double s2;
            double t2;
            double d2;
            std::cout << "\n";
            std::cout << "Speed? ";
            std::cin >> s2;
            std::cout << "Distance? ";
            std::cin >> d2;
            t2 = d2/s2;
            std::cout << "Time is " << t2 << "\n";
            std::cout << "\n";
        }

        else if (stype == 3) {
            break;
        }

        else{}

    }
}


int main() {

   while (true) {
        int mode;
        std::cout << "\n";
        std::cout << "What mode? Quadratics=0 Distance/Speed/Time=1 Exit=2 ";
        std::cin >> mode;

        if (mode == 0) {
            quadratic_solver();
        }

        else if (mode == 1) {
           DST_solver();
        }

        else if (mode == 2) {
            break;
        }

        else {}
   }
}
