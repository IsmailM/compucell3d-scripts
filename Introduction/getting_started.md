# A Quick Getting Started Guide To CompuCell3D

## Setting Up the Template Script 

To get started, load up Twedit++ inside CC3D.


Select "CC3D Project"-->"New CC3D Project". We can then specify the parameters and options of our simulation. Now Twedit++ will generate a default script for us.

## Understanding the XML

- Lattice Parameters `<Potts>`: global parameters like (i) lattice dimensions, (ii) number of Monte Carlo Time Steps, (iii) Temperature and (iv) neighbourhood selection.

- Plugins `<Plugin>`: all te plubins in being used like "Cell Type" and the "Contact Energies"

- Steppables `<Steppable>`: lists all "steppables"

Once all relavant edits have been made, we can play the simulation by "File"-->"Open Simulation File"