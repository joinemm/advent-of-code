def part1(input: str):
    seeds, rest = input.split("\n\n", 1)
    seeds = [int(x) for x in seeds.split(":", 1)[1].split()]

    layers = [
        sorted(
            [[int(x) for x in line.split()] for line in category.split("\n")[1:]],
            key=lambda x: x[1],
            reverse=True,
        )
        for category in rest.split("\n\n")
    ]

    locations = set()
    for seed in seeds:
        for layer in layers:
            for dest_start, source_start, m in layer:
                end = source_start + m
                if source_start <= seed < end:
                    diff = dest_start - source_start
                    seed += diff
                    break

        locations.add(seed)

    return min(locations)


def part2(input: str):
    seeds, rest = input.split("\n\n", 1)
    seed_iterator = iter(int(x) for x in seeds.split(":", 1)[1].split())
    seeds = list(sorted(zip(seed_iterator, seed_iterator)))

    layers = [
        sorted(
            [[int(x) for x in line.split()] for line in category.split("\n")[1:]],
            key=lambda x: x[1],
        )
        for category in rest.split("\n\n")
    ]

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
