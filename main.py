import constants
import classes
import utility
import visualization

def simulation(weekday):
    time_span = constants.SIMULATE_TIME

    # generate people incoming time for time span
    # the var below have type: list(People)
    student_class = utility.generate_student_class(weekday)
    student_OH = utility.generate_student_OH(weekday)
    faculties = utility.generate_faculty()
    people_random = utility.generate_people_random()

    # combine and plot arrivals
    print(f"{len(student_class)+len(student_OH)+len(faculties)+len(people_random)} people in the system")
    all_people = student_class + student_OH + faculties
    #visualization.visualize_people(people_list=all_people)

    # initialize elevators
    





def main():
    for _ in range(constants.ITERATIONS):
        # weekday: 0:monday, ... , 6:sunday
        simulation(weekday=0)


if __name__ == "__main__":
    main()











