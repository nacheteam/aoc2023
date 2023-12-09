import numpy as np
import time

def parseInput(file):
    sensors = []
    for line in file:
        sensor_line = line.strip().split(" ")
        sensor_line_int = [int(s) for s in sensor_line]
        sensors.append(sensor_line_int)
    return sensors

def predictNext(sensor):
    sequences = [sensor]
    curr_seq = sensor
    while np.count_nonzero(curr_seq)!=0:
        curr_seq = list(np.diff(curr_seq))
        sequences.append(curr_seq)
    for i in range(len(sequences)-1, -1, -1):
        if i==len(sequences)-1:
            sequences[i].append(0)
        else:
            sequences[i].append(sequences[i+1][-1] + sequences[i][-1])
    return sequences[0][-1]

def predictPrev(sensor):
    sequences = [sensor]
    curr_seq = sensor
    while np.count_nonzero(curr_seq)!=0:
        curr_seq = list(np.diff(curr_seq))
        sequences.append(curr_seq)
    for i in range(len(sequences)-1, -1, -1):
        if i==len(sequences)-1:
            sequences[i].insert(0,0)
        else:
            sequences[i].insert(0,sequences[i][0]-sequences[i+1][0])
    return sequences[0][0]

def solve(sensors):
    return sum([predictNext(sensor) for sensor in sensors])

def solve2(sensors):
    return sum([predictPrev(sensor) for sensor in sensors])

if __name__ == "__main__":
    file = open("input.txt", "r")
    sensors = parseInput(file)
    print(sensors)
    print(solve(sensors))
    print(solve2(sensors))