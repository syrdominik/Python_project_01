letter_dict = {'0': 'zero',
               '1': 'one',
               '2': 'two',
               '3': 'three',
               '4': 'four',
               '5': 'five',
               '6': 'six',
               '7': 'seven',
               '8': 'eight',
               '9': 'nine'}
def numbers_to_string(word):
  result = ""
  for letter in word:
    result += letter_dict[letter] + ' '
  return result

number = input("Give me a number: ").strip()
print(f"{number} -> {numbers_to_string(number)}")