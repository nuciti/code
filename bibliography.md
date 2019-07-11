# Liu, 2013

The paper develops a mathematical criterion to balance environmental factors (as land price), service radius of a station (i.e. how much the battery gets discharged to get to a station), investment, maintenance, and operation costs. The constraints limit infrastructure properties as how many stations can be connected to one power supply. The objective (formula (3)) is then minimized using standard optimization techniques - a *dual formulation* is calculated and this dual is optimized using the *Newton's method*.

Relevant quote:
* EVs cannot only increase energy utilization andreduce pollution emission, but also smooth the load curve bypeak load shaving and, hence, enhance the security and eco-nomics of the power system concerned by coordinating with intermittent renewable energies, such as wind generation.

# Lam, 2013

This paper proposes a formal definition of the problem (Electric Vehicle Charging Station Placement Problem). In the paper, it is proven that the problem is NP-complete by a reduction from the *Vertex Cover Problem*. The city is represented as a graph with a distance metric, where each car has a maximum reachable distance, the capacity of a station is more than the average demand in the neighborhood of this station (estimated from density!). The problem is then solved using the *Mixed Integer Programming*, and a *greedy heuristics* is provided.

Relevant qote:
* We  study  where  charging  stationsshould be constructed in a city such that we can minimize theconstruction cost with coverage extended to the whole city andfulfillment of drivers’ convenience.
* hundreds of EVs coordinateto  act  as  a  power  source  selling  power  back  to  the  grid  orto  support  auxiliary  services  like  regulation.
* We concernmore about how EVs influence the growth of a smart city.

# Mehar 2013

# Xiang, 2016
The paper formulates an economic planning model for optimal placement of charging stations (CSs) for electric vehicles. The origin-destination traffic flow data is considered in the optimisation problem in order to determine the location of the CSs. The capacity of the CSs is determined after obtaining the equilibrium traffic flow on each road. A queueing model is considered for the service system of CSs, in which the arrival of vehicles in a certain CS is a Poisson process. Load capability constraints are also included in the model.

# Jin, Maojing, Ruifeng Shi, Ning Zhang, and Yang Li. "Study on multi-level layout planning of electric vehicle charging stations based on an improved genetic algorithm." International Journal of Smart Grid and Clean Energy 2, no. 2 (2013): 277-282.

Uses a GA to optimise the distribution of charging stations. Objective function contains two objectives to be minimised: 1) Cost of constructing the charging stations; 2) Cost for drivers to reach their nearest charging station. Candidate solutions are encoded as bit strings: There are ten possible station locations, and five of these are chosen for each individual. For our project, we do not consider the cost of construction of the stations.
