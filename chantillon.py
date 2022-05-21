
def type_sinus(fc, n):
    Pt_ech = fc  # #P_ech *10^9 point de echantillon  par 1 segundo
    t_x = (1 / Pt_ech) * n  # Determination de periode
    f_x = (1 / t_x) * 1000  # Determination de frequence
    t_unit = (1 / Pt_ech) * 1  # Temps pour n=1pts
    return (t_x, f_x, t_unit)  # #echantillon par ns *temps mise pour total de n

def type_square(fc, n,p):
    Pt_ech = fc  # #P_ech *10^9 point de echantillon  par 1 segundo
    t_x = (1 / Pt_ech) * n  # Determination de periode
    f_x = (1 / t_x) * 1000  # Determination de frequence
    t_unit = (1 / Pt_ech) * 1  # Temps pour n=1pts
    t_gating = ((t_x / 2) * p) / 100
    return (t_x, f_x, t_unit, t_gating)  # #echantillon par ns *temps mise pour total de n


