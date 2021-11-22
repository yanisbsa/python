import numpy as np
def pythagore() :
    print (" Vous avez un triange abc rectangle et vous voulez calculer un de ses coté ?  ")
    hypo = ""
    while (hypo!= "a" and hypo != "b" and hypo!= "c" ) : 
    
            hypo = input(" Hypothénus ?")
            
    if (hypo =="a"):
        cote = ""
        
        while (cote!= "a" and cote != "b" and cote!= "c" ) : 
            
                cote = input(" quel coté cherchez vous ?")
            
        while(cote =="a"):
            try :
                b = float(input ("entrez la longueur du coté b"))
                c = float(input ("Entrez la longueur du coté c "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                a = np.sqrt(b**2+c**2)
                print("La longueur de a est %.2f"% a)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
            
        while(cote =="b"):
            try :
                a = float(input ("entrez la longueur du coté a"))
                c = float(input ("Entrez la longueur du coté c "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                b = np.sqrt(a**2-c**2)
                print("La longueur de b est %.2f"% b)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")    
            
        while(cote =="c"):
            try :
                a = float(input ("entrez la longueur du coté a"))
                b = float(input ("Entrez la longueur du coté b "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                c = np.sqrt(a**2-b**2)
                print("La longueur de c est %.2f"% c)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
            
    if (hypo =="b"):
        cote = ""
        
        while (cote!= "a" and cote != "b" and cote!= "c" ) : 
        
                cote= input(" quel coté cherchez vous ?")
            
        while(cote =="a"):
            try:
                b = float(input ("entrez la longueur du coté b"))
                c = float(input ("Entrez la longueur du coté c "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                a = np.sqrt(b**2-c**2)
                print("La longueur de a est %.2f"% a)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
            
        while(cote =="b"):
            try:
                a = float(input ("entrez la longueur du coté a"))
                c = float(input ("Entrez la longueur du coté c "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                b = np.sqrt(a**2+c**2)
                print("La longueur de b est %.2f"% b) 
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
            
        while(cote =="c"):
            try:
                a = float(input ("entrez la longueur du coté a"))
                b = float(input ("Entrez la longueur du coté b "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                c = np.sqrt(b**2-a**2)
                print("La longueur de c est %.2f"% c)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
     
    if (hypo =="c"):
        cote = ""
        while (cote!= "a" and cote != "b" and cote!= "c" ) :
                cote = input(" quel coté cherchez vous ?")
        while(cote =="a"):
            try:
                b = float(input ("entrez la longueur du coté b "))
                c = float(input ("Entrez la longueur du coté c "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))               
                a = np.sqrt(c**2-b**2)
                print("La longueur de a est %.2f"% a)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
        while(cote =="b"):
            try:
                a = float(input ("entrez la longueur du coté a"))
                c = float(input ("Entrez la longueur du coté c "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                b = np.sqrt(c**2-a**2)
                print("La longueur de b est %.2f"% b)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")
        while(cote =="c"):
            try:
                a = float(input ("entrez la longueur du coté a "))
                b = float(input ("Entrez la longueur du coté b "))
                while (b not in range (1,1000000) or c not in range (1,1000000)):
                    raise Exception("la valeur de a ou de b est trop grande ou trop petite")
                    b = float(input ("entrez la longueur du coté b"))
                    c = float(input ("Entrez la longueur du coté c "))       
                c = np.sqrt(b**2+a**2)
                print("La longueur de c est %.2f"% c)
                break
            except :
                print ("la valeur entrée n'est pas la bonne !")

            
            
            
        
        
        
   
    