import csv
import matplotlib.pyplot as plot

times = []
populations = []
average_speeds = []

with open("simulation_stats.csv", "r", newline ="") as stats_file:
    reader = csv.reader(stats_file)
    next(reader)

    for row in reader:
        times.append(float(row[0]))
        populations.append(int(row[1]))
        average_speeds.append(float(row[2]))

plot.figure()
plot.plot(times, populations)
plot.xlabel("Elapsed time(seconds)")
plot.ylabel("Living populations")
plot.title("Population over time")
plot.savefig("population_over_time.png", dpi=150, bbox_inches="tight")

plot.figure()
plot.plot(times, average_speeds)
plot.xlabel("Elapsed time(seconds)")
plot.ylabel("Average speed(pixels per frame)")
plot.title("Average Speed over Time")
plot.savefig("Average_speed_over_time.png", dpi=150, bbox_inches="tight")


plot.show()