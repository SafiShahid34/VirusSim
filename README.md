# Virus Spread Simulation

## Overview
This project presents a Virus Spread Simulation, leveraging advanced programming techniques and mathematical modeling to mirror the transmission dynamics of a viral infection within a structured population. The simulation integrates real-world demographic data, providing insights into the complex interactions and behaviors in a society facing a viral outbreak.

## Technologies and Tools

### Programming Language
- **Python**: The primary language used for the project, chosen for its versatility and strong support for data manipulation and simulation.

### Key Libraries
- **Matplotlib**: Employed for data visualization, this library helps in graphically representing the simulation outcomes.
- **Random**: This module plays a crucial role in the probabilistic aspects of the simulation, generating random events to mimic real-life unpredictability.

## Mathematical Logic and Modeling

This Virus Spread Simulation incorporates a blend of mathematical and computational techniques to accurately model the dynamics of a viral outbreak in a structured society. Key aspects of the simulation's logic and modeling are as follows:

### Probabilistic Approach
- The simulation uses a probabilistic model to mimic real-life uncertainties in virus transmission and its outcomes.
- **Infection Spread**: The likelihood of virus transmission from an infected individual to others is determined using random probability checks. This is based on each person's infection spread rate and the susceptibility of their contacts.
- **Mortality and Recovery**: The outcomes of an infection, such as mortality or recovery, are also modeled probabilistically. Individuals have a mortality rate, and upon reaching a certain duration of infection, a random check determines if they recover or succumb.

### Network Theory in Social Interactions
- The simulation applies principles of network theory to represent the complex web of social interactions.
- **Societal Roles**: Different societal roles like students, teachers, and workers are represented, each having unique patterns of interaction and contact networks.
- **Family and Social Units**: Families are dynamically generated, with each member having permanent contacts (family, co-workers, etc.) and the potential for random interactions. This reflects the multifaceted nature of human social networks.

### Demographic Segmentation
- The population is segmented into various age groups and societal roles, reflecting the demographic structure outlined in the [United Nations report](https://www.un.org/en/development/desa/population/events/pdf/expert/25/2016-EGM_Nicole%20Mun%20Sam%20Lai.pdf).
- **Age-based Susceptibility**: Different age groups have varied susceptibility to the virus, mortality rates, and interaction patterns, mirroring real-world epidemiological data.
- **Population Dynamics**: The societal structure accounts for typical family units, working professionals, and educational settings, ensuring a realistic distribution of interactions.

### Data-Driven Structure
- The societal setup, including the proportion of different roles and age groups, is informed by real-world demographic data. This lends credibility and accuracy to the simulation, allowing it to serve as a tool for understanding and predicting the impact of viral outbreaks.

### Visualization and Analysis
- Using `matplotlib`, the simulation outcomes are visualized to provide insights into the progression of the virus over time. This includes daily and cumulative counts of cases, recoveries, and deaths.
- Data is recorded and plotted to show trends and patterns, facilitating a deeper understanding of the outbreak dynamics under various conditions.

The combination of these mathematical and computational approaches provides a robust framework for simulating and analyzing the spread of viruses in a societal context. It offers a window into the complex interplay of demographic factors, social interactions, and individual behaviors in the face of a public health crisis.

## Real-World Data Integration

- **United Nations Data**: The societal structure and age demographics are based on a [United Nations report](https://www.un.org/en/development/desa/population/events/pdf/expert/25/2016-EGM_Nicole%20Mun%20Sam%20Lai.pdf), ensuring the simulation mirrors real-world population distributions.
- **Societal Role Dynamics**: Each societal role is modeled based on typical real-world behaviors and interactions, like students attending classes or workers having varying degrees of public exposure.

## Installation and Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/virus-spread-simulation.git
cd virus-spread-simulation

# Install required libraries
pip install -r requirements.txt

# Run the simulation
python simulation.py
