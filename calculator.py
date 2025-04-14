import math

megoldás = 0

def plusz(elso,masodik):
    megoldás = elso+masodik
    print(megoldás)
    return elso,masodik,megoldás

def minusz(elso,masodik):
    megoldás = elso-masodik
    print(megoldás)
    return elso,masodik,megoldás

def szorzas(elso,masodik):
    megoldás = elso*masodik
    print(megoldás)
    return elso,masodik,megoldás

def osztas(elso,masodik):
    megoldás = elso/masodik
    print(megoldás)
    return elso,masodik,megoldás


exit = False
elozo_eredmeny = 0 

   
"""def elso_szam(elozo_eredmeny):
    elso = input(f"Add meg az elso szamot, ha entert nyomsz akkor az elozo eredmeny lesz ami : {elozo_eredmeny}   : ")
    if elso == "":
        pass
    else:
        elso = float(elso)
    return elso"""



while not exit:
    
    elso = float(input("Add meg az első számot: "))
    
    muvelet = input("Add meg a műveletet: + - * /: ")
    
    masodik = float(input("Add meg a második számot: "))

    
    if(muvelet == "+"):
        plusz(elso,masodik)
        
        
        
    if(muvelet == "-"):
        minusz(elso, masodik)
        
    
    if(muvelet == "*"):
        szorzas(elso, masodik)
        
        
        
    if(muvelet == "/"):
        osztas(elso, masodik)
        
    
    quit = input("Akarsz még számoni? i/n: ")    
    
    if quit.lower()  == "n" : 
        exit = True
        