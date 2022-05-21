  # Author: Francisco Varela
  #10/05/2022
  #CEMES
test ="Y"
while(test=="Y"):
    print("")

    print("******* DONNES DU ECHANTILLON *********** ")
    print("Signal Periodique  type :   n pts P% Fc[GS/s] ")
    print("Nombres de points : ", end="")
    n = float(input()) * 2  # n à chaque carreua alors n*2 dans un periode
    print("Pourcentage de Gating [%] : ", end="")
    P = float(input())
    print("Frequence de chantillonnage [GS/s] : ",end="")
    Fc=float(input())
    Pt_ech= Fc #P_ech point de echantillon   par segundo




    def chantillon(fc,n,p):
        t_x=(1/Pt_ech)*n        #Determination de periode
        f_x=(1/t_x)*1000        #Determination de frequence
        t_unit = (1 / Pt_ech) * 1 #Temps pour n=1pts
        t_gating =  ((t_x/2)*P)/100
        return (t_x,f_x,t_unit,t_gating)   #  #echantillon par ns *temps mise pour total de n

    t,f,t_unit,tg= chantillon(Fc,n,P)  # unité en nano ns

    print("********PRESENTATION DES VALEURS  ******* ")
    print("")
    print("{:.0f}pts dans un  Periode de T= {:.2f}ns".format(n,t))
    print("Frequence de {:.2}MHz ".format(f))
    print("Temps Gating tg = {:.2}ns ".format(tg))
    print("Signal à 1pts en {:.2}ns ".format(t_unit))
    print("")
    print("************TABOR FINISHED ************** ")
    print("Nouveau calcule [Y/N]: ",end="")
    test = str(input())
