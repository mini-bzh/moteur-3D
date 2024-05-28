def vecteur(A,B):
    Vect=[None,None,None]
    Vect[0]=B[0]-A[0]
    Vect[1]=B[1]-A[1]
    Vect[2]=B[2]-A[2]
    return Vect

def Intersection(P1,P2):
    PI=[None,None,P1[2]]
    Vect=vecteur(P1,P2)
    if Vect[2] == 0:
        PI = P1
        return PI
    t=(-P1[2]/Vect[2])
    PI[0]=P1[0]+t*Vect[0]
    PI[1]=P1[1]+t*Vect[1]
    return PI
    
if __name__=='__main__':
    A=[1,1,10]
    F=[1,1,-10]
    print(Intersection(A,F))
    A=Intersection(A,F)

