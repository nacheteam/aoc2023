def parseInput(file):
    times, distances = [], []
    for line in file:
        cleaned = line.strip()
        if "Time" in cleaned:
            times_numbers = cleaned.split(": ")[1].split(" ")
            for time in times_numbers:
                if time != "":
                    times.append(int(time))
        elif "Distance" in cleaned:
            distances_numbers = cleaned.split(": ")[1].split(" ")
            for distance in distances_numbers:
                if distance != "":
                    distances.append(int(distance))
    return times, distances

def joinRaces(times, distances):
    # Join times by appending digits
    times_str = [str(t) for t in times]
    time = int("".join(times_str))
    # Join distances by appending digits
    distances_str = [str(d) for d in distances]
    distance = int("".join(distances_str))
    return time, distance

def waysToBeatRecord(time, record_distance):
    ways = 0
    for time_holded in range(time+1):
        speed = time_holded
        remaining_time = time - time_holded
        distance = speed * remaining_time
        if distance > record_distance:
            ways += 1
    return ways

def computeAllWays(times, distances):
    all_ways = []
    for i in range(len(times)):
        all_ways.append(waysToBeatRecord(times[i], distances[i]))
    return all_ways

if __name__ == "__main__":
    file = open("input.txt", "r")
    times, distances_record = parseInput(file)
    print(times, distances_record)
    all_ways = computeAllWays(times, distances_record)
    multiplication = 1
    for ways in all_ways:
        multiplication *= ways
    print(multiplication)
    joined_time, joined_distance = joinRaces(times, distances_record)
    print(joined_time, joined_distance)
    all_ways = waysToBeatRecord(joined_time, joined_distance)
    print(all_ways)
    file.close()