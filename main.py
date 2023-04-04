# På bagrund af nedenstående om en fotosyntese model - efter kolon,
# ønsker jeg at lave et Python program som kan simulere og plotte
# en anden ordens differential ligning for fotosyntesen:
#
# Fotosyntese er den proces, hvor planter og andre autotrofe organismer
# bruger sollys til at omdanne vand og kuldioxid til glukose og oxygen.
# Denne proces kan beskrives med en anden ordens differentialligning,
# der modellerer ændringen i mængden af glukose i løbet af tiden.
# Lad G(t) være mængden af glukose på tidspunktet t.
# Så kan vi definere en anden ordens differentialligning,
# der beskriver ændringen i G(t) over tid som:
#
# G''(t) = k * I(t) - r * G'(t)
#
# hvor G'(t) er den første afledte af G(t) og angiver hastigheden af ændringen i mængden af glukose,
# G''(t) er den anden afledte af G(t) og angiver accelerationen af ændringen i mængden af glukose,
# k er en konstant, der angiver fotosyntese effektiviteten,
# I(t) er intensiteten af sollys, som varierer med tiden, og
# r er en konstant, der angiver forbruget af glukose.
#
# Den første del af ligningen, k * I(t), repræsenterer produktionen af glukose gennem fotosyntese,
# mens den anden del, r * G'(t), repræsenterer forbruget af glukose af planten til energi og vækst.
#
# Denne ligning beskriver således balancen mellem produktion og forbrug af glukose i planter og
# kan bruges til at forudsige mængden af glukose på ethvert tidspunkt.
#
#
# For at simulere og plotte denne anden ordens differentialligning for fotosyntese,
# kan du bruge Python's numeriske beregningsbibliotek, NumPy, og plotting bibliotek, Matplotlib.
#
# Først skal du importere de nødvendige biblioteker og definere konstanterne k og r:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k = 0.5  # Fotosyntese effektivitet konstant
r = 0.1  # Forbrug af glukose konstant

# Derefter kan du definere funktionen, der beskriver anden ordens differentialligning for fotosyntese,
# og definere startbetingelserne for mængden af glukose og dens hastighed:

def glucose(G, t):
 I = 1 + 0.5 * np.sin(t)  # Intensiteten af sollys, der varierer med tiden
 G0 = 10  # Start mængden af glukose
 G1 = 0  # Start hastighed af glukose ændring
 return [G[1], k * I - r * G[1]]

# Her bruger vi en sinusfunktion til at simulere varierende intensitet af sollys,
# der angives af I(t).
# Startbetingelserne for mængden af glukose og dens hastighed er henholdsvis G0 og G1.
# Endelig kan du bruge NumPy's "odeint" funktion til at løse differentialligningen numerisk
# og plotte resultaterne:

t = np.linspace(0,10,1000)
# Tidspunkter for simuleringen
G = np.zeros((len(t), 2))  # Matrix til at gemme løsningen
G[0, 0] = 10  # Start mængden af glukose
sol = odeint(glucose, G[0], t)  # Løs differentialligningen numerisk
G = sol[:, 0]  # Hent den numeriske løsning for mængden af glukose

# Plot resultatet
plt.plot(t, G)
plt.xlabel('Tid')
plt.ylabel('Mængde af glukose')
plt.show()

# Her opretter vi en tidsvektor, "t", og en matrix, "G",
# til at gemme løsningen for mængden af glukose og dens hastighed.
# Vi bruger også NumPy's "zeros" funktion til at initialisere G-matrixen
# med startbetingelserne for mængden af glukose og dens hastighed.
#
# Vi løser så differentialligningen numerisk ved hjælp af "odeint" funktionen,
# som tager funktionen glucose, startbetingelsen for mængden af glukose og
# tidsvektoren som input. Resultatet gemmes i "sol" variablen,
# og vi henter derefter løsningen for mængden af glukose i "G"
#
# ved hjælp af  "sol [:, 0]" # notationen.
#
# Endelig plotter vi resultatet ved hjælp af Matplotlibs
# "plot" funktion og angiver akseetiketter
# og en titel ved hjælp af "xlabel", "ylabel" og "title" funktioner.
