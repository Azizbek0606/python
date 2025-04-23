x = ["a", "b", "c", "d", "e", "f"]

for i in x:
    if i == "c":
        continue
    else:
        print(i)
else:
    x.remove("c")