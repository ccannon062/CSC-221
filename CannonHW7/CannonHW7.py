# CannonHW7.py
# Caleb Cannon
# A program to investigate a network of King Baldwin IV

import networkx

def loadEdges(nt):
    infile = open("baldwinIV.csv", "r")
    text = infile.readline()
    while text != "":
        a,b = text.strip().split(',')
        nt.add_edge(a,b)
        text = infile.readline()
    infile.close()
    return

def findBestConnected(nt):
    maxConn = -1
    bestConn = -1
    for i in nt.nodes():
        print(i,":", maxConn)
        if nt.degree(i) > maxConn:
            bestConn = i
            maxConn = nt.degree(i)
    return bestConn, maxConn

def main():
    nt = networkx.Graph()
    loadEdges(nt)
    print()
    print("Number of nodes is:",len(nt.nodes()))
    nt.degree()
    sp1 = networkx.shortest_path(nt,"Baldwin IV","Guy of Lusignan")
    sp2 = networkx.shortest_path(nt, "Pope Alexander III", "Alexander III")
    sp3 = networkx.shortest_path(nt, "Richard I", "Isabella of Scotland")
    print("Shortest path between Baldwin IV and Guy of Lusignan is",sp1)
    print()
    print("Shortest path between Pope Alexander III and Alexander III is",sp2)
    print()
    print("Shortest path between Richard I and Isabella of Scotland is",sp3)
    bc = networkx.betweenness_centrality(nt)
    print("Betweenness centrality of nt is:")
    print("Betweenness centrality of Baldwin IV is",str(bc["Baldwin IV"]))
    print("Betweenness centrality of Guy of Lusignan is",str(bc["Guy of Lusignan"]))
    print("Betweenness centrality of Welf VI is",str(bc["Welf VI"]))
    bestConn, maxConn = findBestConnected(nt)
    print("Best connected is:",bestConn,"with max of",maxConn)

main()
