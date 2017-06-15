import queue
from collections import namedtuple

Edge = namedtuple('Edge',['vertex','weight'])

class Graph(object):  
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight, directed=True):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        if directed:
            self.adjacency_list[dest].append(Edge(source, weight))

    def add_edges(self,edge_list):
        for edge in edge_list:
            try:
                Graph.add_edge(self,edge[0],edge[1],edge[2],edge[3])
            except IndexError:
                Graph.add_edge(self,edge[0],edge[1],edge[2])

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v

def dijkstra(graph, source, dest):  
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]


def main():
    g = Graph(78)
    g.add_edges([(0,1,2),(1,2,4),(2,3,3),(3,4,2),(4,9,3),(9,10,6),(1,5,4),(5,6,1),(3,8,5),(9,12,5),(6,7,4),(7,8,3),(8,11,3),(11,12,4),(12,13,2),(13,14,1),(14,15,1),(7,17,0,False),(16,17,0,False),(6,16,1),(39,17,0,False),(8,39,1),(14,18,1),(18,19,2),(16,21,4),(27,39,3),(18,20,0,False),(33,20,0,False),(35,20,0,False),(19,33,1),(33,35,1),(19,31,1),(21,22,1),(22,23,1),(23,24,1),(24,25,1),(25,26,1),(26,27,1),(27,28,1),(28,29,1),(29,30,1),(30,31,1),(27,75,1),(75,32,2),(32,67,3),(67,42,3),(21,42,7),(32,68,2),(68,73,1),(38,73,2),(75,74,0,False),(75,76,0,False),(68,76,0,False),(68,71,0,False),(72,71,0,False),(67,72,0,False),(42,69,1),(69,70,0,False),(70,72,0,False),(30,34,1),(34,36,1),(35,36,1),(34,38,5),(36,77,1),(66,77,2),(38,41,2),(66,41,3),(69,44,4),(44,38,6),(44,55,2),(42,51,4),(51,52,1),(52,53,1),(53,54,2),(54,55,1),(35,37,2),(37,40,2),(40,77,1),(46,40,5),(41,45,1),(45,43,0,False),(46,43,0,False),(55,56,1),(56,57,1),(57,58,2),(58,59,1),(59,60,1),(48,60,1),(45,60,5),(46,47,2),(47,61,1),(60,61,2),(48,49,3),(61,49,1),(49,64,1),(49,63,2),(61,62,2),(62,50,0,False),(63,50,0,False),(63,65,0,False),(64,65,0,False)])
    homes = [0,1,21,22,23,24,25,26,27,28,29,30,31,11,52,53,54,56,57,58,59]
    homes_dict = {0:'45099',1:'45103',21:'45107',22:'45110/45111',23:'45114/45115',24:'45118/45119',25:'45122/45123',26:'45126/45127',27:'45134/45135',28:'45138/45139',29:'45142/45143',30:'45146/45147',31:'45150/45151',11:'The Mansion',52:'45154/45155',53:'45158/45159',54:'45162/45163',56:'45166/45167',57:'45170/45171',58:'45174/45175',59:'45178/45179'}
    stores = [2,4,10,17,20,37,43,50,55,65,66,71,72,74,76]
    stores_dict = {2:'Costco',4:'Wegmans',10:"Ford's Fish Shack",17:'Marshalls',20:'Tic-Tac-Pool',37:"Dunkin' Donuts",43:'Air and Space Museum',50:'Laser Tag',55:'Community Pool',65:'Spook House',66:'Metro',71:'Starbucks',72:'Target',74:'Home Depot',76:'Walmart'}
    seven11 = [5,13,47,70]
    for s in stores:
        for h in homes:
            print('Home(s): '+str(homes_dict[h])+', Store: '+str(stores_dict[s])+', Path: ' +str(dijkstra(g,h,s)[1]))
    for h in homes:
        print('Home(s): '+str(homes_dict[h])+', Store: 7-Eleven, Path: '+str(min([dijkstra(g,h,s)[1] for s in seven11])))

if __name__ == "__main__":
    main()
