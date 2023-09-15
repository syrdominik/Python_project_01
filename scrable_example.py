nadpis = str("HRA SCRABBLE")
print(f"\n{nadpis}")
print("=" * len(nadpis))


letters = []
for i in range(26): # zarání rozsahu písmen
    letter = chr(97 + i) # zadáním písmen od 97. znaku, což je malé "a"
    letters.append(letter) # přidání kažného znaku písmene do seznamu písmen

# TO DO - doplnit i další písmena abecedy s háčkama a čárkama a rozšířit slovník s bodama
#print(letters) - smazáním # se zobrazí výpis písmen

point_values = [1, 3, 1, 4, 1, 8, 3, 2, 2, 4, 5, 1, 3, 1, 10, 1, 1, 4, 1, 3, 1, 1, 4, 8, 4, 10]
# zadání hodnot jednotlivým písmenům

point_value_dict = dict(zip(letters, point_values))

#print(point_value_dict) - smazáním # se zobrazí výpis slovníku písmen a jeho hodnot

def scrabble_score(word, scoring=point_value_dict):
    total_score = 0
    for letter in word.lower():
        total_score += scoring[letter]
    return total_score

done = False
while True:
    my_word = input("\nZadejte slovo (bez háčků a čárek: ").strip()
    score = scrabble_score(my_word)
    print(f"Slovo {my_word} má hodnotu {score} bodů ve Srabble\n")
    shall_continue = input("Chcete pokračovat? ([a]/n)?: ")
    if shall_continue.lower() != "a":
        done = True