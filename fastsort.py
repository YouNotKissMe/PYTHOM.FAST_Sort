import random
def fastsort(atoy):#есть шанс что я снова пузырьковую сортировочку написал , зато сам(нормально всё , но чтото с пределом рекурсии не ясно)
    zef=len(atoy)
    i=0
    if zef>2:
        a=random.choice(range(zef))
        for i in range(zef):
            if i!=a and atoy[a]<atoy[i] and a>i :
                atoy[a],atoy[i]=atoy[i],atoy[a]
            elif i!=a and atoy[a]>=atoy[i] and a<i:
                atoy[a], atoy[i] = atoy[i], atoy[a]
        h1=[k for k in atoy if k<atoy[a]]
        h2 = [k for k in atoy if k >= atoy[a]]
        fast=fastsort(h1)
        fast2=fastsort(h2)
        atoy=fast+fast2
    elif zef>1:
        if atoy[0]>atoy[1]:
            atoy[0],atoy[1]=atoy[1],atoy[0]
    return atoy
i=input('Введите элементы массива ')
i=i.split()
i=[int(a) for a in i if a.isdigit()==True]
print(fastsort(i))
