a = 1000
counter = 1
while counter <= 100:
    print(f"{counter} - ({a:,})")
    a = a + (a // 10)
    counter += 1
