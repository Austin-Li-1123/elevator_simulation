import matplotlib.pyplot as plt

def visualize_people(people_list):
    arrival_times = [people.arrival_time for people in people_list]
    leave_times = [people.leave_time for people in people_list] 
    floors = [people.floor for people in people_list]

    plt.scatter(arrival_times, floors)
    # plt.scatter(leave_times, floors)
    plt.show()
    
