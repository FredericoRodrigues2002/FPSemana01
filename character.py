
first_name = input("Nome:")
first_attack = int(input("Ataque:"))
first_defence = int(input("Defesa:"))

second_name = input("Nome:")
second_attack = int(input("Ataque:"))
second_defence = int(input("Defesa:"))

third_name = input("Nome:")
third_attack = int(input("Ataque:"))
third_defence = int(input("Defesa:"))

array_bidimensional = [[first_name, first_attack, first_defence], [second_name, second_attack, second_defence], [third_name, third_attack, third_defence]]

print(array_bidimensional)

strongest_attack = array_bidimensional[0]
strongest_defence = array_bidimensional[0]


for x in array_bidimensional:
    if x[1] > strongest_attack[1]:
        strongest_attack = x
    if x[2] > strongest_defence[2]:
        strongest_defence = x

print("Ataque", strongest_attack[0], strongest_attack[1])
print("Defesa", strongest_defence[0], strongest_defence[2])