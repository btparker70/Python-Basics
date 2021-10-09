names = ["AJohn", "Mary"]
# found = False
# for name in names:
#   if name.startswith("J"):
#     print("Found")
#     found = True
#     break

# if not found:
#   print("Not found")


for name in names:
  if name.startswith("J"):
    print("Found")
    found = True
    break

else:
  print("Not found")