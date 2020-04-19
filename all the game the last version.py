import random
def cls():
    i=int(0)
    for i in range (0,50):
        print ("\n")
z = 0
k=[]
q = 0
x = ["a","a","b","b","c","c","d","d","e","e","f","f","g","g","h","h","i","i","j","j"]
random.shuffle(x)
m = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
y = 0
print("1>> Human & computer")
print("2>> Human & Human")
print()

while 1:#chick he will enter numbers onle(1 to 16)
                        a=(input("choose the game option : "))
                        
                        f=['1','2']
                        ze = True
                        for i in range(2):
                            if (f[i]==a) :
                                ze = False
                                break
                        if ze == False :
                            break
a=int(a)
if a==2: #2 player2 vs eatch other
    #print(x)
    print (m)
    for i in range (100000000000000):
        while 1:#chick he will enter numbers onle(1 to 16)
                        j=(input("welcome: please,player1 enter the first number : "))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==j) :
                                ze = False
                                break
                        if ze == False :
                            break
        j=int(j)
        
        while 1:#chick he will enter numbers onle(1 to 16)
                        g=(input("welcome: please,player1 enter the second number :"))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==g) :
                                ze = False
                                break
                        if ze == False :
                            break
        g=int(g)
        
        while True:
            if (g>=20 or j>=20 or g<0 or j<0) or (g in k) or (j in k)or(g==j):
                
                while 1:#chick he will enter numbers onle(1 to 16)
                        j=(input("welcome: please,player1 enter the first number : "))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==j) :
                                ze = False
                                break
                        if ze == False :
                            break
                j=int(j)
                
                while 1:#chick he will enter numbers onle(1 to 16)
                        j=(input("welcome: please,player1 enter the second number :"))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==j) :
                                ze = False
                                break
                        if ze == False :
                            break
                j=int(j)
            else:
                break

        
        if (x[g]==x[j]and (m[g]!="*" and m[j]!="*")):
            m[g]=x[g]
            m[j]=x[j]
            print (m)
            z=z+1
            print("the score of player 1 is = ",z)
            print ("the score of player 2 is = ",y)
            m[j]="*"
            m[g]="*"
            k.append(g)
            k.append(j)
            
            
            print ("the new list is= ",m)

            
        else :
            m[g]=x[g]
            m[j]=x[j]
            print (m)
            i=int(0)
            for i in range (0,4000000):
                if i == 39999999 :
                    cls()
            m[g]=g
            m[j]=j
            print (m)
            print("the score of player 1 is = ",z)
            print("the score of player 2 is = ",y)
            
        while 1:#chick he will enter numbers onle(1 to 16)
                        j=(input("welcome: please,player2 enter the first number : "))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==j) :
                                ze = False
                                break
                        if ze == False :
                            break
        j=int(j)
        
        while 1:#chick he will enter numbers onle(1 to 16)
                        g=(input("welcome: please,player2 enter the second number :"))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==g) :
                                ze = False
                                break
                        if ze == False :
                            break
        g=int(g)
        
        while True:
            if (g>=20 or j>=20 or g<0 or j<0) or (g in k) or (j in k)or(g==j):
                while 1:#chick he will enter numbers onle(0 to 20)
                        j=(input("welcome: please,player2 enter the first number : "))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==j) :
                                ze = False
                                break
                        if ze == False :
                            break
                j=int(j)
                
                while 1:#chick he will enter numbers onle(0 to 20)
                        g=(input("welcome: please,player2 enter the second number :"))
                        
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            if (f[i]==g) :
                                ze = False
                                break
                        if ze == False :
                            break
                g=int(g)
                
            else:
                break

        if (x[g]==x[j]and (m[g]!="*" and m[j]!="*")):
            m[g]=x[g]
            m[j]=x[j]
            print (m)
            y=y+1
            print("the score of player 1 is = ",z)
            print("the score of player 2 is = ",y)
            m[j]="*"
            m[g]="*"
            k.append(g)
            k.append(j)
            
            
            print ("the new list is= ",m)


        else :
            m[g]=x[g]
            m[j]=x[j]
            print (m)
            i=int(0)
            for i in range (0,4000000):
                if i == 39999999 :
                    cls()
            m[g]=g
            m[j]=j
            print (m)
            print("the score of player 1 is = ",z)
            print("the score of player 2 is = ",y)
           
        
        if  ((y==5)&(z==5)):
            print ("draw")
            break
        if   (z>5):
            print(z, "player 1 is the winner")
            break
        
        if   (y>5):
            print (y, "player 2 is the winner")
            break


