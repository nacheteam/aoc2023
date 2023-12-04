def parseInput(file):
    input_matrix = []
    with open(file) as f:
        for line in f:
            input_matrix.append(line.strip())
    return input_matrix

def getAdjacentNumbers(matrix, i, j):
    adjacent_numbers = []
    for x in range(max(0, i-1), min(i+2, len(matrix))):
        for y in range(max(0, j-1), min(j+2, len(matrix[0]))):
            if matrix[x][y].isdigit():
                begin = y
                end = y
                while begin >= 0 and matrix[x][begin].isdigit():
                    begin -= 1
                while end < len(matrix) and matrix[x][end].isdigit():
                    end += 1
                if not int(matrix[x][begin+1:end]) in adjacent_numbers:
                    adjacent_numbers.append(int(matrix[x][begin+1:end]))
    return adjacent_numbers

def solve1(matrix):
    all_adjacents = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!="." and not matrix[i][j].isdigit():
                adjacents = getAdjacentNumbers(matrix, i, j)
                all_adjacents = all_adjacents + adjacents
    return sum(all_adjacents)

def solve2(matrix):
    gear_ratios = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=="*" and not matrix[i][j].isdigit():
                adjacents = getAdjacentNumbers(matrix, i, j)
                if len(adjacents)==2:
                    gear_ratios.append(adjacents[0]*adjacents[1])
    return sum(gear_ratios)

if __name__ == "__main__":
    matrix = parseInput("input1.txt")
    print(solve1(matrix))
    print(solve2(matrix))