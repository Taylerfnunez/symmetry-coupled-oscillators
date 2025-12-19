from sage.all import Graph as sg
import networkx as nx




def compute_Q(G):
    """
    Compute the quotient graph of a graph with respect to its automorphism orbits.

    Parameters
    ----------
    G : networkx.Graph or sage.graphs.graph.Graph
        Input graph. If a NetworkX graph is provided, it is internally converted
        to a Sage graph to compute automorphism orbits.

    Returns
    -------
    list of lists
        A list of the orbit set 
    networkx.Graph
        The quotient graph obtained by collapsing vertices in the same
        automorphism orbit of G.
    """
  
    #  Check whether input graph is a sage or networkx object
    if isinstance(G, (nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph)):
        sage_G = sg(G)     # Sage copy
        nx_G   = G          # Networkx graph
    else:
        sage_G = G
        nx_G = nx.Graph(sage_G.networkx_graph()) 

    # Compute vertex orbits from the automorphism group
    Aut = sage_G.automorphism_group()
    orbits = Aut.orbits()

    # Convert orbits to plain Python sets matching nx_G node labels
    orbits_py = [set(orb) for orb in orbits]


    #  Build quotient graph in NetworkX
    return orbits, nx.quotient_graph(nx_G, orbits_py)