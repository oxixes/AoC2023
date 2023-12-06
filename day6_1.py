from math import ceil

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")

    # PART 1
    times = [int(num) for num in lines[0].split(":")[1].strip().split()]
    distances = [int(num) for num in lines[1].split(":")[1].strip().split()]

    # We need to solve the equation x(t - x) = d
    # x^2 - tx + d = 0
    # and find BOTH solutions

    # We use the quadratic formula

    result = 1
    for i in range(len(times)):
        a = 1
        b = -times[i]
        c = distances[i]

        # We find the discriminant
        discriminant = b * b - 4 * a * c

        # We find the solutions
        solution1 = (-b + discriminant ** 0.5) / (2 * a)
        solution2 = (-b - discriminant ** 0.5) / (2 * a)

        min = solution1 if solution1 < solution2 else solution2
        max = solution1 if solution1 > solution2 else solution2

        # We need to find the number of integers between min and max (not including min and max)
        mult = ceil(max) - ceil(min)
        if ceil(min) == min or ceil(max) == max:
            mult -= 1

        result *= mult

    print(result)

if __name__ == "__main__":
    main()