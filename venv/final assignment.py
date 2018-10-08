#Schrijf functie standaardprijs(afstandKM).
#Iedere treinrit kost 80 cent per kilometer,
#maar als de rit langer is dan 50 kilometer betaal je een vast bedrag van €15,- plus 60 cent per kilometer.
#Ga bij invoer van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

def standaardprijs(afstandKM):
    if afstandKM >= 50.0:
        standaardprijs = afstandKM * 0.6 + 15
        return standaardprijs
    elif afstandKM > 0 and afstandKM < 50:
        standaardprijs = afstandKM * 0.80
        return standaardprijs
    else:
        standaardprijs = afstandKM <= 0
        return 0.0

def ritprijs(leeftijd, weekendrit, afstandKM):
    stdprijs = standaardprijs(afstandKM)

    if leeftijd <= 12 or leeftijd >= 65:
        if weekendrit ==True:
            return stdprijs * 0.65
        else:
            return stdprijs * 0.70
    else:
        if weekendrit == True:
            return stdprijs * 0.60

        else:
            return stdprijs * 1

print(ritprijs(11, True, 50))#verwacht = 29.25, uitkomst = 29.25
print(ritprijs(12, True, 50))#verwacht = 29.25, uitkomst = 29.25
print(ritprijs(64, True, 50))#verwacht = 27.0, uitkomst = 27.0
print(ritprijs(65, True, 50))#verwacht = 29.25, uitkomst = 29.25
print(ritprijs(11, False, 50))#verwacht = 31.496, uitkomst = 31.496
print(ritprijs(12, False, 50))#verwacht = 31.496, uitkomst = 31.496
print(ritprijs(64, False, 50))#verwacht = 45.0, uitkomst = 45.0
print(ritprijs(65, False, 50))#verwacht = 31.496, uitkomst = 31.496
print(ritprijs(11, True, 20))#verwacht = 10.4, uitkomst = 10.4
print(ritprijs(12, True, 20))#verwacht = 10.4, uitkomst = 10.4
print(ritprijs(64, True, 20))#verwacht = 9.6, uitkomst = 9.6
print(ritprijs(65, True, 20))#verwacht = 10.4, uitkomst = 10.4
print(ritprijs(11, False, 20))#verwacht = 11.2, uitkomst = 11.2
print(ritprijs(12, False, 20))#verwacht = 11.2, uitkomst = 11.2
print(ritprijs(64, False, 20))#verwacht = 16.0, uitkomst = 16.0
print(ritprijs(65, False, 20))#verwacht = 11.2, uitkomst = 11.2
print(ritprijs(11, True, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(12, True, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(64, True, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(65, True, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(11, False, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(12, False, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(64, False, -40))#verwacht = 0.0, uitkomst = 0.0
print(ritprijs(65, False, -40))#verwacht = 0.0, uitkomst = 0.0


#commit