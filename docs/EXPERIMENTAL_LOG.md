## 2 June 2026

Started development of the Evolution Simulator as a Python-based artificial ecosystem project using Pygame.

Confirmed the initial simulation was running correctly in Visual Studio Code. The first working version displayed multiple blue organisms moving randomly within the simulation window.

Added the first environmental resource system using static food particles distributed randomly throughout the simulation area. Food particles were represented visually as green circles while organisms remained blue.

---

## June–July 2026

Continued development of the basic simulation environment and organism behaviour.

Improved the random movement system and maintained boundary restrictions so organisms remained within the visible simulation area.

Developed the food system further so food existed as individual objects within the environment rather than only as visual elements.

Began structuring the interaction between organisms and food in preparation for collision detection and energy-based survival mechanics.

The project remained intentionally simple at this stage, with organisms moving randomly and food remaining stationary.

---

## 30 July 2026

Restarted active development after a break and reviewed the structure of the simulator.

Reorganised the project around object-oriented programming.

Created an `Organism` class so each organism could store its own position, speed and behaviour.

Moved organism movement and drawing logic into class methods instead of handling all organism behaviour directly in the main simulation loop.

Created a separate `Food` class to represent individual food particles with their own position and properties.

This refactor established a clearer structure for adding interaction, energy and later evolutionary behaviour.

---

## 31 July – 1 August 2026

Implemented organism-food collision detection.

Added distance-based collision checking between circular organisms and food particles using the difference between their x and y coordinates.

Used squared distance rather than calculating the actual square root, allowing collision detection to compare:

```text
distance² <= combined radius²
```

This determined whether an organism had physically reached a food particle.

Added food consumption behaviour so food particles are removed from the active food list when an organism collides with them.

Used copied lists during iteration to allow food particles to be safely removed without causing skipped elements or iteration errors.

---

## 2–3 August 2026

Added the first organism energy system.

Each organism was given a starting energy value when created.

Added an energy value to food particles so consuming food increases the organism's stored energy.

Implemented an `eat()` method within the `Organism` class to handle the transfer of food energy to the organism.

At this stage, organisms could move, encounter food and gain energy, but energy did not yet decrease automatically over time.

Reviewed the interaction between movement, collision detection, food removal and energy gain before adding energy depletion.

---

## 4 August 2026

Prepared the simulation for time-based energy depletion.

Introduced frame-time measurement using Pygame's clock system.

Used:

```python
dt = clock.tick(FPS)/1000
```

to calculate the elapsed time between frames in seconds.

This allowed future energy changes to depend on real elapsed time rather than the number of frames rendered.

The change prevents differences in frame rate from significantly changing the rate at which organisms lose energy.

---

## 5 August 2026

Implemented continuous energy depletion.

Added an `ENERGY_LOSS_RATE` constant and a `lose_energy(dt)` method to the `Organism` class.

Organism energy now decreases continuously according to elapsed real time.

Added organism death when energy reaches zero or below.

Dead organisms are removed from the active `organisms` list.

Used a copied organism list during iteration so organisms could be removed safely while the simulation loop continued running.

Added `continue` after organism removal so dead organisms do not continue through food interaction or drawing logic during the same frame.

Tested the energy and death system by temporarily removing food from the simulation. Organisms died after approximately the expected time based on their starting energy and energy-loss rate.

At this stage, the simulator contained the complete basic survival loop:

```text
movement
→ energy loss
→ food encounter
→ energy recovery
→ death
```

---

## Early–Mid August 2026

Reviewed and cleaned the simulator code after the basic survival systems were working.

Reorganised constants so organism-related and food-related settings were grouped together.

Reordered methods in the `Organism` class so behaviour followed a clearer sequence.

Simplified list creation for organisms and food using list comprehensions.

Improved indentation, spacing and general code consistency while keeping the existing structure and behaviour unchanged.

---

## 22 August 2026

Reviewed the project roadmap after another short break from development.

Confirmed that the basic simulation systems were working:

