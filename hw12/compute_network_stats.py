import json
import networkx as nx
import argparse

def degree(network):
    edges = []
    for k,v in network.items():
        for edge in v.keys():
            edges.append((k, edge))
    G = nx.Graph(edges)
    deg_cent = nx.degree_centrality(G)
    result = sorted(deg_cent, key=deg_cent.get, reverse=True)
    return result[:3]

def weighted(network):
    edges = []
    for k,v in network.items():
        for edge, weight in v.items():
            edges.append((k, edge, {'weight': weight}))
    G = nx.Graph(edges)
    weight_cent = dict(G.degree(weight='weight'))
    result = sorted(weight_cent, key=weight_cent.get, reverse=True)
    return result[:3]

def closeness(network):
    edges = []
    for k,v in network.items():
        for edge in v.keys():
            edges.append((k, edge))
    G = nx.Graph(edges)
    close_cent = nx.closeness_centrality(G)
    result = sorted(close_cent, key=close_cent.get, reverse=True)
    return result[:3]

def betweenness(network):
    edges = []
    for k,v in network.items():
        for edge in v.keys():
            edges.append((k, edge))
    G = nx.Graph(edges)
    bet_cent = nx.betweenness_centrality(G)
    result = sorted(bet_cent, key=bet_cent.get, reverse=True)
    return result[:3]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file')
    parser.add_argument('-o', '--output_file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        network = json.load(f)

    results = {}
    results["degree"] = degree(network)
    results["weighted_degree"] = weighted(network)
    results["closeness"] = closeness(network)
    results["betweenness"] = betweenness(network)

    with open(args.output_file, 'w') as f:
        json.dump(results, f, indent=4)
