import constants

class People:
    def __init__(self, objective, floor, arrival_time, leave_time) -> None:
        self.objective = objective
        self.floor = floor
        # 0: 8:00, 60: 9:00, ....
        self.arrival_time = arrival_time
        self.leave_time = leave_time
    
    def press_button(self, floor, elevator):
        elevator.respond_button(floor)

    def __str__(self) -> str:
        return f"arrive at {self.arrival_time}, leave at {self.leave_time}, floor {self.floor}"


class Elevator:
    def __init__(self) -> None:
        self.pressed_buttons = []
        self.curr_floor = 1
        self.curr_load = 0
        self.capacity = constants.ELEVATOR_CAPACITY
        self.is_moving = False

    def respond_button(self, floor):
        self.pressed_buttons.append(floor)
