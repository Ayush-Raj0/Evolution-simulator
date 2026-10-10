import csv
import matplotlib.pyplot as plot

times = []
populations = []
average_speeds = []
average_sensing_ranges = []

stats_filename = input("Enter the CSV filename to plot = ").strip()
run_name = stats_filename.removesuffix(".csv")

with open(stats_filename, "r", newline ="") as stats_file:
    reader = csv.reader(stats_file)
    next(reader)

    for row in reader:
        times.append(float(row[0]))
        populations.append(int(row[1]))
        average_speeds.append(float(row[2]))
        if len(row)>3:
            average_sensing_ranges.append(float(row[3]))

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
plot.savefig(run_name + "average_speed_over_time.png", dpi=150, bbox_inches="tight")

if average_sensing_ranges:
    plot.figure()
    plot.plot(times, average_sensing_ranges)
    plot.xlabel("Elapsed time(seconds)")
    plot.ylabel("Average sensing range(pixels)")
    plot.title("Average sensing range over time")
    plot.savefig(run_name + "average_sensing_range_over_time.png", dpi=150, bbox_inches="tight")

plot.show()