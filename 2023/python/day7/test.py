import unittest

from solution import part1, part2


def get_input(input_file):
    DAY = 7
    with open(f"../../inputs/{DAY}/{input_file}") as file:
        return file.read().strip()


class Tests(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(
            part1(get_input("example")),
            6440,
        )

    def test_part2_example(self):
        self.assertEqual(
            part2(get_input("example")),
            5905,
        )

    def test_part1(self):
        self.assertEqual(
            part1(get_input("full")),
            248422077,
        )

    def test_part2(self):
        self.assertEqual(
            part2(get_input("full")),
            249817836,
        )


if __name__ == "__main__":
    unittest.main()
