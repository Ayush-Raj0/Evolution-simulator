import csv
import matplotlib.pyplot as plot

times = []
populations = []
average_speeds = []

stats_filename = input("Enter the CSV filename to plot = ").strip()
run_name = stats_filename.removesuffix(".csv")

with open(stats_filename, "r", newline ="") as stats_file:
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
plot.savefig(run_name + "population_over_time.png", dpi=150, bbox_inches="tight")

plot.figure()
plot.plot(times, average_speeds)
plot.xlabel("Elapsed time(seconds)")
plot.ylabel("Average speed(pixels per frame)")
plot.title("Average Speed over Time")
plot.savefig(run_name + "Average_speed_over_time.png", dpi=150, bbox_inches="tight")

plot.show()