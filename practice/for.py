# for i in range(1, 6):
#     print(i, end=" ")

# print()

# for i in range(1, 10, 3):
#     print(i, end=", ")

# print()
# n = 3
# for i in range(1, 11):
#     print(n, " X ", i, " = ", n * i)

for i in range(1, 11):
    for j in range(1, 11):
        if j == 5:
            break
        print(j, end=" ")
    print()