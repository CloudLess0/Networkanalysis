# Networkanalysis

This Project was part of my preparetion for the Networkanalysis lecture of Prof. Zweig at the Technische Universität Kaiserslautern (TUK)

## Requirements

The Code was written in Python 2.7

and requires the following packages:

```
numpy
matplotlib
python-igraph
```
## Content

- ```smallworld_experiment.py``` is the R code from the lecture writte in Python.
  It shows the properties of smallworld graphs.

- ```trans_cc.py``` is an experiment to show the influece on transitivity and clustering coefficient when adding a linear list of nodes to a clique with size 4.

- ```cpm_clustering.py``` is my implementation of the [Clique Percolation Method](https://en.wikipedia.org/wiki/Clique_percolation_method), that produces an overlapping clustering for a given graph and k.
Differnce to Wikipedia desciption is that it groups cliques with size k+1 if they share k nodes.
It also contains a method ```lectureexample()``` , which produces a hierarchical overlapping clustering for a given graph.

