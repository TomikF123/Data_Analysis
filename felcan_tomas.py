import pandas as pd
import numpy as np
data = pd.read_csv("M000102c_1991_2021.csv")
activity = "B"
df = data["value"][(data["activity"] == activity)] # choose the value of "activity" from _T or (A - S) to analyze different sectors of the Economy
l = np.array(df,dtype= int)

print(activity)

aMean = l.mean() # arythmetic mean
mn = min(l) # minimal value
mx = max(l) # maximal value
ln = len(l) # amount of values
def g_mean(x): # geometric mean, avoiding overlow
    a = np.log(x)
    return np.exp(a.mean())
gMean = g_mean(l)
def harmonic_mean(x):
    v = len(x)
    sum_of_inverted_values = 0
    for n in x:
        sum_of_inverted_values += 1/n
    return v/sum_of_inverted_values
harmMean = harmonic_mean(l)

def modus(x): #calculating the mode with a frequency table
    help_dict = {}
    for n in x:
        if round(n/1000) in help_dict:
            help_dict[round(n/1000)] += 1
        else:
            help_dict[round(n/1000)] = 1
    key_list = list(help_dict.keys())
    val_list = list(help_dict.values())
    return key_list[max(val_list)]*1000

mds = modus(l)
def median(x): # picking the ln//2 ellement of sorted list
    x=sorted(x)
    if ln%2 != 0:
        return x[(ln)//2]
    else:
        return (x[ln/2] + x[ln/2 +1])/2
med = median(l)
print(f"Produkce podle odvětví (ceny roku 2015) - Zemědělství, lesnictví a rybářství. \n\n Míry polohy:\n"
      f"Aritmetický průměr: {aMean} \n"
      f"Gemetrický průměr: {gMean} \n"
      f"Harmonický průměr: {harmMean} \n"
      f"Maximální hodnota: {mx} \n"
      f"Minimální hodnota: {mn}\n"
      f"Modus: {mds}\n"
      f"Medián: {med}\n"
      f"Dolní kvartil {np.percentile(sorted(l),25)}\n"
      f"Horní kvartil {np.percentile(sorted(l),75)}\n"
      f"\n Míry variability: \n"
      f"populační rozptyl a směrodaná odchylka: {np.var(l)},  {np.var(l)**(1/2)}\n"
      f"výběrový rozptyl a směrodatná odchylka: {np.cov(l)}, {np.cov(l)**(1/2)}\n"
      f"Variační rozpětí: {mx-mn}\n"
      f"Variační koeficient (výběrový sd): {np.cov(l)**(1/2)/aMean}")