* random organism movement
* food generation
* collision detection
* food consumption
* energy recovery
* time-based energy depletion
* organism death
* safe removal of dead organisms

Identified reproduction, inheritance and mutation as the next major evolutionary systems to implement.

Also noted that movement and sensing would later need improvement because purely random movement would limit meaningful interaction with food.

---

## 28–30 August 2026

Implemented organism reproduction based on an energy threshold.

Added a fixed reproduction energy cost to the parent organism. New offspring are returned from the reproduction method and appended to the active organism list.

Changed offspring spawning so that new organisms appear near the parent rather than at a random location. Added boundary constraints to prevent offspring from spawning outside the simulation window.

Tested reproduction by temporarily increasing organism energy to verify the reproduction logic.

Observed that natural reproduction remains uncommon because the current random movement model produces a low food encounter rate.

Added basic inheritance of movement speed from parent to offspring.

Next step: introduce mutation to inherited speed while keeping speed within the defined minimum and maximum limits.


## 2 October 2026

Added speed mutation during reproduction. Previously, offspring inherited the parent’s speed exactly through `child.speed = self.speed`. Offspring now inherit the parent’s speed with a random variation between −0.2 and +0.2 using `random.uniform()`. The resulting speed is bounded by `MIN_SPEED` and `MAX_SPEED` using `max()` and `min()`.

Tested the change by printing parent and offspring speeds during reproduction. Observed a parent speed of 1.55 produce an offspring speed of 1.48, and a parent speed of 1.45 produce an offspring speed of 1.54. Both variations were within the mutation range, and the offspring speeds remained within the allowed limits.

Next step: Add food sensing so organisms can detect nearby food, then use this information to guide movement toward it.

## 3 October 2026

Added food sensing and seeking behaviour. Before, organisms moved randomly each frame and encountered food by chance. Organisms now search for the nearest food particle within `SENSING_RANGE`, currently set to 100 pixels. The `sense_food()` method compares squared distances and updates the selected target whenever a closer particle is found. It returns `None` if no food is within range.

Updated `move()` to accept the detected food as a target. When a target exists, the organism calculates the direction toward it and moves along that direction using its individual speed. Movement is limited to the remaining distance to prevent overshooting, and a zero-distance check avoids division by zero. Existing boundary limits remain in place.

Random movement is retained when no food is detected. Food seeking therefore replaces random movement while a target is available, allowing organisms to approach nearby food deliberately. Existing collision detection and food consumption handle eating when the organism reaches the particle.

Next step: Test target selection, movement toward food, and the return to random movement when no food is within sensing range.

## 4 October 2026

Added speed-dependent energy loss to introduce a metabolic trade-off between movement speed and survival. Previously, all organisms lost energy at the same constant rate. The `lose_energy()` method now calculates each organism’s energy loss rate by adding `self.speed * SPEED_ENERGY_COST` to the base `ENERGY_LOSS_RATE`. This rate is multiplied by `dt`, keeping energy depletion based on elapsed time.

Faster organisms can reach food more quickly, but now spend more energy per second. This gives inherited speed variation a consequence for survival: greater speed offers an advantage in food collection while also increasing the energy needed to stay alive.

- During testing, I temporarily increased the reproduction threshold to reduce population growth and adjusted food energy to make individual survival easier to observe. Tried different speed-cost values, including `SPEED_ENERGY_COST = 2`. Some organisms disappeared sooner than nearby organisms whose food availability changed at roughly the same time. This observation was consistent with the intended trade-off, although individual feeding histories also affect survival.

- Also added on-screen display stats showing the live population count and the average organism     speed.
Both values are recalculated for each frame after organisms have been updated, so they reflect births and deaths of any organism which happen in each frame. 
Added a check for an empty population, to prevent division by zero when calculating the average.

Used Pygame's font and rendering methods and `screen.blit()` to display the statistics in the top-left corner, with average speed rounded off to 2 decimal points. 
I confirmed that the display is updated during the simulation, and in during my test simulation, 
the speed fluctuated between 2.35 and 2.45 in the run.

