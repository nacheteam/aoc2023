def findDigit(line, numbers, start, end, step):
    for i in range(start, end, step):
        if line[i].isdigit():
            return line[i]
        else:
            sub = line[:i+1] if step==1 else line[i:]
            #print(line, " - ", sub, " - ", "reverse" if step==-1 else "forward")
            for number in numbers:
                if number in sub:
                    return str(numbers[number])
    return None


if __name__ == "__main__":
    f = open("input1.txt")
    numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    integers = []
    for line in f:
        line = line.strip()
        digits = []
        digits.append(findDigit(line, numbers, 0, len(line), 1))
        digits.append(findDigit(line, numbers, len(line)-1, -1, -1))
        integers.append(int("".join(digits)))
        print(line, " - ", integers[-1])
    f.close()
    print(sum(integers))