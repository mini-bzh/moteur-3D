import math

def rotation_DG(pointCentre,Point, angleR):
    x=math.cos(angleR)*(Point[0]-pointCentre[0])-math.sin(angleR)*(Point[2]-pointCentre[2])
    z=math.sin(angleR)*(Point[0]-pointCentre[0])+math.cos(angleR)*(Point[2]-pointCentre[2])
    return [x+pointCentre[0],Point[1],z+pointCentre[2]]

def rotation_objet_DG(point0, liste_point, angleR):
    for i in range(len(liste_point)):
        liste_point[i] = rotation_DG(point0, liste_point[i], angleR)
    return liste_point

def rotation_Clock(pointCentre,Point, angleR):
    x=math.cos(angleR)*(Point[0]-pointCentre[0])-math.sin(angleR)*(Point[1]-pointCentre[1])
    y=math.sin(angleR)*(Point[0]-pointCentre[0])+math.cos(angleR)*(Point[1]-pointCentre[1])
    return [x+pointCentre[0],y+pointCentre[1],Point[2]]

def rotation_objet_Clock(point0, liste_point, angleR):
    for i in range(len(liste_point)):
        liste_point[i] = rotation_Clock(point0, liste_point[i], angleR)
    return liste_point

def rotation_Top(pointCentre,Point, angleR):
    z=math.cos(angleR)*(Point[2]-pointCentre[2])-math.sin(angleR)*(Point[1]-pointCentre[1])
    y=math.sin(angleR)*(Point[2]-pointCentre[2])+math.cos(angleR)*(Point[1]-pointCentre[1])
    return [Point[0],y+pointCentre[1],z+pointCentre[2]]

def rotation_objet_Top(point0, liste_point, angleR):
    for i in range(len(liste_point)):
        liste_point[i] = rotation_Top(point0, liste_point[i], angleR)
    return liste_point

def rotation(point0, liste_point, angleR):
    return rotation_objet_Top(point0,rotation_objet_Clock(point0, rotation_objet_DG(point0, liste_point, angleR[0]), angleR[1]), angleR[2])

if __name__ == "__main__":
    PointA=[1,1,0]
    Point0=[1,0,0]
    print(rotation_Top(Point0,PointA,(math.pi)))
