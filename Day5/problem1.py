from functools import partial
from multiprocessing import Pool

def parseInput(file):
    to_translator = {}
    maps = {}
    seeds = []
    last_dest = ""
    current_source = ""
    current_dest = ""
    for line in file:
        line = line.strip()
        if "seeds" in line and len(seeds) == 0:
            s = line.split(": ")[1].split(" ")
            seeds = [int(x) for x in s]
        elif "-to-" in line:
            source = line.split("-to-")[0].strip()
            dest = line.split("-to-")[1].strip().split(" ")[0]
            to_translator[source] = dest
            current_source = source
            current_dest = dest
            last_dest = dest
        elif line == "":
            continue
        else:
            numbers = line.split(" ") # 3 numbers destination start, source start, range len
            numbers_tuple = (int(numbers[0]), int(numbers[1]), int(numbers[2]))
            if current_dest not in maps.keys():
                maps[current_dest] = [numbers_tuple]
            else:
                maps[current_dest].append(numbers_tuple)
    to_translator[last_dest] = "end"
    return to_translator, maps, seeds

def translate(to_translator, maps, seeds):
    init_to_end = {}
    for s in seeds:
        init_to_end[s] = s
        current = to_translator["seed"]
        while current != "end":
            converters = maps[current]
            for converter in converters:
                if converter[1] <= init_to_end[s] <= converter[1] + converter[2]:
                    init_to_end[s] = converter[0] + init_to_end[s] - converter[1]
                    break
            current = to_translator[current]
    return init_to_end

def computeFinalPos(s, to_translator, maps):
    final_pos = s
    current = to_translator["seed"]
    while current != "end":
        converters = maps[current]
        for converter in converters:
            if converter[1] <= final_pos <= converter[1] + converter[2]:
                final_pos = converter[0] + final_pos - converter[1]
                break
        current = to_translator[current]
    return final_pos


def translate2(to_translator, maps, seeds):
    min_seed = float("inf")
    for i in range(0,len(seeds),2):
        print(i, len(seeds))
        seeds_range = range(seeds[i], seeds[i]+seeds[i+1])
        for s in seeds_range:
            final_pos = computeFinalPos(s, to_translator, maps)
            if final_pos < min_seed:
                min_seed = final_pos
    return min_seed

def getMin(init_to_end):
    min = float("inf")
    for key in init_to_end:
        if init_to_end[key] < min:
            min = init_to_end[key]
    return min

if __name__ == "__main__":
    with open("input.txt") as f:
        to_translator, maps, seeds = parseInput(f)
        init_to_end = translate(to_translator, maps, seeds)
        print(getMin(init_to_end))
        min_seed = translate2(to_translator, maps, seeds)
        print(min_seed)