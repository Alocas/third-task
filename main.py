mass = [0, 1, 2, 5, 3, 0, 3, 6, 7, 8, 2, 5, 5, 9, 8, 4, 5, 6, 7, 8, 9, 0]
zero = []
four = []
six = []
eigth = []
nine = []
other = []

for i in range(len(mass)):
    if mass[i] == 0:
        zero.append(mass[i])
    elif mass[i] == 4:
        four.append(mass[i])
    elif mass[i] == 6:
        six.append(mass[i])
    elif mass[i] == 8:
        eigth.append(mass[i])
    elif mass[i] == 9:
        nine.append(mass[i])
    else:
        other.append(mass[i])
  
other.sort()

print(other + zero + four + six + nine + eigth)
