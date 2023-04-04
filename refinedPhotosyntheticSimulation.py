# Dette eksempel er efter min mening bedre og mere troværdigt,
# fordi kurven i plottet har en svagt aftagende hældning,
# hvilket igen indikerer at den fotosyntetiske effekt har et optimum
# og som bekendt - træerne vokser ikke ind i himlen !

# For at simulere og plotte denne anden ordens differentialligning
# for fotosyntesen i Python, kan du følge disse trin - Held og lykke med opgaven :

#Importer de nødvendige biblioteker, herunder numpy og matplotlib:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#Definer konstanterne k og r, og definer en funktion I(t) for at repræsentere intensiteten af sollys,
# som varierer med tiden.
# For eksempel kan du bruge en sinusfunktion for at simulere dagslysets variationer:
k = 0.5
r = 0.1

def I(t):
    return 100 * (1 + np.sin(t/12))

#Definer den anden ordens differentialligning ved hjælp af en funktion,
# og definer startværdierne for G(t) og G'(t):
def G_diff_eq(G, t):
    return np.array([G[1], k * I(t) - r * G[1]])

G0 = np.array([0, 0]) # startværdier for G(t) og G'(t)

#Brug scipy.integrate.odeint funktionen til at løse denne anden ordens differentialligning numerisk
# og beregne G(t) for en række tidsværdier:
t = np.linspace(0, 48, 1000) # tidsværdier fra 0 til 48 timer
G = odeint(G_diff_eq, G0, t)

#Plot resultatet ved hjælp af matplotlib:
plt.plot(t, G[:, 0], label='Glucose') # plot G(t)
plt.xlabel('Time (hours)')
plt.ylabel('Glucose (mg)')
plt.legend()
plt.show()

#Dette vil generere et plot af mængden af glukose over tid,
# som varierer med sollysintensiteten og forbrugsraten.
# Du kan herefter justere konstanterne og intensitetsfunktionen til at simulere
# forskellige scenarier og observere, hvordan mængden af glukose varierer over tid.
