def nb_year(p0, percent, aug, p):
    numberofyears = 0
    pn = (p0)
    while(pn < p):
        pn = int(pn) + ((percent/100) * pn) + aug
        numberofyears += 1
    return numberofyears

