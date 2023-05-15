# Inicia o algoritmo de dijkstra com busca em camadas para percorrer o labirinto
# matriz, obstáculos, nó inicial
def dijkstra(m,*h,start=None):
    #define nó incial
    if start is None:
        start=(m.rows,m.cols)

    #para cada obstáculo irá escolher a posição e o valor de custo
    hurdles=[(i.position,i.cost) for i in h]

    #celulas do labirinto são os nós (chave-valor)
    unvisited={n:float('inf') for n in m.grid}
    #custo zero para a primeira célula
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        #pega a célula com custo mínimo no dicionário
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        #verificar os 4 vizinhos (aqueles que são abertos)
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                #quando encontrar a célula filha, verificar se já está presente
                #caso positivo pularemos
                if childCell in visited:
                    continue
                
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]
                
                #caso contrário calcula o custo
                #se o custo calculado for melhor que o custo anterior substituimos os valores
                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        #remove célula atual dos não visitados
        unvisited.pop(currCell)
    
    #calcula o custo
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]