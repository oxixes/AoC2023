def get_value_after_maps(seed, maps):
    for map in maps:
        mapping = None
        for data in map:
            if seed >= data[1] and seed < data[1] + data[2]:
                mapping = data
                break
        if mapping != None:
            seed = mapping[0] + seed - mapping[1]

    return seed

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    # PART 1
    parts = txt.replace("\r", "").split("\n\n")
    seeds = [int(num) for num in parts[0].split(": ")[1].split(" ")]

    maps = [[(int(data.split(" ")[0]), int(data.split(" ")[1]), int(data.split(" ")[2])) for data in part.split(":\n")[1].split("\n")] for part in parts[1:]]

    result = get_value_after_maps(seeds[0], maps)
    for seed in seeds[1:]:
        val = get_value_after_maps(seed, maps)
        if val < result:
            result = val

    print(result)

if __name__ == '__main__':
    main()