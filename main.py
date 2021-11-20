import constants
import classes
import utility

def simulation(weekday):
    time_span = constants.SIMULATE_TIME

    # generate people incoming time for time span
    # the var below have type: list(People)
    student_class = utility.generate_student_class(weekday)
    student_OH = utility.generate_student_OH(weekday)
    faculties = utility.generate_faculty(weekday)
    people_random = utility.generate_people_random(weekday)

    # combine and plot arrivals

    
    # initialize elevators
    





def main():
    for _ in range(constants.ITERATIONS):
        # weekday: 0:monday, ... , 6:sunday
        simulation(weekday=0)


if __name__ == "__main__":
    main()











