h_dict = {}
graph_dict = {}
total_cost = {}


def readFile():
    flag = 0
  # Graph file format: 
      # Node	Neighboring_Node	Actual_Cost_btw_the_Two_Nodes	 Node_Heuristic_Cost
    with open("Graph.txt", "r") as txt_file:
        Lines = txt_file.readlines()
    node = 'A'
    l1 = []
    for line in Lines:
        if flag != 0:
            content = line.split()
            # print(content)
            h_dict[content[0]] = int(content[3])
            current_node = content[0]
            if node != current_node:
                graph_dict[node] = l1
                l1 = []
                node = current_node
            l1.append([content[1], int(content[2])])
        flag = 1
    graph_dict[node] = l1


def getPath(start, goal):
    current_path = start
    current_path_totalCost = 0
    while True:
        # print(current_path)
        last_node = current_path[-1]
        children_nodes = graph_dict[last_node]
        for child in children_nodes:
            if child[0] == goal:
                return current_path+goal, current_path_totalCost+child[1]
            total_cost[current_path+child[0]
                       ] = current_path_totalCost+child[1]+h_dict[child[0]]
        current_path = min(total_cost, key=total_cost.get)
        current_path_totalCost = total_cost[current_path] - \
            h_dict[current_path[-1]]
        del total_cost[current_path]



readFile()

current_path, current_path_totalCost = getPath('A', 'J')
print(current_path)
print(current_path_totalCost)
