def join_ranges(ranges):
    # We sort the ranges by their start value
    ranges.sort(key=lambda x: x[0])

    # We join the ranges
    new_ranges = []
    prev_range = None
    for range in ranges:
        if prev_range == None:
            prev_range = range
            continue

        if prev_range[0] + prev_range[1] > range[0]:
            prev_range = (prev_range[0], max(prev_range[0] + prev_range[1], range[0] + range[1]) - prev_range[0])
        else:
            new_ranges.append(prev_range)
            prev_range = range

    if prev_range != None:
        new_ranges.append(prev_range)

    return new_ranges

def apply_maps_to_range(seed_range, maps):
    new_seed_ranges = []
    remaining_range = seed_range
    while remaining_range:
        mapping = None
        for data in maps[0]:
            if remaining_range[0] >= data[1] and remaining_range[0] < data[1] + data[2]:
                mapping = data
                break

        if mapping == None:
            # We check if some of the remaining range is part of a map
            for data in maps[0]:
                if remaining_range[0] + remaining_range[1] > data[1] and remaining_range[0] + remaining_range[1] <= data[1] + data[2]:
                    mapping = data
                    break

            if mapping == None:
                new_seed_ranges.append(remaining_range)
                remaining_range = None
                break
            else:
                new_seed_ranges.append((remaining_range[0], mapping[1] - remaining_range[0]))
                remaining_range = (remaining_range[0] + mapping[1] - remaining_range[0], remaining_range[1] - mapping[1] + remaining_range[0])
                continue

        # We apply the mapping to the range, but the range may be split into two ranges
        # if the mapping is not applied to the entire range (i.e. the mapping is not long enough)
        if mapping[1] + mapping[2] > remaining_range[0] + remaining_range[1]:
            new_seed_ranges.append((mapping[0] + remaining_range[0] - mapping[1], remaining_range[1]))
            remaining_range = None
        else:
            mapped_length = mapping[1] + mapping[2] - remaining_range[0] - 1
            new_seed_ranges.append((mapping[0] + remaining_range[0] - mapping[1], mapped_length))
            remaining_range = (mapping[1] + mapping[2], remaining_range[0] + remaining_range[1] - mapping[1] - mapping[2] + 1)

    new_seed_ranges = join_ranges(new_seed_ranges)
    maps = maps[1:]

    if len(maps) == 0:
        return new_seed_ranges
    else:
        result = []
        for seed_range in new_seed_ranges:
            result += apply_maps_to_range(seed_range, maps)
        return result

def find_smallest_value(seed_ranges):
    smallest_value = None
    for seed_range in seed_ranges:
        if smallest_value == None or seed_range[0] < smallest_value:
            smallest_value = seed_range[0]
    return smallest_value

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    # PART 2
    parts = txt.replace("\r", "").split("\n\n")
    seeds = [int(num) for num in parts[0].split(": ")[1].split(" ")]
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    maps = [[(int(data.split(" ")[0]), int(data.split(" ")[1]), int(data.split(" ")[2])) for data in part.split(":\n")[1].split("\n")] for part in parts[1:]]

    min = find_smallest_value(apply_maps_to_range(seed_ranges[0], maps))
    for seed_range in seed_ranges[1:]:
        val = find_smallest_value(apply_maps_to_range(seed_range, maps))
        if val < min:
            min = val

    print(min)

if __name__ == '__main__':
    main()