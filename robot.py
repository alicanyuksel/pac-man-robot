import re


class B_VZXR:
    def __init__(self, instruction_file, universe_file) -> None:
        self.instruction_file = instruction_file
        self.universe_file = universe_file
        self.universe = ""

        self.instruction_list = []
        self.instruction_completed = []

        # universe
        self.width = ""
        self.height = ""

        # Robot's head:
        # UP = 1, RIGHT = 2, DOWN = 3, LEFT = 4

        self.robot_head = 1

        # robot location
        self.position_x, self.position_y = 0, 0

    def get_instruction(self):
        try:
            f = open(self.instruction_file, "r")
        except FileNotFoundError as error:
            print(error)
        else:
            # convert string into char
            self.instruction_list = [char for char in f.readline()]

    def read_instruction(self):
        for instruction in self.instruction_list:
            if instruction != "r":
                self.execute_instruction_function(instruction)
            else:
                last_instruction = self.instruction_completed[-1]
                self.execute_instruction_function(last_instruction)

    def execute_instruction_function(self, instruction):
        if instruction == "F":
            self.move(instruction)
        elif instruction == "R":
            self.turn_right(instruction)
        elif instruction == "L":
            self.turn_left(instruction)

    def add_instruction_completed(self, instruction):
        self.instruction_completed.append(instruction)

    def get_universe(self):
        try:
            f = open(self.universe_file, "r")
        except FileNotFoundError as error:
            print(error)
        else:
            # convert string into char
            self.universe = f.read().replace("\n", "")
            self.width, self.height = re.findall(r'\d+', self.universe)

    def get_location(self):
        #final_position = (self.position_x, self.position_y)
        #print(f"Final position : {final_position}")
        return (self.position_x, self.position_y)

    def turn_right(self, instruction):
        self.add_instruction_completed(instruction)
        if self.robot_head != 4:
            self.robot_head += 1
        else:
            self.robot_head = 1

    def turn_left(self, instruction):
        self.add_instruction_completed(instruction)
        if self.robot_head != 1:
            self.robot_head -= 1
        else:
            self.robot_head = 4

    def move(self, instruction):
        self.add_instruction_completed(instruction)

        if self.robot_head == 1:
            if self.position_y == int(self.height) - 1:
                pass
            else:
                self.position_y += 1

        elif self.robot_head == 3:
            if self.position_y == 0:
                pass
            else:
                self.position_y -= 1

        elif self.robot_head == 2:
            if self.position_x == int(self.width) - 1:
                pass
            else:
                self.position_x += 1

        elif self.robot_head == 4:
            if self.position_x == 0:
                pass
            else:
                self.position_x -= 1
