
first_name = input("Nome:")
first_attack = int(input("Ataque:"))
first_defence = int(input("Defesa:"))

second_name = input("Nome:")
second_attack = int(input("Ataque:"))
second_defence = int(input("Defesa:"))

third_name = input("Nome:")
third_attack = int(input("Ataque:"))
third_defence = int(input("Defesa:"))

array_bidimensional = [[str(first_name), str(first_attack), str(first_defence)], [str(second_name), str(second_attack), str(second_defence)], [str(third_name), str(third_attack), str(third_defence)]]

print(array_bidimensional)

a = sorted(array_bidimensional)

print("Ataque", max(a[0]))
print("Defesa", max(a[0]))

