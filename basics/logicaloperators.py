# and
# or
# not

name = ""
# if name is an emptry string

if not name:
  print("Name is empty")

if not name.strip():
  print("Name is empty")

age = 22
if age >= 18 and age < 65:
  print("Eligible")

if 18 <+ age < 65:
  print("Eligible")