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
