f = open("input1.txt")
integers = []
for line in f:
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            digits.append(line[i])
            break
    integers.append(int("".join(digits)))
f.close()
print(sum(integers))