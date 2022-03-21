import random

hromadka1, hromadka2, hromadka3 = 2,3,2
x = [hromadka1, hromadka2, hromadka3]
y = [2,3,2]

def binarni(y):

    z = []
    for i in range(len(y)):
        z.append(list (format(y[i], 'b')))
   
        if len(z[i]) == 1:
            z[i].insert(0, 0)
 
    return z

z = binarni(y)

def xor (y):
    
    soucet = []
    z = binarni(y) 

    a = [(int(z[0][0]) ^ int(z[1][0])), (int(z[0][1]) ^ int(z[1][1]))] 
    soucet = [(a[0]^ int(z[2][0])), (a[1]^ int(z[2][1]))]
         
    return soucet


def mozne(y):
    
    seznam = []
    for hromadka in range(0, len(y)):
        for sirky in range(1, y[hromadka]+1):

                if y[hromadka] == 0 or y[hromadka] - sirky < 0 or sirky <=0:
                    False
                    
                else:
                     True

                if True:     
                    seznam.append([hromadka, sirky])

    return seznam



def napoveda(y):
    
     nulovyxor = False
     if nulovyxor == False:

             for hromadka in range(0, len(y)):
                for sirky in range (1,y[hromadka]+1):       
                         
                    for _ in mozne(y):
                        y[hromadka] -= sirky   
                        xor((y))  
                                 
                        if xor(y) == [0,0]:                                              
                            y[hromadka] += sirky
                            return [hromadka, sirky]                                 
    
                        else:
                            y[hromadka] += sirky
                            False

     return False
                             
          
def prvnihrac(x):

       
      if konec() == True:
          print ('Prohráli jste.')
          
      else:          
          napoveda(y)
          print('Nápověda: Vyberte {}. hromádku a vytáhněte {} sirek.'. format(napoveda(y)[0]+1, napoveda(y)[1]))
          
          #výběr hromádky a počtu sirek 
          hrac1h = int (input('Ze které hromádky chcete sirky odebírat?'))
          hrac1s = int (input('Kolik sirek chcete odebrat?'))  
          print('Odebrali jste', hrac1s, 'sirek z ', hrac1h, '. hromadky' )    
            
          #odebrání sirek 
          if hrac1h > len(x):
             print('Tolik hromádek ve hře není')
             hrac1h = int(input('Vyberte hromádku: '))
             hrac1s = int (input('Kolik sirek chcete odebrat?'))
             x[hrac1h-1] -= hrac1s
             y[hrac1h-1] -= hrac1s
             
          elif hrac1s == 0:
              print('Musíte vytáhnout alespoň jednu sirku.')
              hrac1s = int(input('Kolik sirek chcete tahat?'))
              x[hrac1h-1] -= hrac1s
              y[hrac1h-1] -= hrac1s              
              
          elif hrac1s > x[hrac1h-1]:
              print('Tolik sirek ve', hrac1h, 'není.')
              hrac1s = int(input('Počet sirek: '))
              x[hrac1h-1] -= hrac1s
              y[hrac1h-1] -= hrac1s
            
          else:
              x[hrac1h-1] -= hrac1s
              y[hrac1h-1] -= hrac1s
              
      return x
        
        
def druhyhrac(x):
    if konec() == True:
        print('Vyhráli jste.')
        
    else:
        a = []
        for i in range(len(x)):
            if x[i] != 0:
                b = x[i]
                a.append(x.index(b))        
        hrac2h = int (random.choice(a))
        hrac2s = random.randint(1, x[hrac2h])
        x[hrac2h] -= hrac2s
        y[hrac2h] -= hrac2s
        print('Druhý hráč odebral', hrac2s, 'sirek z', hrac2h+1, 'hromadky.' )

    return x
        

def konec():
    if x == [0,0,0]:
        return True
    else:
        return False


def hra():
  
    print('Stav hry: ', x)

    if not konec():
       
        napoveda(y)
        prvnihrac(x)
        druhyhrac(x)

    else:
        return False
    return True

   
while hra() == True:
    hra()