- Added generation tracking to distinguish the starting organisms from their descendants. Each organism now has a `generation` attribute, initialized to 0. During reproduction, the child receives its parent’s generation number plus 1. The parent’s generation remains unchanged, since the number represents ancestry rather than the number of offspring produced.

Extended the on-screen statistics to show the highest generation currently alive. This value is recalculated each frame while summing organism speeds, using the same loop through the living population. Unlike the highest generation ever reached, this value can decrease if all organisms belonging to the highest living generation die. When the population becomes extinct, the current display returns to 0; handling that case more clearly remains a small improvement.

Next step: Record population size and speed statistics over time so that changes across the simulation can be examined beyond the current on-screen values.

## 8 October 2026

Added recording of population count and average organism speed over time. The simulation now accumulates elapsed time using `dt` and stores a sample approximately once per second. A separate recording timer retains the fractional time remaining after each interval. When the simulation window is closed normally, the collected samples are written to `simulation_stats.csv`, along with column headings. Each run currently replaces the previous CSV file.

Checked the exported data and confirmed that samples were recorded roughly one second apart. In one test, the population increased from 14 to 17 to 19 across the first three samples, while average speed changed slightly.

Created a separate `plot_stats.py` script that reads the CSV and uses Matplotlib to plot population versus elapsed time and average speed versus elapsed time. Both graphs open in separate windows and are also saved as PNG images. Resolved an initial import error by installing Matplotlib into the project’s virtual environment. Confirmed that both graph windows and image files were generated successfully.

Added the generated CSV and PNG filenames to `.gitignore` so routine simulation outputs remain local. Committed and pushed the statistics-recording code, plotting script, and ignore rules.

Also added `EXPERIMENTS.md` to outline the experiment question, settings, data collection, planned graphs, and method. Updated the README’s feature descriptions and added links to the roadmap, experiment plan, and development log.

Next step: Run repeated experiments with different food availability and speed energy costs, recording the settings and comparing the resulting population and speed trends.

## 9 October 2026 — Preserving Simulation Runs and Food Replenishment

Added timestamped filenames to the simulation's CSV exports so that new runs no longer overwrite previous results. Updated the plotting script to accept a chosen CSV filename and save its population and average-speed graphs with filenames corresponding to that run.

Added a separate settings CSV for each run, using the same timestamp as its statistics file. This records the simulation parameters alongside the results, making it easier to identify the conditions used when reviewing graphs later. Food energy is now defined through the FOOD_ENERGY_VALUE constant.

Implemented timed food replenishment. New food particles spawn at random positions at a configurable interval, provided the current food count is below MAX_FOOD_COUNT. The timer preserves leftover elapsed time between intervals. Testing confirmed that food continues to spawn and stops accumulating at the configured limit of 150 particles. Both replenishment settings are included in the settings export.

Updated the README and roadmap to reflect the completed features, while keeping experiment controls and further evolutionary analysis pending.

Next step: Extend the simulator with additional inherited traits and their associated trade-offs.

## 10 October 2026

Added sensing range as a second inherited trait alongside movement speed. Starting organisms retain a sensing range of 85 pixels, while offspring inherit their parent's range with a random mutation between -5 and +5 pixels. The resulting range is bounded between 30 and 150 pixels.

Introduced sensing-dependent energy loss, creating a trade-off between detecting food farther away and spending more energy to maintain that ability. Added average sensing range to the on-screen statistics, recorded it in the statistics CSV, and included the new sensing parameters in each run's settings export.

Extended the plotting script to generate an average sensing range graph alongside the existing population and average-speed graphs. Updated the ignore rules for generated images and improved the spacing of the on-screen sensing label.

In one observed run, average sensing range decreased from 85 to approximately 83.4–83.5 pixels before extinction. This observation alone does not establish a consistent evolutionary trend.

Next step: Improve compatibility with earlier statistics files and introduce persistent wandering.

## 11 October 2026

