
weigth = input("Zadejte vaši váhu v [kg]: ")
height = input("Zadejte vaši výšku v [cm]: ")
gender = input("Zadejte své pohlaví [muž/ žena/ oni]: ")

result_they_18 = "Jste podvyživeni."
result_man_18 = "Jste podvyživen."
result_women_18 = "Jste podvyživena."
result_all_25 = "Máte normální postavu."
result_all_30 = "máte nadváhu"
result_all_35 = "Jste obézní."
result_all_over = "Jste extrémně obézní."

def compute_bmi(weight, height):
  bmi = int(weight) / (int(height)/100) ** 2
  if bmi < 18.5 and gender == "muž":
    result = result_man_18
  elif bmi < 18.5 and gender == "žena":
    result = result_women_18
  elif bmi < 18.5 and gender == "oni":
    result = result_they_18
  elif bmi < 25:
    result = result_all_25
  elif bmi < 30:
    result = result_all_30
  elif bmi < 35:
    result = result_all_35
  else:
    result = result_all_over
  return (round(float(bmi),2), result)
# outside of the function


bmi_tuple = compute_bmi(weigth, height)
print(bmi_tuple)

