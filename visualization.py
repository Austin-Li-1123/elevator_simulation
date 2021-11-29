import matplotlib.pyplot as plt
import numpy as np

def visualize_people(people_list):
    arrival_times = [people.arrival_time for people in people_list]
    leave_times = [people.leave_time for people in people_list] 
    floors = [people.floor for people in people_list]

    plt.scatter(arrival_times, floors)
    # plt.scatter(leave_times, floors)
    plt.show()
    

def plot_starvation(starvation):
    y_val = np.array(starvation.values()) / sum(starvation.values())
    plt.bar(starvation.keys(), y_val)
    plt.xlabel("Wait time(sec)")
    plt.ylabel("Frequency")
    plt.show()