Updated the plotting script to support earlier three-column statistics CSVs. Files without sensing data produce population and average-speed graphs, while newer four-column files also produce the sensing-range graph. Checked the older format using a temporary three-column CSV.

Replaced random movement chosen every frame with persistent wandering when no food is sensed. Each organism maintains its own direction and changes it approximately once per second of wandering. Direction normalisation keeps movement consistent with the organism's speed, while the existing boundary limits keep it inside the window.

Observed organisms maintaining a direction and then changing it at the expected interval, both after food became scarce and with reduced starting food and delayed replenishment. Added the wandering interval to the settings export and updated the README and roadmap.

Next step: Continue developing inherited traits and environmental trade-offs.

## 14 October 2026

Fixed pause timing by keeping the frame clock running while paused, while allowing simulation timers to advance only when running. This prevents time spent paused from being counted as a large elapsed interval on resuming. Restored the movement boundary clamps so organisms remain inside the window during both food seeking and wandering.

Moved the statistics and settings CSV exports into a reusable save_run() function. Checked that closing the simulation still saves both files. Added microseconds to the shared filename timestamp to distinguish runs saved in quick succession.

Implemented reset using the R key. Reset saves the previous run before creating fresh organisms and food, clearing recorded statistics, resetting simulation timers, and resuming in the existing window. Checked the behaviour both while running and while paused, and confirmed that the previous run's files were saved. Corrected indentation and a lowercase organism() call during implementation.

Wondered why reset appeared to switch to a different starting arrangement rather than reopening the window. Reset replaces the simulation's organisms and food, whose starting positions are randomly generated, while retaining the same Pygame window.

Also questioned whether uneven frame durations could interfere with resetting timers. The timers are explicitly assigned zero, independently of frame timing. Subsequent updates accumulate measured elapsed time through dt. Events occur on the frame where their timer reaches the required interval, so their timing has frame-level precision.

Next step: Continue with the remaining roadmap features.

## 16 October 2026

Added a configurable random seed and included it in each run's settings export. Reset now reapplies the seed before creating organisms and food, allowing the same initial arrangement and starting traits to be recreated. Variable frame timing can still cause later behaviour to differ, so the seed alone does not guarantee identical simulation outcomes.

Added individual organism speed recording at each statistics sample. Each living organism contributes a row containing the elapsed simulation time and its speed. These records are saved in a separate speeds CSV using the same timestamp as the run's statistics and settings files, and are cleared after saving when resetting.

Inspected the exported speed records and confirmed that multiple organisms share each sampling time. Repeated speeds across samples are expected because an organism retains its speed during its lifetime. Speed-distribution plotting remains to be implemented.

Expanded the roadmap with trait visualisation ideas: mapping speed to colour, representing a future inherited size trait through body radius, and indicating critically low energy through fading or a shrinking energy indicator. Considered keeping these visual meanings distinct so low energy is not confused with a change in inherited size.

Next step: Plot speed distributions from the recorded individual speed samples.

## 17 October 2026

Created plot_speed_distribution.py to inspect individual organism speeds at a selected sampling time. The script reads the speeds CSV and groups records by time, allowing each population snapshot to be examined separately rather than combining repeated observations across the entire run.

Added a time selection prompt that chooses the nearest available recorded sample. Revisited how lambda works with min() to compare the distance between recorded times and the requested time.

Implemented a histogram showing the number of organisms within each speed interval and saved it as a PNG. Corrected filename handling, the title expression, and the image export argument during implementation. Ran the script and confirmed that it generated the histogram successfully.

Next step: Use consistent speed intervals and display the sampled population to make comparisons clearer.

## 18 October 2026

Replaced automatically chosen histogram intervals with fixed boundaries from 1 to 3 pixels per simulation update, in steps of 0.2. Fixed the horizontal axis to the same range, matching the simulator's current speed limits.

Questioned what this change achieved and clarified that automatic intervals can differ between snapshots. Fixed boundaries ensure that each bar represents the same speed range across graphs without changing the simulation or recorded data.

