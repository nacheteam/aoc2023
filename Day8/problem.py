import math

def parseInput(file):
    first_line = True
    movements = []
    nodes = {}
    for line in file:
        if line=="\n":
            continue
        else:
            if first_line:
                first_line = False
                movements = [*line.strip()]
            else:
                key = line.split(" = ")[0]
                left_node = line.split(" = ")[1].split(", ")[0][1:]
                right_node = line.split(" = ")[1].split(", ")[1][:-2] if "\n" in line else line.split(" = ")[1].split(", ")[1][:-1]
                nodes[key] = [left_node, right_node]

    return movements, nodes

def solve(movements, nodes, current_node="AAA", end_node="ZZZ"):
    current_node = current_node
    cont_movements = 0
    steps = 0
    condition = current_node!=end_node if end_node=="ZZZ" else current_node[-1]!=end_node[-1]
    while condition:
        if movements[cont_movements]=="L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        cont_movements = cont_movements+1 if cont_movements<len(movements)-1 else 0
        steps+=1
        condition = current_node!=end_node if end_node=="ZZZ" else current_node[-1]!=end_node[-1]
    return steps

def allNodesAtEnd(nodes):
    for n in nodes:
        if n[-1]!="Z":
            return False
    return True

def solve2(movements, nodes):
    current_nodes = []
    for key in nodes.keys():
        if key[-1]=="A":
            current_nodes.append(key)
    print("Starting nodes: ", current_nodes)
    steps = []
    for node in current_nodes:
        steps.append(solve(movements, nodes, node, "Z"))
    return math.lcm(*steps)

if __name__ == "__main__":
    file = open("input.txt", "r")
    movements, nodes = parseInput(file)
    #print(movements)
    #print(nodes)
    #print(solve(movements, nodes))
    print(solve2(movements, nodes))