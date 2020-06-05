from dynamic import *
from Greedy import *
import numpy as np
import time

def measure_time(function, capacity: int, weight: list, values: list):
    start = time.clock()
    result = function(capacity, weight, values)
    end = time.clock()
    duration = end - start
    return (duration, result)

def export_data_to_file(filename: str, data: float):
    file = open(filename,"a")
    file.write("{0:02f}\n".format(data))
    file.close()
    return 0

def mainConstC():
    filename = "data/constC"       # C – capacity, N – number of items
    probes = 3
    capacity = 600
    maxw = 100
    maxv = 100
    for n in range(10, 1000, 10):
        time_gre = 0
        time_dyn = 0
        error = 0
        for p in range(probes):
            weights = np.random.randint(maxw, size=n)
            values = np.random.randint(maxv, size=n)

            time, result_dyn = measure_time(mainDynamic, capacity, weights, values)
            time_dyn += time
            time, result_gre = measure_time(greedy,capacity,weights,values)
            time_gre += time

            error += (result_dyn[0]-result_gre[0])/result_dyn[0]
            print(n)
        export_data_to_file(filename+"_time_dyn", time_dyn/probes)
        export_data_to_file(filename+"_time_gre", time_gre/probes)
        export_data_to_file(filename+"_error", error/probes)
    return 0

def mainConstN():
    filename = "data/constN"
    probes = 3
    n = 100
    maxw = 100
    maxv = 100
    for capacity in range(800, 2500, 100):
        time_dyn = 0
        time_gre = 0
        error = 0
        for p in range(probes):
            weights = np.random.randint(maxw, size=n)
            values = np.random.randint(maxv, size=n)

            time, result_dyn = measure_time(mainDynamic, capacity, weights, values)
            time_dyn += time
            time, result_gre = measure_time(greedy,capacity,weights,values)
            time_gre += time

            error += (result_dyn[0]-result_gre[0])/result_dyn[0]
            print(capacity)
        export_data_to_file(filename+"_time_dyn", time_dyn/probes)
        export_data_to_file(filename+"_time_gre", time_gre/probes)
        export_data_to_file(filename+"_error", error/probes)
    return 0

if __name__ == '__main__':
    mainConstN()
