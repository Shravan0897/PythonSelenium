it = 4
while it > 1:
    print(it)
    it = it - 1
print("while loop is done")

gg = 10
while gg > 1:
    if gg == 8:
        gg = gg - 1
        continue
    if gg == 3:
        break
    print(gg)
    gg = gg - 1
print("while loop is done")