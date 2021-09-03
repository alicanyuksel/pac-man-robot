import unittest
from robot import B_VZXR

instruction_test_file = "./test/instruction_test.txt"
universe_test_file = "./test/universe_test.txt"


class TestRobot(unittest.TestCase):
    def test_simple(self):
        robot = B_VZXR(instruction_file=instruction_test_file,
                       universe_file=universe_test_file)
        robot.get_instruction()
        robot.get_universe()
        robot.read_instruction()
        final_position = robot.get_location()
        
        self.assertEqual(final_position, (0, 3))


if __name__ == '__main__':
    unittest.main()
