from sympy import symbols,simplify
from sympy.plotting import plot

def Lagrange (Lx, Ly):
    X=symbols('X')
    if  len(Lx) != len(Ly):
        print ("ERROR")
        return 1
    y=0
    for k in range ( len(Lx) ):
        t=1
        for j in range ( len(Lx) ):
            if j != k:
                t=t* ( (X-Lx[j]) /(Lx[k]-Lx[j]) )
        y+= t*Ly[k]
    return y

def main():
    Lx=[]
    Ly=[]
    n = int(input("Entrer le nombre de point: "))
    i = 0
    while i < n:
        Lx.append(int(input("X{} =".format(i))))
        Ly.append(int(input("Y{} =".format(i))))
        i += 1
    p_x = simplify(Lagrange(Lx,Ly))
    print ("P(X) = {}".format(p_x))
    plot(p_x)

    key = input("q pour quitter, r pour recommencer: ")
    print("========================================")
    if(key == "r"):
        main()

main()
