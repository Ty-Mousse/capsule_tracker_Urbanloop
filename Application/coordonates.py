import numpy as np

# Méthode permettant d'obtenir les coordonnées cartésiennes d'un point du circuit à partir de son abscisse curviligne
def get_coordonates(long):
    l = long%212149
    if l <= 14101:
        teta1= 0.35
        x = l*np.cos(teta1)
        y = l*np.sin(teta1)
        return x, y
    elif l <= 22993:
        l2 = l-14101
        teta2 = l2/10449
        x = 7426+10449*np.cos(teta2-0.98)
        y = 13526.8+10449*np.sin(teta2-0.98)
        return x, y
    elif l <= 26480:
        l3 = l-22993
        x = 17786
        y = 12182+l3
        return x, y
    elif l <= 39191:
        l4 = l-27917
        teta3 = l4/11000
        x = 6890.8+11000*np.cos(teta3+0.138)
        y = 14176+11000*np.sin(teta3+0.138)
        return x, y
    elif l <= 73781:
        teta5 = 0.33
        l5 = l-39191
        x = 11254-l5*np.cos(teta5)
        y = 24273+l5*np.sin(teta5)
        return x, y
    elif l <= 97030:
        l6 = l-73781
        teta6 = l6/18000
        x = -28778.9+857+18000*np.cos(teta6+1.196)
        y = 20952.8-2019+18000*np.sin(teta6+1.196)
        return x, y
    elif l <= 132670:
        teta7 = 1.035
        l7 = l - 97030
        x = -42207-l7*np.cos(teta7)
        y = 29884-l7*np.sin(teta7)
        return x, y
    elif l <= 150940:
        r8 = 11000
        teta8i = 2.63
        l8 = l-132670
        teta8 = l8/r8
        x = -52207 + r8*np.cos(teta8 + teta8i)
        y = -6975.9 + r8*np.sin(teta8 + teta8i)
        return x, y
    elif l <= 152540:
        teta9 = 0.47
        l9 = l-150940
        x = -56707 + l9*np.cos(0.47)
        y = -17013 - l9*np.sin(0.47)
        return x, y
    elif l <= 161533:
        teta10i = 4.22
        r10 = 11000
        l10 = l-152540
        teta10 = l10/r10
        x = -50606.8 + r10*np.cos(teta10+teta10i)
        y = -7250 + r10*np.sin(teta10+teta10i)
        return x, y
    elif l <= 212149:
        teta1= 0.35
        x = (l-161533)*np.cos(teta1) - 47470
        y = (l-161533)*np.sin(teta1) - 17566
        return x, y

    