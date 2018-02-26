# Somnath Tagore
import sys
from collections import defaultdict
from itertools import combinations
from math import sqrt
import time

# specialized gmean for six values
gmean = lambda a, b, c, d, e, f: sqrt(sqrt(sqrt(a * b * c * d * e * f)))

def weighted_comm_percol(filename):
  start = time.time()
  print >> sys.stderr, 'Pruning ...'
  # read protein-protein pairs
  data = defaultdict(set)
  weights = defaultdict(dict)
  four_comms = defaultdict(set)
  connected_comms = defaultdict(set) 
  with open(filename, 'r') as f:
    for line in f:
      a,b,w = line.split()[:3]
      x,y = data[a], data[b]
      w = float(w)
      for c,d in combinations(x & y, 2):
        if d not in data[c]: continue
        comm = frozenset((a,b,c,d))
        connected_comms[frozenset((a,b,c))].add(comm)
        connected_comms[frozenset((a,b,d))].add(comm)
        connected_comms[frozenset((a,c,d))].add(comm)
        connected_comms[frozenset((b,c,d))].add(comm)
        # group communities by their intensities
        four_comms[gmean(weights[a][c], weights[a][d], weights[b][c],
          weights[b][d], weights[c][d], w)].add(comm)
      x.add(b)
      y.add(a)
      weights[a][b] = w
      weights[b][a] = w
  del data
  del weights

  if len(four_comms) == 0:
    raise Exception('No communities found. (%f sec)' % (time.time()-start))

  print >> sys.stderr, 'Building communities... (%f sec)' % (time.time()-start)

  # sort communities
  four_comms = sorted(four_comms.iteritems())

  comm_graph = defaultdict(set)
  connected_comms = connected_comms.values()
  while connected_comms:
    for a,b in combinations(connected_comms.pop(), 2):
      comm_graph[a].add(b)
      comm_graph[b].add(a)
  del connected_comms

  print >> sys.stderr, 'Running algorithm... (%f sec)' % (time.time()-start)

  good_comms = set() 
  i = 0
  while four_comms:
    communities = []
    good_comms |= four_comms.pop()[1]
    frontier, unvisited = set(), good_comms.copy()
    while unvisited:
      component = set()
      frontier.add(unvisited.pop())
      
      while frontier:
        component.update(*frontier)
        unvisited -= frontier
        frontier = unvisited & set.union(*(comm_graph[x] for x in frontier))
      
      communities.append(component)

    if len(communities) > 1:
      communities.sort(key=len, reverse=True)
      if i % 100 == 0:
        print >> sys.stderr, i, float(len(communities[0])) / len(communities[1])
      if len(communities[0]) / len(communities[1]) >= 2:
        print >> sys.stderr, 'Done. (%f sec)' % (time.time()-start)
        return communities

    i += 1

  print >> sys.stderr, 'Done. (%f sec)' % (time.time()-start)
  return communities

if __name__ == '__main__':
  for c in weighted_comm_percol(sys.argv[1]):
    print ' '.join(c)
