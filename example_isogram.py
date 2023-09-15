nadpis = str("Isogram je slovo, kde se neopakují žádná písmena")
print(f"\n{nadpis}")
print("-" * len(nadpis))

def is_isogram(word):
    letters = set()
    for letter in word.lower():
        if letter in letters:
            return False
        letters.add(letter)
    return True

done = False
while not done:
  my_word = input("\nZadejte slovo: ").strip()
  #answer = "is" if is_isogram(my_word) else "is_not"
  if is_isogram(my_word):
    answer = "je"
  else:
    answer = "není"
  print(f"Slovo {my_word} {answer} isogram\n")
  shall_continue = input("Chcete pokračovat ([a]/n)?: ")
  if shall_continue.lower() != "a":
    done = True