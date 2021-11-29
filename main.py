from matplotlib.collections import BrokenBarHCollection
import constants
import classes
import utility
import visualization
from collections import Counter

#TODO:
'''
1. capacity <- COVID
2. include waiting time in request
3. output distribution of wait time
4. plot 3 on different models
'''

def simulation(weekday):
    request_queue = []
    starvation = []
    time_span = constants.SIMULATE_TIME

    # generate people incoming time for time span
    # the var below have type: list(People)
    student_class = utility.generate_student_class(weekday)
    student_OH = utility.generate_student_OH(weekday)
    faculties = utility.generate_faculty()
    people_random = utility.generate_people_random()

    # combine and plot arrivals
    print(f"{len(student_class)+len(student_OH)+len(faculties)+len(people_random)} people in the system")
    all_people = student_class + student_OH + faculties + people_random
#    visualization.visualize_people(people_list=all_people)

    # sort all people by arrival time
    people_sorted_start = all_people.copy()
    people_sorted_start.sort(key=lambda x: x.arrival_time)

    people_sorted_leave = all_people.copy()
    people_sorted_leave.sort(key=lambda x: x.leave_time)

    # initialize elevators
    all_elevators = utility.initialize_elevators(count=constants.NUM_ELEVATORS)

    # start simulation
    seconds_passed = 0
    curr_ptr_start = 0
    curr_ptr_end = 0

    k_range = 6

    # print("----- Start timer -----")
    for min in range(constants.SIMULATE_TIME):
        for k in range(k_range):
            clock_time = min*60 + k*(60/k_range)

            elevator_locations = []
            # update elevator positions
            for elevator in all_elevators:
                # if e is openning door, skip this time slot
                if elevator.is_door_open:
                    elevator.is_door_open = False
                    continue

                if elevator.target_floors != []:
                    # having target floors means is moving
                    # move 1 floor in its direction
                    if elevator.up_direction != None:
                        if elevator.up_direction:
                            elevator.curr_floor += 1
                        else:
                            elevator.curr_floor -= 1

                        elevator_locations.append(elevator.curr_floor)
                        # check if target floor, and remove if so
                        if elevator.curr_floor in elevator.target_floors:
                            elevator.is_door_open
                            elevator.target_floors.remove(elevator.curr_floor)
                        
                            # update capacity

                            # TODO: ignore request if at capacity
                            # pick up request at floor, if any
                            # remove that request
                            for i, request in enumerate(request_queue):
                                if request.from_ == elevator.curr_floor:
                                    # delete i from queue
                                    req = request_queue.pop(i)
                                    starvation.append(clock_time - req.start_time)
                                    # add target floors to e
                                    for target in req.to:
                                        if target not in elevator.target_floors:
                                            elevator.target_floors.append(target)
                                    # TODO: increase curr_load


                        # if elevator is done with work, continue
                        if elevator.target_floors == []:
                            continue

                        utility.set_elevator_direction(elevator)
                    # set elevator directions
                    # the order of the targets is also priority
                    utility.set_elevator_direction(elevator)
                    
            # people to arrive
            curr_time = min + k * 0.25
            l = curr_ptr_end
            r = l

            # get r 
            for i in range(l, len(people_sorted_start)):
                if people_sorted_start[i].arrival_time >= curr_time:
                    r = i
                    break
            # assign an elevator for them
            if l != r:
                target_floors = set()
                for i in range(l, r):
                    target_floors.add(people_sorted_start[i].floor)
                # push to requset queue
                new_requset = classes.Request(from_=0, to=list(target_floors), start_time=clock_time)
                request_queue.append(new_requset)

            # people to leave
            l = curr_ptr_start
            r = l
            # get r 
            for i in range(l, len(people_sorted_leave)):
                if people_sorted_leave[i].leave_time >= curr_time:
                    r = i
                    break
            # assign an elevator for them
            if l != r:
                from_floors = set()
                for i in range(l, r):
                    from_floors.add(people_sorted_leave[i].floor)

                # push to requset queue
                for from_ in from_floors:
                    new_requset = classes.Request(from_=from_, to=[0], start_time=clock_time)
                    request_queue.append(new_requset)
            
            # request queue to elevators
            for request in request_queue:
                least_e_index = utility.find_least_tasked_e(all_elevators)
                # insert request.from_ to that e
                e = all_elevators[least_e_index]
                if request.from_ not in e.target_floors:
                    e.target_floors.append(request.from_)


            seconds_passed += 10

    counts = Counter(starvation)
    return counts




def main():
    for _ in range(constants.ITERATIONS):
        # weekday: 0:monday, ... , 6:sunday
        starvation = simulation(weekday=0)
        visualization.plot_starvation(starvation)


if __name__ == "__main__":
    main()