#___________________________________________________________________________________________________________________________
#player 1 vs pc
elif a==1:
    
    #print(x)
    print (m)
    for i in range (100000000000000):
        
        while 1:#chick he will enter numbers onle(0 to 20)
            
            j=(input("welcome: please,player1 enter the first number : "))
            f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
            ze = True
            for i in range(20):
                
                if (f[i]==j):
                    
                    ze = False
                    break
            if ze == False :
                
                break
        j=int(j)
                   
        
        while 1:#chick he will enter numbers onle(0 to 20)
            
            
            g=(input("welcome: please,player1 enter the second number :"))
            f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
            ze = True
            for i in range(20):
                
                if (f[i]==g) :
                    
                    ze = False
                    break
            if ze == False :
                
                break
        g=int(g)

    
        while True:
            
            if (g>=20 or j>=20 or g<0 or j<0) or (j in k) or (g in k)or(g==j):
                
                    
                    while 1:#chick he will enter numbers onle(1 to 16)
                        
                        j=(input("welcome: please,player1 enter the first number : "))
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            
                            if (f[i]==j) :
                                
                                ze = False
                                break
                        if ze == False :
                            
                            break
                    j=int(j)
        
                    while 1:#chick he will enter numbers onle(1 to 16)
                        
                        g=(input("welcome: please,player1 enter the second number :"))
                        f=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                        ze = True
                        for i in range(20):
                            
                            if (f[i]==g) :
                                
                                ze = False
                                break
                        if ze == False :
                            
                            break
                    g=int(g)
          
            else:

                
                break
        
        if (x[g]==x[j]and (m[g]!="*" and m[j]!="*")):#the turn to player 1
            
            
            m[g]=x[g]
            m[j]=x[j]
            print (m)
            z=z+1
            print("the score of player 1 is = ",z)
            print("the score of pc is = ",q)
            m[j]="*"
            m[g]="*"
            k.append(g)
            k.append(j)
            print ("the new list is= ",m)
            

            s = random.randrange(0,19)
            v = random.randrange(0,19)
            print(s,v)
            while (s in k) or (v in k) or (s==v):
                
                
                s = random.randrange(0,19)
                v = random.randrange(0,19)
                print(s,v)
                
                      
            
            if (x[s]==x[v] and (m[s]!="*" and m[v]!="*")):
                
                m[s]=x[s]
                m[v]=x[v]
                print (m)
                q=q+1
                print("the score of player 1 is = ",z)
                print("the score of pc is = ",q)
                m[v]="*"
                m[s]="*"
                k.append(s)
                k.append(v)
                      
                print ("the new list is= ",m)


            
            elif (x[s]!=x[v]and (m[s]!="*" and m[v]!="*")):
                
                
                m[s]=x[s]
                m[v]=x[v]
                print (m)
                i=int(0)
                for i in range (0,4000000):
                    
                
                    if i == 39999999 :
                        
                        cls()
                m[s]=s
                m[v]=v
                print (m)
                print("the score of player 1 is = ",z)
                print ("the score of pc is = ",q)
                    
            
        
        elif(x[g]!=x[j]and (m[g]!="*" and m[j]!="*")):#the other type of player 1
            m
            m[g]=x[g]
            m[j]=x[j]
            print (m)
            i=int(0)
            for i in range (0,4000000):
                
                if i == 39999999 :
                    
                    cls()
                    
            m[g]=g
            m[j]=j
            print (m)
            print("the score of player 1 is = ",z)
            print("the score of pc is = ",q)
            for i in range (0,4000000):
                
                if i == 39999999 :
                    
                    
                    cls()

            s =random.randrange(0,19)
            v =random.randrange(0,19)
            while (s in k) or (v in k) or v==s:
                m
                s =random.randrange(0,19)
                v =random.randrange(0,19)
                print(s,v)


                if (x[s]==x[v]and (m[s]!="*" and m[v]!="*")):
                    
                    
                    m[s]=x[s]
                    m[v]=x[v]
                    print (m)
                    q=q+1
                    print("the score of player 1 is = ",z)
                    print("the score of pc is = ",q)
                    m[s]="*"
                    m[v]="*"
                       
                    print ("the new list is= ",m)


                elif(x[s]!=x[v]and (m[s]!="*" and m[v]!="*")):
                    
                    
                    m[s]=x[s]
                    m[v]=x[v]
                    print (m)
                    m[s]=s
                    m[v]=v
                    print (m)
                    print("the score of player 1 is = ",z)
                    print ("the score of pc is = ",q)
        
           
                
                if  ((z==5)&(q==5)):# the tybe of draw
                    
                    
                   
                    print ("draw")
                    break
                if   (z>5):# player 1 is winner
                    
                    print(z, "player 1 is the winner")
                    break
         
                if   (q>5):#pc is winner
                    
                    print (q, "pc  is the winner")
                    break  
