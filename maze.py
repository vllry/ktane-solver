import networkx as nx



def horizontal(m, xstart, xend, y):
	for i in range(xstart, xend):
		m.add_edge(str(i)+str(y), str(i+1)+str(y))

def vertical(m, x, ystart, yend):
	for i in range(ystart, yend):
		m.add_edge(str(x)+str(i), str(x)+str(i+1))

maze = [nx.Graph(), nx.Graph(), nx.Graph(), nx.Graph(), nx.Graph(), nx.Graph(), nx.Graph(), nx.Graph(), nx.Graph()]
squares = []
for i in range(1,7):
	for j in range(1,7):
		squares.append(str(j)+str(i))
for i in range(0,9):
	maze[i].add_nodes_from(squares)

horizontal(maze[0], 1, 3, 1)
horizontal(maze[0], 4, 6, 1)
horizontal(maze[0], 2, 3, 2)
horizontal(maze[0], 4, 6, 2)
horizontal(maze[0], 2, 3, 3)
horizontal(maze[0], 4, 6, 3)
horizontal(maze[0], 2, 4, 4)
horizontal(maze[0], 5, 6, 4)
horizontal(maze[0], 1, 3, 5)
horizontal(maze[0], 4, 5, 5)
horizontal(maze[0], 1, 2, 6)
horizontal(maze[0], 3, 4, 6)
horizontal(maze[0], 5, 6, 6)

vertical(maze[0], 1, 1, 6)
vertical(maze[0], 2, 2, 3)
vertical(maze[0], 3, 1, 2)
vertical(maze[0], 3, 3, 4)
vertical(maze[0], 3, 5, 6)
vertical(maze[0], 4, 1, 2)
vertical(maze[0], 4, 3, 4)
vertical(maze[0], 4, 5, 6)
vertical(maze[0], 6, 2, 6)


def main(dic):
	Path = nx.shortest_path(maze[0], source = "11", target="55")
	print(Path)
main({})
