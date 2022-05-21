  # Author: Francisco Varela
  #10/05/2022
  #CEMES
from chantillon import *
from printdoc import *
test ="Y"
while(test=="Y"):

    if __name__ == '__main__':
        print("")

        print("******* DONNES DU ECHANTILLON *********** ")
        print("Signal Periodique  type :   n pts P% Fc[GS/s] ")
        print("type_signal  : sinus/Square [1/2] : ", end="")
        type_signal = int(input()) #VALEUR de cyscle pour le nombres de points
        print("Nombres de points : ", end="")
        n = float(input()) * type_signal   # n à chaque carreua alors n*2 dans un periode
        if type_signal==2:
            print("Pourcentage de Gating [%] : ", end="")
            P = float(input())
        print("Frequence de chantillonnage [GS/s] : ", end="")
        Fc = float(input())
        # P_ech point de echantillon Rechantillon par segundo
        if type_signal==2:
            t,f,t_unit,tg= type_square(Fc,n,P)  # unité en nano ns
        else :
            t, f, t_unit= type_sinus(Fc, n)
            tg=0
        printdoc(n, t, f, tg, t_unit,type_signal)  #ecrire sur un document
        print("********PRESENTATION DES VALEURS  ******* ")
        print("")
        print("{:.0f}pts dans un  Periode de T= {:.2f}ns".format(n,t))
        print("Frequence de {:.2}MHz ".format(f))
        if type_signal == 2:
            print("Temps Gating tg = {:.2}ns ".format(tg))
        print("Signal à 1pts en {:.2}ns ".format(t_unit))
        print("")
        print("************TABOR FINISHED ************** ")
        print("Nouveau calcul [Y/N]: ",end="")
        test = str(input())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

