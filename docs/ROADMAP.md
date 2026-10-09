# Evolution Simulator Roadmap
Build the simulator one feature at a time, starting with basic survival
behaviour and progressing towards observable evolution across generations.

## Completed

- [x] Create the Pygame simulation window and main loop.
- [x] Represent organisms and food using classes.
- [x] Add random movement and keep organisms within the window.
- [x] Detect collisions between organisms and food.
- [x] Allow organisms to eat food and gain energy.
- [x] Add time-based energy depletion and death.
- [x] Add reproduction with an energy threshold and energy cost.
- [x] Spawn offspring near their parent.
- [x] Pass the parent's speed to offspring.
- [x] Add bounded speed mutation.
- [x] Sense the nearest food within a limited range.
- [x] Move towards sensed food and wander when none is detected.
- [x] Add speed-dependent energy loss as a metabolic trade-off.
- [x] Display the living population count and average speed.
- [x] Gradually replenish food during the simulation with a maximum food count.
- [x] Give each organism a generation number, starting at generation 0.
- [x] Give each child its parent's generation number plus 1.
- [x] Display the highest generation currently alive.
- [x] Record population size and average speed over time.
- [x] Plot population size and average speed over time from exported CSV data.experiment controls.

## Next: Multi-generation Evolution
Reproduction already produces descendants. The next stage is to track
generations and study how inherited traits change under environmental
pressures.

- Run experiments with different food availability and energy costs.
- Analyse how survival and reproduction affect the distribution of speeds.

## Future Ideas: After the Current Roadmap
These are longer-term ideas rather than a fixed implementation order -

- Explore additional inherited traits, such as size or sensing range.
- Explore different metabolic strategies.
- Explore environmental zones and changing conditions.
- Explore communication, cooperation, resource storage, and specialised behaviour.
- Add Experiment controls.

- Add inherited sensing range with mutation and a sensing energy cost.
- Add persistent wandering direction.
- Use random seeds for reproducible experiments.
- Add speed-distribution graphs.
- Add food patches and extend environmental zones.
- Track family lines and their descendants.

## Advanced Future Features

- Add organism decision-making using small neural networks.
- Evolve neural-network weights through inheritance and genetic mutation.
- Compare evolved behaviour with the existing food-seeking rules.
- Measure performance as organism and food counts increase.
- Add spatial partitioning using a grid of cells.
- Use nearby grid cells for food sensing and collision checks.
- Compare performance and correctness with the original food-search approach