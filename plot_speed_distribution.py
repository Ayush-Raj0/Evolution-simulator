import csv
import matplotlib.pyplot as plot

speeds_by_time = {}
speed_filename = input("Enter the speeds CSV filename = ").strip()
run_name = speed_filename.removesuffix(".csv")

with open(speed_filename, "r", newline="") as speed_file:
    reader = csv.reader(speed_file)
    next(reader, None)

    for row in reader:
        sample_time = float(row[0])
        speed = float(row[1])

        if sample_time not in speeds_by_time:
            speeds_by_time[sample_time] = []

        speeds_by_time[sample_time].append(speed)

if not speeds_by_time:
    print("This file contains no recorded speed samples.")
    raise SystemExit

available_times = sorted(speeds_by_time)

print("Available sampling times:")
for sample_time in available_times:
    print(round(sample_time, 3))

requested_time = float(input("Enter the time to inspect in seconds: "))

selected_time = min(
    available_times,
    key=lambda sample_time: abs(sample_time - requested_time)
)
selected_speeds = speeds_by_time[selected_time]

print("Using sample at " + str(round(selected_time, 3)) + " seconds.")

plot.figure()
plot.hist(selected_speeds, bins=10, edgecolor="black")
plot.xlabel("Speed (pixels per frame)")
plot.ylabel("Number of organisms")
plot.title(
    "Speed distribution at "
    + str(round(selected_time, 3))
    + " seconds"
)

plot.savefig(
    run_name + "_speed_distribution_" + str(selected_time) + ".png",
    dpi=150,
    bbox_inches="tight"
)

plot.show()