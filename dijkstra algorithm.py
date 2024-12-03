# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:52:28 2021

@author: Tapas
"""
#Importing networkx, and aliasing it as nx. Networkx module has the graph dat strucuture.
import networkx as nx
#Importing infinity from math module
from math import inf
#Function called shortest_path for a graph, arguments passed are a graph, starting node and the target node
def shortest_path(G, s, t):
    #A list called explored to keep track of all the explored nodes, it initially has 's' as the first explored node
    explored = [s]
    #A list that stores the distance b/w nodes from the starting node, it is initialised as -1, meaning that there isn't no path between the nodes.
    dist_bw_nodes = [-1]*len(G)
    #The distance b/w starting node and itself is given a value of zero
    dist_bw_nodes[s] = 0
    #A list that stores the preceding nodes
    predecessors = [-1]*len(G)
    #A loop that keeps iterating until our target node is not in the explored list
    while t not in explored :
        #Setting the best distance from starting node as infinity
        d_best = inf
        # A loop that iterates over every element in the explored list.
        for u in explored:
            #A loop that iterates over every neighbor called 'v' for 'u'
            for v in G.neighbors(u):
                #Storing the weight between '' and 'v' in a variable called 'w'
                w = G.get_edge_data(u, v, default = 0)['weight']
                # Tells the interpreter to try the condition given inside the try keyword
                try:
                    #A condition telling what to do if v is not in the list explored
                    if v not in explored:
                        #Tells that the distance 'dist' is just the distance for u from the list dist_bw_nodes added to w
                        dist = dist_bw_nodes[u] + w
                        #Tells what to do if dist is less than d_best which is set as infinity
                        if dist < d_best:
                            #If the above condition is satisfied, d_bes will have the value dist
                            d_best = dist
                            #sets the value of variable u_best as u
                            u_best = u
                            #sets the value of variable v_best as v
                            v_best = v
                #Tells the interpreter to execute the command written inside the except keywork if the above condition fails            
                except:
                    #Asks to execute the print statement if the above condition fails.
                    print('No possible path')
                    # tis to loop out of the function
                    return 
        #sets the best distance for v_best in the list dist_bw_nodes                
        dist_bw_nodes[v_best] = d_best
        #Appends v_best to explored
        explored.append(v_best)
        #Sets the predecessor as u_best for v_best
        predecessors[v_best] = u_best
    #A list called path which shows the shortest path taken from target node to the starting node 
    path = [t]
    #A condition that iterates over till the last element of path isn't 's'
    while path[-1] != s:
        #Appends the element from predecessor for which the value is path[-1]
        path.append(predecessors[path[-1]])
    #Reverses the list path so that it shsows the path taken from starting node to target node
    path.reverse()
    #Returns the list path, which show the path taken from s to t
    return path
#Test case
G = nx.Graph()

G.add_edge(0, 1, weight=5)
G.add_edge(1, 6, weight=100)
G.add_edge(1, 5, weight=7)
G.add_edge(1, 2, weight=2)
G.add_edge(1, 4, weight=3)
G.add_edge(6, 5, weight=3)
G.add_edge(5, 3, weight=7)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=4)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos =nx.circular_layout(G), with_labels= True)

print(shortest_path(G, 0, 6))