Added the selected snapshot's population count to the histogram title. This provides context when comparing bar heights between populations of different sizes. Checked the updated graph and confirmed that the population count appeared correctly.

Updated the README and roadmap to reflect completed speed-distribution plotting.

Investigated whether movement and energy expenditure used consistent timing. Movement previously occurred once per rendered frame, while energy loss and other timers depended on elapsed seconds. This meant a lower rendering frame rate could reduce the distance organisms travelled without reducing their energy expenditure per second.

Introduced a fixed simulation timestep of 1/60 second and an accumulator that determines how many updates are needed before drawing each frame. Movement, energy loss, food replenishment, reproduction checks, and statistics recording now run within the fixed-update loop. Drawing remains separate, and reset clears the accumulator.

Compared runs rendered at 30 and 60 FPS using the same random seed and simulation settings. The first eight recorded samples matched exactly across elapsed time, population, average speed, and average sensing range. Rendering at 30 FPS appeared rougher, but the recorded simulation behaviour remained consistent. Restored rendering to 60 FPS and added timing parameters to the settings export.

Questioned what would happen at higher or nonstandard rendering rates, such as 120, 43, or 95 FPS. Clarified that the accumulator accommodates different ratios between rendering and simulation updates. Also distinguished the display's refresh rate from rendering FPS and simulation frequency; drawing more frequently does not increase the simulation's update rate.

Extracted the repeated population statistics calculation into calculate_stats(), returning the population count, average speed, average sensing range, and highest living generation. Used the function for both recording and display, and checked that the simulation continued to work.

Reviewed generated-file ignore patterns and added explicit rules matching the capitalised simulation CSV filenames.

Next step: Continue with the remaining roadmap features using the fixed-timestep simulation as the foundation.

## 19 October 2026

Updated the speed-axis labels in the plotting scripts from pixels per frame to pixels per simulation update, matching the fixed-timestep implementation.

Added individual organism colours based on movement speed. A normalised speed value blends RGB components between blue at minimum speed and orange at maximum speed, producing a continuous gradient.

During implementation, corrected a missing method-call parenthesis that caused an invalid colour argument. Also corrected addition to multiplication in the blending formula after observing that all organisms initially appeared orange. Running the corrected version showed intermediate colours between the endpoints.

Added a legend identifying the slower and faster ends of the gradient. Each organism retains its colour while its speed remains unchanged, while offspring can receive slightly different colours through speed mutation. Energy visualisation remains a separate planned feature.

Updated the README and roadmap to reflect completed speed-based colour mapping.

Next step: Continue with the remaining roadmap features.

## 24 October 2026

Implemented low-energy darkening through get_display_color(), which adjusts the brightness of each organism's existing speed colour. Organisms retain their full colour above the configured energy threshold and become progressively darker below it, with a minimum brightness of 20%. This changes appearance without affecting simulation mechanics.

Initially tested a critical-energy threshold of 30. The darkening appeared too brief and abrupt, so increased it to 50 to make the transition easier to observe.

Considered alternative energy indicators. Bars and rings would add clutter around a large population, shrinking would conflict with the planned inherited size trait, and changing shape would disrupt the intended appearance. Chose body darkening while accepting that speed colours become harder to distinguish at low energy.

Added a low-energy explanation to the visual legend and reduced all three legend labels from font size 28 to 25.

Recognised that displaying organisms in different speed-based colours made it harder to perceive them as members of the same species and distinguish their low-energy darkening. 

Addressed this by adding two viewing modes, toggled with V. Normal view uses a shared body colour, making the darkening below the critical-energy threshold easier to observe. Speed-trait view retains the colour gradient for inspecting inherited speed differences. Both views apply the same low-energy darkening.

Updated the legend to match the selected view. Normal view keeps the mode and energy labels together, while speed-trait view moves the mode label upward to accommodate the speed-colour explanations. Checked switching while running and paused, and confirmed that reset preserves the selected view.

Next step: Continue with the remaining roadmap features.