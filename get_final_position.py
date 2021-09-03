from robot import B_VZXR

instruction_file = "./instruction_list.txt"
universe_file = "./universe.txt"


def main():
    robot = B_VZXR(instruction_file=instruction_file,
                   universe_file=universe_file)
    robot.get_instruction()
    robot.get_universe()
    robot.read_instruction()
    final_position = robot.get_location()
    print(final_position)


if __name__ == "__main__":
    main()
