

from random import *

def théme():
    """

    permet à l'utilisateur de choisir son théme entre le 2048 'normal', 2048 en chiffre romain, l'alphabéte et la chimie

    """
    return input("Ton théme?, N(2048), R(2048 en chiffre romain), A(alphabéte), C(chimie)")

Théme={"N":"2048 CLASSIQUE","R": "2048 EN CHIFFRE ROMAIN","A":"ALPHABETE" ,"C": "CHIMIE"}

def select_théme():


def grid_init():
    """
    La fonction ne prend pas de paramétre
    Fait une liste(grille) de 4 colonnes et 4 lignes.

    CU: grille carrée de 4 lignes
    """
    L=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
    for i in range(2):
        a=randrange(2,5,2)
        b=randrange(0,4,1)
        c=randrange(0,4,1)
        if L[b][c]==0:
            L[b][c]=str(a)
    return L



def grid_print(grid):
    """
    Prend en paramétre une grille de 4 lignes et 4 colonnes et l'affiche

    CU: grid est une liste de 4 listes de 4 entiers, len(grid)==4,
    len(grid[1])==4, len(grid[1][1])==1

    Exemple:
    >>> l=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 4]]
    >>> grid_print(l)
    ---------------------
    |    |    |    |    |
    ---------------------
    |    |    |    |    |
    ---------------------
    |    |    |    |    |
    ---------------------
    |    |2   |    |4   |
    ---------------------

    """
    a='-'*21
    b='|'
    c='|'
    for e in grid:
        for i in e:
            if i==0:
                c+='    '+b
            elif len(str(i))==1:
                c+=str(i)+' '*3+b
            elif len(str(i))==2:
                c+=str(i)+' '*2+b
            elif len(str(i))==3:
                c+=str(i)+' '+b
            else:
                c+=str(i)+b
        c+='\n' +a+'\n'+b
    c=a+'\n'+ c[:len(c)-1]
    print(c)


def is_grid_over(grid):
    """
    Fonction qui renvoie True si la grille est remplis

    CU: grid est une liste de 4 listes de 4 entiers, len(grid)==4,
    len(grid[1])==4, len(grid[1][1])==1

    Exemples:
    >>> is_grid_over([[0, 0, 0, 0], [0, 0, 4, 0], [0, 0, 0, 0], [0, 0, 2, 0]])
    False

    """
    for e in range (len(grid)-1):
        for i in range(len(grid)-1):
            if not(grid[e][i]==0 in grid):
                if grid[e][i]!=grid[e][i+1] and grid[e][i]!=grid[e+1][i]:
                        return False

def grid_get_max_value(grid):
    """
    Une fonction que renvoie la valeur maximale de la grille

    CU: aucune

    Exemple
    >>> grid=[[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    >>> grid_get_max_value(grid)
    4
    """
    l=[]
    for e in grid:
       for i in e:
           if i!=0:
               l+=str(i)
    l.sort()
    return int(l[len(l)-1])




def trouver_cases_vides(grid):
    """
    Fonction que trouve les cases vides dans la grille

    CU: la len(grid)==4, grid doit être une liste de 4 liste contenant 4 entiers

    Exemple:
    >>> grid= [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    >>> trouver_cases_vides(grid)
    [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    """
    liste=[]
    for e in range(4):
        for i in range(4):
            if grid[e][i]==0:
                liste+=[(e,i)]
    return liste


