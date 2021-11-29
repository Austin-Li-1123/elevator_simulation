import numpy as np
import constants
import class_schedule
import OH_schedule
import classes
import faculty_floors

def convert_time(time_str):
    hour, min = time_str.split(":")
    hour, min = int(hour), int(min)

    time_val = (hour-8) * 60 + min
    return time_val

def generate_normal_distribution(mean, count):
    std = constants.ARRIVAL_STD
    return np.random.normal(mean, std, count)

def generate_student_class(weekday):
    people_list = []

    if weekday == 0:
        # [(start, end, count, floor)]
        schedule = class_schedule.MONDAY_CLASS

    for class_ in schedule:
        start_time = convert_time(class_[0])
        end_time = convert_time(class_[1])
        num_student = class_[2]
        arrival_times = generate_normal_distribution(mean=start_time, count=num_student)
        leave_times = generate_normal_distribution(mean=end_time, count=num_student)

        # initalize student objects
        for i in range(num_student):
            new_person = classes.People(objective=constants.OBJECTIVE_DICT["class"], 
                        floor=class_[3], arrival_time=arrival_times[i], leave_time=leave_times[i])
            people_list.append(new_person)

    return people_list

def generate_student_OH(weekday):
    people_list = []
    if weekday == 0:
        # [(start, end, average, floor)]
        schedule = OH_schedule.MONDAY_OH

    for time_ in schedule:
        start_time = convert_time(time_[0])
        end_time = convert_time(time_[1])
        num_student = time_[2]
        arrival_times = generate_normal_distribution(mean=start_time, count=num_student)
        leave_times = generate_normal_distribution(mean=end_time, count=num_student)

        # initalize student objects
        for i in range(num_student):
            new_person = classes.People(objective=constants.OBJECTIVE_DICT["OH"], 
                        floor=2, arrival_time=arrival_times[i], leave_time=leave_times[i])
            people_list.append(new_person)

    return people_list


def generate_faculty():
    people_list = []

    for floor in range(constants.NUM_FLOORS):
        num_faculty = faculty_floors.floor_to_count[floor]
        start_time = convert_time(constants.FACULTY_WORK_START)
        end_time = convert_time(constants.FACULTY_WORK_END)

        arrival_times = generate_normal_distribution(mean=start_time, count=num_faculty)
        leave_times = generate_normal_distribution(mean=end_time, count=num_faculty)

        for i in range(num_faculty):
            new_person = classes.People(objective=constants.OBJECTIVE_DICT["faculty"], 
                            floor=floor, arrival_time=arrival_times[i], leave_time=leave_times[i])
            people_list.append(new_person)

    return people_list

def get_random_floor():
    random_float = np.random.random()
    if random_float <= 0.075:
        return 0
    if random_float <= 0.2:
        return 1
    if random_float <= 0.415:
        return 2
    if random_float <= 0.515:
        return 3
    if random_float <= 0.765:
        return 4
    if random_float <= 0.965:
        return 5
    if random_float <= 0.99:
        return 6
    return 7


def generate_people_random():
    people_list = []

    people_per_minute = constants.RANDOM_PEOPLE_PER_MIN
    output = np.random.poisson(people_per_minute, constants.SIMULATE_TIME)
    
    for i, num in enumerate(output):
        for j in range(num):
            floor = get_random_floor()
            leave_time = i + np.random.normal(constants.AVERAGE_STAY, 1)
            new_person = classes.People(objective=constants.OBJECTIVE_DICT["others"], 
                            floor=floor, arrival_time=i, leave_time=leave_time)
            people_list.append(new_person)
    

    return people_list

def initialize_elevators(count):
    elevators = []

    for i in range(count):
        elevators.append(classes.Elevator())

    return elevators

# the order of the targets is also priority
def set_elevator_direction(elevator_obj):
    if elevator_obj.target_floors[0] > elevator_obj.curr_floor:
        # move upward
        elevator_obj.up_direction = True
    else:
        elevator_obj.up_direction = False


def find_least_tasked_e(all_elevators):
    min_elevator = 0
    for i, e in enumerate(all_elevators):
        if len(e.target_floors) < len(all_elevators[min_elevator].target_floors):
            min_elevator = i

    return min_elevator