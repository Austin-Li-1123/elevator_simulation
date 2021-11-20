import constants

class People:
    def __init__(self, objective, floor, arrival_time) -> None:
        self.objective = objective
        self.floor = floor
        self.arrival_time = arrival_time
    
    def press_button(self, floor, elevator):
        elevator.respond_button(floor)



class Elevator:
    def __init__(self) -> None:
        self.pressed_buttons = []
        self.curr_floor = 1
        self.curr_load = 0
        self.capacity = constants.ELEVATOR_CAPACITY
        self.is_moving = False

    def respond_button(self, floor):
        self.pressed_buttons.append(floor)
