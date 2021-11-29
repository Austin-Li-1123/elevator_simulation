# simulation details
# all time units are in minutes
ITERATIONS = 2
SIMULATE_HOURS = 18 - 8
SIMULATE_TIME = SIMULATE_HOURS * 60

# objectives for incoming people
OBJECTIVE_DICT = {"class": 0,
                    "OH": 1,
                    "faculty": 2,
                    "others": 3}


# model details
NUM_FLOORS = 8
NUM_ELEVATORS = 3
ELEVATOR_CAPACITY = 4

ARRIVAL_STD = 2

FACULTY_WORK_START = "9:00"
FACULTY_WORK_END = "16:00"


# assumptions
RANDOM_PEOPLE_PER_MIN = 0.5
AVERAGE_STAY = 1.5
MEAN_STUDENT_PRE_OH = 8