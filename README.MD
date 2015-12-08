## Requirements:
#####networkx

  pip3 install networkx
  
  https://networkx.github.io/
#####matplotlib

  pip3 install matplotlib
  
  http://matplotlib.org/
  
##Total Infection
Infection is released to one user that is then spread through using the connections between users. Users from the graph are traversed by a breadth-first search using a queue until all users on the graph are infected.

##Limited Infection
An infection is released to a user in the same fashion as total infection, however users are infected only if their neighbors have a frequency >= 2. This stops the infection from traversing to nodes that don't satisfy such condition.
