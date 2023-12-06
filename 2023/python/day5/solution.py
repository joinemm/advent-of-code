import time


def part1(input: str):
    seeds, rest = input.split("\n\n", 1)
    seeds = [int(x) for x in seeds.split(":", 1)[1].split()]
    sieves = []
    for category in rest.split("\n\n"):
        lines = category.split("\n")
        ranges = []
        for line in lines[1:]:
            ranges.append([int(x) for x in line.split()])
        sieves.append(sorted(ranges, key=lambda r: r[1], reverse=True))

    locations = set()

    for seed in seeds:
        for sieve in sieves:
            i = 0
            while i < len(sieve) - 1 and sieve[i][1] > seed:
                i += 1
            if (sieve[i][1] + sieve[i][2]) > seed >= sieve[i][1]:
                diff = seed - sieve[i][1]
                result = sieve[i][0] + diff
            else:
                result = seed
            seed = result
        locations.add(seed)

    return min(locations)


def part2(input: str):
    seeds, rest = input.split("\n\n", 1)
    seed_iterator = iter(int(x) for x in seeds.split(":", 1)[1].split())
    seeds = list(sorted(zip(seed_iterator, seed_iterator)))

    layers = []
    for category in rest.split("\n\n"):
        layers.append(
            sorted(
                [[int(x) for x in line.split()] for line in category.split("\n")[1:]],
                key=lambda x: x[1],
            )
        )

    for layer in layers:
        new_seeds = []
        for i, n in seeds:
            while n > 0:
                for dest_start, source_start, m in layer:
                    end = source_start + m
                    if source_start <= i < end:
                        used = min(i + n, end) - i
                        new_seeds.append([i + dest_start - source_start, used])
                        n -= used
                        i += used
                        break
                else:
                    new_seeds.append([i, n])
                    n = 0

        seeds = new_seeds

    return min(s[0] for s in seeds)
