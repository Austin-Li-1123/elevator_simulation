import numpy as np
import constants
import class_schedule
import classes

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

print(generate_student_class(0)[0])