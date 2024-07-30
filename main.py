RED = "\033[0;31m"
RESET = "\033[0m"

def system(outp):
  print("System Message:",outp)
def cooper(outp):
  print("Cooper:",outp)
def kripke(outp):
  print("Kripke:",outp)
def inpMess():
  return input("Input ('Yes' or 'No'): ")
def invInp(i):
  print("Invalid input.")
  if i == 3:
      print(RED + "\nSystem Termination.")
      quit()

print()
print(RESET + "[Placing Phone Call...]")
kripkeAns = None
for i in range(4):
  print()
  system("Is Kripke currently available to be contacted?")
  kripkeAns = inpMess()
  if kripkeAns == "Yes":
    break
  elif kripkeAns == "No":
    cooper(input("As Cooper, please leave a message for Kripke.\nMessage: "))
    print("[Waiting for a certain interval of time...]")
    if i == 3:
      print(RED + "\nUnfortunately Kripke is unable to be contacted.")
      quit()
  else:
    invInp(i)
    if i == 3:
      quit()

print()
cooper("Would you like to share a meal?")
for i in range(4):
  print()
  system("Does Kripke want to share a meal with Cooper?")
  mealAns = inpMess()
  if mealAns == "Yes":
    print("[Cooper and Kripke share a meal together.]")
    quit()
  elif mealAns == "No":
    break
  else:
    invInp(i)


