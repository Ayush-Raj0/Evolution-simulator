# Evolution Simulator
To explore how complex traits may emerge under environmental and evolutionary pressures.

## Overview
Evolution Simulator is an independent project built by me in Python using Pygame. It simulates organisms interacting with a simple environment in which they move, consume food, expend energy over time, reproduce after accumulating sufficient energy, and die if they are unable to sustain themselves.

The project began from a question of mine: **How do organisms evolve and adapt when exposed to environmental pressures and external stimuli?**

The current version establishes the basic survival and reproduction mechanics required to explore that question. Organisms can reproduce and pass their movement speed to their offspring. The longer-term goal is to introduce mutation, additional inherited traits, improved behaviour and environmental pressures so that populations can evolve over multiple generations.

## Current Features
* Random organism movement
* Energy consumption over time
* Food consumption and energy recovery
* Collision detection
* Organism death based on energy level
* Organism reproduction after reaching a minimum energy threshold
* Reproduction energy cost
* Offspring spawning near the parent
* Basic inheritance of movement speed
* Real-time graphical simulation using Pygame
* Food sensing and seeking
* Population statistics
* Timed food replenishment with a maximum food count
* Inherited sensing range with bounded mutation
* Sensing-dependent energy loss
* Average sensing range display, CSV recording, and graph
* Persistent wandering with timed direction changes
## Planned Features
* Trait mutation
* Additional inherited traits
* Vision
* Different metabolic strategies
* Multi-generation evolution

## Built With

* Python
* Pygame

## Development

The project was developed independently using Visual Studio Code. A public roadmap, development log, and experiment plan are included in the repository to document its progression and future work.

- [Roadmap](ROADMAP.md): Completed features and future development plans.
- [Experiment Plan](EXPERIMENTS.md): Questions, settings, and data planned for simulation experiments.
- [Development Log](EXPERIMENTAL_LOG.md): Implementation notes, observations, and bug fixes.


## How to Run
To run the Evolution Simulator on your computer:

1. Install Python if it is not already installed.

2. Open a command-line window:

   * **Windows:** Press `Windows + R`, type `cmd`, and press Enter.
   * **macOS:** Open **Terminal** from Applications → Utilities, or search for “Terminal” using Spotlight.

3. Install Pygame by entering the following command:

   `pip install pygame`

   On some macOS systems, you may need to use:

   `pip3 install pygame`

4. Clone or download this repository to your computer.

5. Open the downloaded project folder in Visual Studio Code or another Python IDE/code editor.

6. Open the `Evolution_simulator` file.

7. Run the `Evolution_simulator` file to start the Evolution Simulator.
