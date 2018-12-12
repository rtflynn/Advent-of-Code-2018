import re
my_file = open(r"C:\Users\beera\Desktop\Advent of Coding\day7_input.txt")
instruction_graph = []
for instruction in my_file.readlines():
    parsed_instruction = re.split(' |\n', instruction)
    first_step = parsed_instruction[1]
    second_step = parsed_instruction[7]
    instruction_graph.append((first_step, second_step))



vertices = []
for edge in instruction_graph:
    if edge[0] not in vertices:
        vertices.append(edge[0])
    if edge[1] not in vertices:
        vertices.append(edge[1])
    vertices = sorted(vertices)

remaining_vertex_list = vertices.copy()
unvisited_edges = instruction_graph.copy()


def has_no_remaining_earlier_steps(vert, edge_set):
    for edge in edge_set:
        if vert == edge[1]:
            return False
    return True



def determine_next_step(remaining_vertex_list, unvisited_edges):
    for vertex in remaining_vertex_list:
        if has_no_remaining_earlier_steps(vertex, unvisited_edges):
            remaining_vertex_list.remove(vertex)
            edges_to_remove = []
            for edge in unvisited_edges:
                if edge[0] == vertex:
                    edges_to_remove.append(edge)
            for edge in edges_to_remove:
                unvisited_edges.remove(edge)        # We can't just remove 'as we go' without causing serious issues.

            return vertex

instruction_order = ""
while remaining_vertex_list:
    instruction_order += determine_next_step(remaining_vertex_list, unvisited_edges)

print("Project 1 answer:  " + instruction_order)


remaining_vertex_list = vertices.copy()
unvisited_edges = instruction_graph.copy()

vertices_being_worked_on_dict = {}
vertices_being_worked_on = []
workers_active = 0
time_elapsed = 0


def time_to_do_step(some_char):
    return ord(some_char) - 4


def assign_worker(remaining_vertex_list, unvisited_edges, workers_active, vertices_being_worked_on, vertices_being_worked_on_dict):
    if workers_active >= 5:
        pass
    for vertex in remaining_vertex_list:
        if vertex not in vertices_being_worked_on:
            if has_no_remaining_earlier_steps(vertex, unvisited_edges):
                vertices_being_worked_on_dict[vertex] = time_to_do_step(vertex)
                vertices_being_worked_on.append(vertex)
                return True


def tick(remaining_vertex_list, unvisited_edges, workers_active, vertices_being_worked_on, vertices_being_worked_on_dict):
    vertices_to_remove = []
    for vertex in vertices_being_worked_on:
        vertices_being_worked_on_dict[vertex] -= 1
        if vertices_being_worked_on_dict[vertex] == 0:
            workers_active -= 1
            remaining_vertex_list.remove(vertex)
            vertices_to_remove.append(vertex)
            del vertices_being_worked_on_dict[vertex]
            edges_to_remove = []
            for edge in unvisited_edges:
                if edge[0] == vertex:
                    edges_to_remove.append(edge)
            for edge in edges_to_remove:
                unvisited_edges.remove(edge)
    for vertex in vertices_to_remove:
        vertices_being_worked_on.remove(vertex)


while remaining_vertex_list:
    while assign_worker(remaining_vertex_list, unvisited_edges, workers_active, vertices_being_worked_on, vertices_being_worked_on_dict):
        workers_active += 1

    tick(remaining_vertex_list, unvisited_edges, workers_active, vertices_being_worked_on, vertices_being_worked_on_dict)
    time_elapsed += 1


print("Project 2 answer:  " + str(time_elapsed))



