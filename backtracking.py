from time import time
iterador=0
def is_safe(n, graph, colors, c):
    # Iterate trough adjacent vertices
    # and check if the vertex color is different from c
    for i in range(n):
        if graph[n][i] and c == colors[i]: return False
    return True

# n = vertex nb
def graphColoringUtil(graph, color_nb, colors, n):
    # Check if all vertices are assigned a color
    global iterador
    iterador += 1 
    if color_nb+1 == n :
        return True

    # Trying differents color for the vertex n
    for c in range(1, color_nb+1):
        # Check if assignment of color c to n is possible
        if is_safe(n, graph, colors, c):
            # Assign color c to n
            colors[n] = c
            # Recursively assign colors to the rest of the vertices
            if graphColoringUtil(graph, color_nb, colors, n+1): return True
            # If there is no solution, remove color (BACKTRACK)
            colors[n] = 0

#nb of vertex
vertex_nb = 5
# nb of colors
color_nb = 3
# Initiate vertex colors
colors = [0] * vertex_nb

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
]

def totalTime():
    if graphColoringUtil(graph, color_nb, colors, 1):
        print (colors)
        print("Las iteraciones fueron: ", iterador)
        print("Número Cromático: ", color_nb)
    else:
        print ("No hay Soluciones")
start_time = time()
totalTime()
elapsed_time = time() - start_time
print("Tiempo de ejecución: %.10f segundos." % elapsed_time)

        