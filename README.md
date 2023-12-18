# Virus Spread Simulation

## Overview
This project presents a Virus Spread Simulation, leveraging advanced programming techniques and mathematical modeling to mirror the transmission dynamics of a viral infection within a structured population. The simulation integrates real-world demographic data, providing insights into the complex interactions and behaviors in a society facing a viral outbreak.

## Technologies and Tools

### Programming Language
- **Python**: The primary language used for the project, chosen for its versatility and strong support for data manipulation and simulation.

### Key Libraries
- **Matplotlib**: Employed for data visualization, this library helps in graphically representing the simulation outcomes.
- **Random**: This module plays a crucial role in the probabilistic aspects of the simulation, generating random events to mimic real-life unpredictability.

## Simulation
![image](https://github.com/SafiShahid34/VirusSim/assets/96895832/c509bb04-52a3-446a-871b-5c809239086f)

## Mathematical Logic and Modeling

This Virus Spread Simulation incorporates a blend of mathematical and computational techniques to accurately model the dynamics of a viral outbreak in a structured society. Key aspects of the simulation's logic and modeling are as follows:


### 1. Infection Spread Mechanism
- When a person (p) in the population is infected and alive, the simulation iterates through their contacts (p.rcontact + p.pcontact).
- For each contact (j), there's a chance they will get infected. This is determined by p.spreadrate (the infected person's likelihood to spread the virus) and j.poss (the contact's susceptibility to getting infected).
- The possibility function is a key part of this process. It converts these probabilities into a yes/no outcome using randint. If a random number from 0 to 999 is less than or equal to probability * 1000, the event (like infection) occurs.
  
### 2. Mortality and Recovery Calculation
- Each person in the simulation has a mrate, which is their mortality rate.
- After a person has been infected for a certain number of days (15 in your simulation), the possibility function checks against their mortality rate to determine if they die or recover.
- If they survive (random chance determined by mrate), they are marked as recovered and no longer infected. If not, they are marked as not alive.
  
### 3. Tracking the Spread and Outcomes
- The simulation keeps track of various statistics like newcases, newdeaths, newrecovery, and accumulates them in lists like casesl, deathsl, recoverl, etc.
- These statistics are updated in each iteration (each day in the simulation) based on the outcomes of the infection spread and recovery/mortality checks.
  
### 4. Random Social Connections
- The function randomConnections creates random interactions (social connections) between individuals, based on their types ('w', 's', 'o').
- This randomness simulates real-life encounters outside of a person's permanent social circle.

#### Formulaic Explanation
- Infection Chance: if randint(0, 999) <= spreadrate * 1000 then infect
- Mortality Check: if randint(0, 999) <= mrate * 1000 then die else recover
  
#### Key Points
- The simulation does not use deterministic formulas but probabilistic models. This means the outcomes (like who gets infected, who dies, and who recovers) are based on chance, reflecting the uncertainty and randomness found in real-life disease spread.
- The parameters like spreadrate, mrate, and the number of days before recovery/death checks are crucial. They should be set based on realistic data or estimates for the simulation to be meaningful.
- This probabilistic approach allows the simulation to mimic the unpredictability and complexity of real-world viral spread, making it a valuable tool for understanding and analyzing potential scenarios in public health studies.

## Network Theory in Social Interactions
- The simulation applies principles of network theory to represent the complex web of social interactions.
- **Societal Roles**: Different societal roles like students, teachers, and workers are represented, each having unique patterns of interaction and contact networks.
- **Family and Social Units**: Families are dynamically generated, with each member having permanent contacts (family, co-workers, etc.) and the potential for random interactions. This reflects the multifaceted nature of human social networks.

### Demographic Segmentation
- The population is segmented into various age groups and societal roles, reflecting the demographic structure outlined in the [United Nations report](https://www.un.org/en/development/desa/population/events/pdf/expert/25/2016-EGM_Nicole%20Mun%20Sam%20Lai.pdf).
- **Age-based Susceptibility**: Different age groups have varied susceptibility to the virus, mortality rates, and interaction patterns, mirroring real-world epidemiological data.
- **Population Dynamics**: The societal structure accounts for typical family units, working professionals, and educational settings, ensuring a realistic distribution of interactions.

### Visualization and Analysis
- Using `matplotlib`, the simulation outcomes are visualized to provide insights into the progression of the virus over time. This includes daily and cumulative counts of cases, recoveries, and deaths.
- Data is recorded and plotted to show trends and patterns, facilitating a deeper understanding of the outbreak dynamics under various conditions.

The combination of these mathematical and computational approaches provides a robust framework for simulating and analyzing the spread of viruses in a societal context. It offers a window into the complex interplay of demographic factors, social interactions, and individual behaviors in the face of a public health crisis.


## Installation and Usage

```bash
# Clone the repository
git clone https://github.com/yourUsername/VirusSim.git
cd VirusSim

# Install required libraries
pip install matplotlib

# Run the simulation
python VirusSim.py
