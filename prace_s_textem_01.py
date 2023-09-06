# Soubor prikazu pro praci s textem

print("Toto je zkušební kód pro práci s textem")

quote_01 = input("Zadejte nějaké své oblíbené přísloví.: ")

page_width = input("Zadejte šířku zobrazované stránky: ")
print(f"Takto vypadá vaše přísloví zarovnané na střed stránky o šířce {page_width}. ")
print(quote_01.center(int(page_width)))

random_letter = input("Zadejte písmeno abecedy:")
print(f'Počet písmen "{random_letter}" v zadaném přísloví: ', quote_01.count(random_letter))

print(f"Počet písmen v zadaném přísloví: ", len(quote_01))

letter_minus = input("Zadejte číslo 1-10: ")

print(f"Zobrazení každého {letter_minus}. písmene po zpátku.")
print(quote_01[::-int(letter_minus)])

letter_plus = input("Zadejte další číslo 1-10: ")

print(f"Zonrazení každého {letter_plus}. písmene po předu.")
print(quote_01[::int(letter_plus)])
