class Graph:
     def __init__(self):
          pass

     def add_edge(graph, vertex, edge):
          graph[vertex].append(edge)
          # graph[edge].append(vertex)

     def display_adj_list(graph):
          for vertex in range(len(graph)):
               print(f"{vertex}: ", end="")
               for edge in graph[vertex]:
                    print(edge, end=" ")
               print()

