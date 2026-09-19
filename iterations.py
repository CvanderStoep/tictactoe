piece = 100
for i in range(1, 100):
    print(i, i * piece / 100)
    piece = piece - i * piece / 100