print(trouver_cases_vides([[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]))

def grid_add_new_tile(grid):
    """
    Fonction qu'additione des nouveux elements à la grille

    CU: grille carrée de 4 lignes
    """
    if not(is_grid_over):
        a=randrange(2,5,2)
        b=randrange(0,4,1)
        c=randrange(0,4,1)
        e=0
        while e!=1:
            if (b,c) in trouver_cases_vides(grid):
                grid[b][c]=str(a)
                e=1
    else:
        return grid
    return grid



DIRECTIONS = { "right" : (1,0), "left" : (-1,0), "up" : (0,-1), "down" : (0,1) }

def grid_get_next(grid,i,j,d):
    """
   Qui renvoie la cellule adjacente à la cellule de coordonnées (i,j)
   dans la grille grid dans la direction d si elle existe ou None sinon

    CU: i et j doivent être compris entre 0 et 3 inclus,
    et d ne peut être que up, down, right et left en chaine de caracteres

    Exemple:
    >>> grid = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
    >>> grid_get_next(grid,1,0,'up')
    2
    >>> grid_get_next(grid,2,0,'down')
    4
    """

    sum1 = 0

    if(d == "up"):
        sum1 = i-1
        if(sum1<0):
            return grid[i][j]
        else:
            return grid[sum1][j]
    else if(d == "down"):
        sum1 = i+1
        if(sum1>len(grid)-1):
            return grid[i][j]
        else:
            return grid[sum1][j]
    else if(d == "right"):
        sum1 = j+1
        if(sum1>len(grid)-1):
            return grid[i][j]
        else:
            return grid[i][sum1]
    else if(d == "left"):
        sum1 = j-1
        if(sum1<0):
            return grid[i][j]
        else:
            return grid[i][sum1]



##    if 0<i<3 and 0<j<3:
##        return grid[i+ DIRECTIONS[d][1]][i+ DIRECTIONS[d]][0]
##    if d == 'up' and j==0:
##        return None
##    if d == 'left' and i==0:
##        return None
##    if d == 'down' and j==3:
##        return None
##    if d == 'right' and i==3:
##        return None
##
##
##grid = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
##print(grid_get_next(grid,2,0,'down'))




def tiles_up(grid):
    """
    Envoie vers l'haut toutes les elements de la grille

    CU: grille carrée de 4 lignes

    Exemple:
    >>> grid=[[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    >>> tiles_up(grid)
    [[4, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    i=0
    for j in range(4):
        if grid[i][j]==0 and ( grid[i+1][j]!=0  or grid[i+2][j]!=0  or grid[i+3][j]!=0):
            if grid[i][j]==0:
                while grid[i][j]==0:
                    grid[i][j]=grid[i+1][j]
                    grid[i+1][j]=grid[i+2][j]
                    grid[i+2][j]=grid[i+3][j]
                    grid[i+3][j]=0

        if  grid[i+1][j]==0  and (grid[i+2][j]!=0 or grid[i+3][j]!=0):
             while grid[i+1][j]==0:
                grid[i+1][j]=grid[i+2][j]
                grid[i+2][j]=grid[i+3][j]
                grid[i+3][j]=0

        if grid[i+2][j] ==0 and grid[i+3][j]!=0:
            grid[i+2][j]=grid[i+3][j]
            grid[i+3][j]=0
    return grid

def tiles_down(grid):
    """
    Envoie vers le bas toutes les elements de la grille

    CU: grille carrée de 4 lignes

    Exemple:
    >>> grid=[[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    >>> tiles_down(grid)
    [[0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]]
    """
    i=3
    for j in range(4):
        if grid[i][j]==0 and ( grid[i-1][j]!=0  or grid[i-2][j]!=0  or grid[i-3][j]!=0):
            if grid[i][j]==0:
                while grid[i][j]==0:
                    grid[i][j]=grid[i-1][j]
                    grid[i+1][j]=grid[i-2][j]
                    grid[i+2][j]=grid[i-3][j]
                    grid[i+3][j]=0

        if  grid[i-1][j]==0  and (grid[i-2][j]!=0 or grid[i-3][j]!=0):
             while grid[i-1][j]==0:
                grid[i-1][j]=grid[i-2][j]
                grid[i-2][j]=grid[i-3][j]
                grid[i-3][j]=0
        if grid[i-2][j] ==0 and grid[i-3][j]!=0:
            grid[i-2][j]=grid[i-3][j]
            grid[i-3][j]=0
    return grid

def tiles_right(grid):
    """
    Envoie vers le bas toutes les elements de la grille.

    CU: grille carrée de 4 lignes

    Exemple:
    >>> grid=[[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    >>> tiles_right(grid)
    [[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]
    """
    i=3
    for j in range(4):
        if grid[j][i]==0 and ( grid[j][i-1]!=0  or grid[j][i-2]!=0  or grid[j][i-3]!=0):
            if grid[j][i]==0:
                while grid[j][i]==0:
                    grid[j][i]=grid[j][i-1]
                    grid[j][i-1]=grid[j][i-2]
                    grid[j][i-2]=grid[j][i-3]
                    grid[j][i-3]=0

        if  grid[j][i-1]==0  and (grid[j][i-2]!=0 or grid[j][i-3]!=0):
             while grid[j][i-1]==0:
                grid[j][i-1]=grid[j][i-2]
                grid[j][i-2]=grid[j][i-3]
                grid[j][i-3]=0

        if grid[j][i-2] ==0 and grid[j][i-3]!=0:
            grid[j][i-2]=grid[j][i-3]
            grid[j][i-3]=0
    return grid

def tiles_left(grid):
    """
    Envoie vers le bas toutes les elements de la grille

    CU: grille carrée de 4 lignes

    Exemple:
    >>> grid=[[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    >>> tiles_left(grid)
    [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    """
    i=0
    for j in range(4):
        if grid[j][i]==0 and ( grid[j][i+1]!=0  or grid[j][i+2]!=0  or grid[j][i+3]!=0):
            if grid[j][i]==0:
                while grid[j][i]==0:
                    grid[j][i]=grid[j][i+1]
                    grid[j][i+1]=grid[j][i+2]
                    grid[j][i+2]=grid[j][i+3]
                    grid[j][i+3]=0

        if  grid[j][i+1]==0  and (grid[j][i+2]!=0 or grid[j][i+3]!=0):
             while grid[j][i+1]==0:
                grid[j][i+1]=grid[j][i+2]
                grid[j][i+2]=grid[j][i+3]
                grid[j][i+3]=0
        if grid[j][i+2] ==0 and grid[j][i+3]!=0:
            grid[j][i+2]=grid[j][i+3]
            grid[j][i+3]=0
    return grid





def fusion_up(grid):
    """
    Ajoute deux element egaux lorsque le mouvement est vers l'haut

    CU: grille carrée de 4 lignes

    Exemples:
    >>> grid=[[4, 2, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [4, 0, 0, 0]]
    >>> l=tiles_up(grid)
    >>> fusion_up(l)
    [[8, 4, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    i=0
    for j in range (4):
        if grid[i][j]==grid[i+1][j]:
            grid[i][j]+=grid[i+1][j]
            if grid[i+2][j]==grid[i+3][j]:
                grid[i+1][j]=2*grid[i+2][j]
                grid[i+2][j]=0
                grid[i+3][j]=0
            grid[i+1][j]=grid[i+2][j]
            grid[i+2][j]=grid[i+3][j]
            grid[i+3][j]=0

        if grid[i+1][j]==grid[i+2][j]:
            grid[i+1][j]+=grid[i+2][j]
            grid[i+2][j]=grid[i+3][j]
            grid[i+3][j]=0

        if grid[i+2][j]==grid[i+3][j]:
            grid[i+2][j]=grid[i+3][j]
            grid[i+3][j]=0

    return grid


def grid_move(grid, d):
    """
    Bouge les elements de la grille en fonction du move choisi

    CU: grille carrée de 4 cases

    Exemple:
    >>>
    >
    """
    if d=='up':
        return fusion_up(tiles_up(grid))
    if d=='down':
        return fusion_down(tiles_down(grid))
    if d==' right':
        return fusion_right(tiles_right(grid))
    if d=='left':
        return fusion_left(tiles_left(grid))



def get_new_tile():
    """
    Renvoie la valeur d’une nouvelle case (2 ou 4)
    Par défaut, les 2 sont plus fréquents que les 4

    CU: aucune
    """
    L=['2','2','4','2','2','2','4']
    for i in range(len(L)):
        return L[randint(0,7)]

def grid_score(grid):
    """
    Retournant le score, c’est-à-dire la somme des valeurs des tuiles présentes dans la grille

    CU: une grille carrée de 4 lignes

    Exemple:
    >>> grid=[[4, 2, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [4, 0, 0, 0]]
    >>> aide_grid_score(grid)
    14
    """







if __name__ == '__main__':
    import doctest
    doctest.testmod()
