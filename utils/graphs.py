import graphviz as gv
import math
import heapq

def show(G, labels=[], directed=False, weighted=False, path=[], layout="sfdp"):
  graph = gv.Digraph("felicidad") if directed else gv.Graph("alegria")
  graph.format = 'svg'
  graph.graph_attr["layout"] = layout
  graph.edge_attr["color"] = "gray"
  graph.node_attr["color"] = "orangered"
  graph.node_attr["width"] = "0.1"
  graph.node_attr["height"] = "0.1"
  graph.node_attr["fontsize"] = "8"
  graph.node_attr["fontcolor"] = "mediumslateblue"
  graph.node_attr["fontname"] = "monospace"
  graph.edge_attr["fontsize"] = "8"
  graph.edge_attr["fontname"] = "monospace"
  n = len(G)
  if labels:
        for i, lbl in enumerate(labels):
            graph.node(str(i), lbl)
  added = set()
  for v, u in enumerate(path):
    if u != -1:
      if weighted:
        w = 0
        for vi, w in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="orange")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  for u in range(n):
    for edge in G[u]:
      w = 0
      if weighted:
        v, w = edge
      else:
        v = edge
      draw = False
      if not directed and not f"{u},{v}" in added:
        added.add(f"{u},{v}")
        added.add(f"{v},{u}")
        draw = True
      elif directed and not f"{u},{v}" in added:
        added.add(f"{u},{v}")
        draw = True
      if draw:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))
  return graph

def bellmanFord(G, s):
    n = len(G)
    g = [math.inf]*n
    path = [-1]*n
    g[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                if g[u] + w < g[v]:
                    g[v] = g[u] + w
                    path[v] = u

    for u in range(n):
        for v, w in G[u]:
            if g[u] + w < g[v]:
                return None, None

    return path, g

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    g = [math.inf]*n
    g[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in G[u]:
            if g[u] + w < g[v]:
                g[v] = g[u] + w
                path[v] = u
                heapq.heappush(pq, (g[v], v))

    return path, g

