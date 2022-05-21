import datetime
date = str(datetime.datetime.now())
def printdoc(n,t,f,tg,t_unit,type_signaldoc):
    with open("TABOR_TEST.txt", "a") as o:
        date = str(datetime.datetime.now())
        o.write(date +"\n")
        o.write("********PRESENTATION DES VALEURS  ******* \n")
        o.write("\n")
        o.write("{:.0f}pts dans un  Periode de T= {:.2f}ns \n".format(n, t))
        o.write("Frequence de {:.2}MHz \n".format(f))
        if type_signaldoc ==2 :
            o.write("Temps Gating tg = {:.2}ns \n".format(tg))
        o.write("Signal à 1pts en {:.2}ns \n".format(t_unit))
        o.write("")
        o.write("************TABOR FINISHED ************** \n")
        o.close()