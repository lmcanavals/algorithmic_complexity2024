import graphviz as gv
import random


def randomG(n, m, directed=False, weighted=False, wrange=(1, 10)):
    if directed:
        checker = [(i, j) for i in range(n) for j in range(i, n) if i != j]
    else:
        checker = [(i, j) for i in range(n) for j in range(i + 1, n)]

    random.shuffle(checker)
    G = [[] for _ in range(n)]
    checker = checker[:m]
    checker.sort()
    for u, v in checker:
        if weighted:
            w = random.randint(*wrange)
            G[u].append((v, w))
            if not directed:
                G[v].append((u, w))
            continue
        G[u].append(v)
        if not directed:
            G[v].append(u)
    return G


def scaleCoords(coords, maxsize, stretch):
    maxsizex, maxsizey = maxsize
    maxsizey = maxsizex if not stretch and maxsizex < maxsizey else maxsizey
    maxsizex = maxsizey if not stretch and maxsizex > maxsizey else maxsizex
    x, y = zip(*coords)
    minx, maxx, miny, maxy = min(x), max(x), min(y), max(y)
    spanx, spany = maxx - minx, maxy - miny
    spanx = spany if not stretch and spanx < spany else spanx
    spany = spanx if not stretch and spanx > spany else spany
    factorx = spanx / maxsizex
    factory = spany / maxsizey

    x = map(lambda x: (x - minx) / factorx, x)
    y = map(lambda y: (y - miny) / factory, y)

    return list(zip(x, y))


def showG(G, labels=None, path=[], directed=False, weighted=False,
          coords=None, maxsize=(5, 5), stretch=False, xlabels=False,
          layout='circo', pathcolor='darkorange',
          node_attr={'color': 'peru',
                     'fontcolor': 'mediumslateblue',
                     'fontname': 'monospace',
                     'fontsize': '8',
                     'height': '0.1',
                     'width': '0.1'},
          edge_attr={'color': 'lightgray',
                     'fontname': 'monospace',
                     'fontsize': '8'}):

    # setup the graph
    dot = gv.Digraph('x') if directed else gv.Graph('y')
    layout = 'fdp' if coords and layout not in ['fdp', 'neato'] else layout
    dot.graph_attr['layout'] = layout
    dot.node_attr = node_attr
    dot.edge_attr = edge_attr

    # preparing labels and scaling coords
    n = len(G)
    labels = labels if labels else list(map(str, range(n)))
    coords = scaleCoords(coords, maxsize, stretch) if coords else None

    # adding node info: id, label or xlabel and coords. '' if not provided
    for u in range(n):
        dot.node(str(u),
                 '' if xlabels else labels[u] if labels else str(u),
                 xlabel='' if not xlabels else labels[u] if labels else str(u),
                 pos=f'{coords[u][0]},{coords[u][1]}!' if coords else '')

    # easy access path arcs with direction both ways to avoid omitting
    rpath = dict()
    for node, parent in enumerate(path):
        if parent == -1:
            continue
        rpath[f'{parent},{node}'] = 'forward'
        rpath[f'{node},{parent}'] = 'back'

    # create a list of edges pulling path info and sort it, ensure same figure
    checker = set()
    edges = []
    for u in range(n):
        for edge in G[u]:
            v, w = edge if weighted else (edge, None)
            e = f'{u},{v}'
            if e in checker:
                continue
            edges.append((u, v, w, '' if e not in rpath else rpath[e]))
            checker.add(e)
            if not directed:
                checker.add(f'{v},{u}')
    edges.sort()

    # adding edges to the dot graph
    for u, v, w, dirpath in edges:
        edgeinfo = map(str, (u, v, w) if w else (u, v))
        if dirpath:
            dot.edge(*edgeinfo, dir=dirpath, color=pathcolor)
        else:
            dot.edge(*edgeinfo)

    return dot

