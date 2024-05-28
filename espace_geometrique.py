from math import *
import Fonction_rotation as r
import INTERSECTION as inter



class segment:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def distance(self,):
        return sqrt((self.A[0]-self.B[0])**2+(self.A[1]-self.B[1])**2)    
        
    def distance_3D(self):
        return sqrt((self.A[0]-self.B[0])**2+(self.A[1]-self.B[1])**2+(self.A[2]-self.B[2])**2)

    def Vecteur(self,n):
        return self.B[n]-self.A[n]

    def Solution_ligne(self,t):
        return (self.A[0]+t*self.Vecteur(0),self.A[1]+t*self.Vecteur(1),self.A[2]+t*self.Vecteur(2))

    def point_ligne(self,c):
        result = list()
        for i in range(round(self.distance_3D())):
            result.append(self.Solution_ligne(i/(self.distance_3D())))
            result[-1] = (round(result[-1][0]),round(result[-1][1]),round(result[-1][2]),c)
        result.append(tuple(list(self.B)+[c]))
        result.append(tuple(list(self.A)+[c]))
        return result
    
    def equation_droite(self,coords):
        """
        x(P) * y(Vd) + y(P) * -x(Vd) + k = 0
        """
        k = -(self.A[0]*self.Vecteur(1)+self.A[1]*(-self.Vecteur(0)))
        return coords[0]*self.Vecteur(1)+coords[1]*(-self.Vecteur(0))+k
    



class polygone:
    def __init__(self,liste_point):
        self.liste_point = list(liste_point)
        self.n_point = len(liste_point)
        
    def produit_vectoriel(self):
        v1 = segment(self.liste_point[0],self.liste_point[1])
        v2 = segment(self.liste_point[0],self.liste_point[2])
        return (v1.Vecteur(1)*v2.Vecteur(2)-v1.Vecteur(2)*v2.Vecteur(1),v1.Vecteur(2)*v2.Vecteur(0)-v1.Vecteur(0)*v2.Vecteur(2),v1.Vecteur(0)*v2.Vecteur(1)-v1.Vecteur(1)*v2.Vecteur(0))
        
    def point_polygone(self,c):
        result = list()
        for i in range(-1,self.n_point-1,1):
            result += segment(self.liste_point[i],self.liste_point[i+1]).point_ligne(c)
        return result
    
    def point_carre(self,c):
        """
        eq plan de la forme : x(P) * x(Vn) + y(P) * y(Vn) + z(P) * z(Vn) + p = 0
        """
        if self.n_point != 4:
            return None
        
        result = list()
        deb = (int(min([self.liste_point[i][0]for i in range (4)])),int(min([self.liste_point[i][1]for i in range (4)])))
        fin = (round(max([self.liste_point[i][0]for i in range (4)])),round(max([self.liste_point[i][1]for i in range (4)])))
        V_normal = self.produit_vectoriel()
        p = -(V_normal[0]*self.liste_point[0][0]+V_normal[1]*self.liste_point[0][1]+V_normal[2]*self.liste_point[0][2])
        dis = 0
        
        
        for y in range(deb[1],fin[1]):
            for x in range (deb[0],fin[0]):
                if segment(self.liste_point[0],self.liste_point[1]).equation_droite((x,y))>dis and segment(self.liste_point[1],self.liste_point[2]).equation_droite((x,y))>dis:
                    if segment(self.liste_point[2],self.liste_point[3]).equation_droite((x,y))>dis and segment(self.liste_point[3],self.liste_point[0]).equation_droite((x,y))>dis:
                        z = (-(V_normal[0]*x+V_normal[1]*y+p))/V_normal[2]
                        result.append((x,y,z,c))
        return result



class cube:
    def __init__(self,point_centre, taille_cote,angle_R, FOV):
        taille_cote /= 2
        liste_point = [point_centre for _ in range(8)]
        liste_point[0] = (liste_point[0][0]-taille_cote,liste_point[0][1]-taille_cote,liste_point[0][2]+taille_cote)
        liste_point[1] = (liste_point[1][0]-taille_cote,liste_point[1][1]-taille_cote,liste_point[1][2]-taille_cote)
        liste_point[2] = (liste_point[2][0]+taille_cote,liste_point[2][1]-taille_cote,liste_point[2][2]-taille_cote)
        liste_point[3] = (liste_point[3][0]+taille_cote,liste_point[3][1]-taille_cote,liste_point[3][2]+taille_cote)
        liste_point[4] = (liste_point[4][0]-taille_cote,liste_point[4][1]+taille_cote,liste_point[4][2]+taille_cote)
        liste_point[5] = (liste_point[5][0]-taille_cote,liste_point[5][1]+taille_cote,liste_point[5][2]-taille_cote)
        liste_point[6] = (liste_point[6][0]+taille_cote,liste_point[6][1]+taille_cote,liste_point[6][2]-taille_cote)
        liste_point[7] = (liste_point[7][0]+taille_cote,liste_point[7][1]+taille_cote,liste_point[7][2]+taille_cote)
        
        
        liste_point = r.rotation((FOV[0],FOV[1],0),liste_point,angle_R)
        
        self.liste_point = [inter.Intersection(i,FOV) for i in liste_point]

    
    def point_cube(self,c):
        result = list()
        
        if max([i[2] for i in self.liste_point])<0:
            return result
        
        for i in [(0,1,2,3),(5,4,0,1),(6,5,1,2),(7,6,2,3),(4,7,3,0),(4,7,6,5)]:
            result += polygone((self.liste_point[i[0]],self.liste_point[i[1]],self.liste_point[i[2]],self.liste_point[i[3]])).point_polygone(c)
        return result
    
    def point_cote(self,c):
        result = list()

        if max([i[2] for i in self.liste_point])<0:
            return result
        
        cote = [(0,1,2,3),(4,5,1,0),(5,6,2,1),(6,7,3,2),(7,4,0,3),(4,7,6,5)]
        for j in range(len(cote)):
            i = cote[j]
            result += polygone((self.liste_point[i[0]],self.liste_point[i[1]],self.liste_point[i[2]],self.liste_point[i[3]])).point_carre(c[j])
        return result

    




if __name__ == "__main__":
    A = (1,1,5)
    B = (6,9,7)
    C = (8,5,10)
    D = (5,32,4)
    print(segment(A,C).Vecteur(2))
    print(polygone((A,B,C,D)).produit_vectoriel())

#     print(s.point_ligne())
#     print(p.point_polygone())
#     print(p.point_polygone())

    



