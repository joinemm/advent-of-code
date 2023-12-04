import unittest

from solution import part1, part2


def get_input(input_file):
    DAY = None
    with open(f"../../inputs/{DAY}/{input_file}") as file:
        return file.read().strip()


class Tests(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(
            part1(get_input("example")),
            None,
        )

    def test_part2_example(self):
        self.assertEqual(
            part2(get_input("example")),
            None,
        )

    def test_part1(self):
        self.assertEqual(
            part1(get_input("full")),
            None,
        )

    def test_part2(self):
        self.assertEqual(
            part2(get_input("full")),
            None,
        )


if __name__ == "__main__":
    unittest.main()
