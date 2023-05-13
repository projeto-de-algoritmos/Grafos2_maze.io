from random import randint
from pyamaze.pyamaze import maze,agent,COLOR,textLabel
from dijsktra import dijkstra

if __name__=='__main__':
    #  Define o tamanho do labirinto
    myMaze=maze(7,9)

    # Define o ponto de chegada do labirinto e o quão juntas as paredes vão ser
    myMaze.CreateMaze(7,9,loopPercent=200)
    #print(myMaze.maze_map)

    # Cria um labirinto a partir de um arquivo .csv
    # myMaze.CreateMaze(loadMaze='dijkMaze.csv')

    # Define em qual região vai receber um valor maior que 1
    h1=agent(myMaze,1,randint(2,9),color=COLOR.red)
    h2=agent(myMaze,1,randint(2,9),color=COLOR.red)
    h3=agent(myMaze,1,randint(2,9),color=COLOR.red)
    h4=agent(myMaze,2,randint(1,9),color=COLOR.red)
    h5=agent(myMaze,2,randint(1,9),color=COLOR.red)
    h6=agent(myMaze,2,randint(1,9),color=COLOR.red)
    h7=agent(myMaze,3,randint(1,9),color=COLOR.red)
    h8=agent(myMaze,3,randint(1,9),color=COLOR.red)
    h9=agent(myMaze,3,randint(1,9),color=COLOR.red)
    h10=agent(myMaze,4,randint(1,9),color=COLOR.red)
    h11=agent(myMaze,4,randint(1,9),color=COLOR.red)
    h12=agent(myMaze,4,randint(1,9),color=COLOR.red)
    h13=agent(myMaze,5,randint(1,9),color=COLOR.red)
    h14=agent(myMaze,5,randint(1,9),color=COLOR.red)
    h15=agent(myMaze,5,randint(1,9),color=COLOR.red)
    h16=agent(myMaze,6,randint(1,9),color=COLOR.red)
    h17=agent(myMaze,6,randint(1,9),color=COLOR.red)
    h18=agent(myMaze,6,randint(1,9),color=COLOR.red)
    h19=agent(myMaze,7,randint(1,8),color=COLOR.red)
    h20=agent(myMaze,7,randint(1,8),color=COLOR.red)
    h21=agent(myMaze,7,randint(1,8),color=COLOR.red)

    # Define a o valor que uma região recebeu
    h1.cost=randint(10,25)
    h2.cost=randint(10,25)
    h3.cost=randint(10,25)
    h4.cost=randint(10,25)
    h5.cost=randint(10,25)
    h6.cost=randint(10,25)
    h7.cost=randint(10,25)
    h8.cost=randint(10,25)
    h9.cost=randint(10,25)
    h10.cost=randint(10,25)
    h11.cost=randint(10,25)
    h12.cost=randint(10,25)
    h13.cost=randint(10,25)
    h14.cost=randint(10,25)
    h15.cost=randint(10,25)
    h16.cost=randint(10,25)
    h17.cost=randint(10,25)
    h18.cost=randint(10,25)
    h19.cost=randint(10,25)
    h20.cost=randint(10,25)
    h21.cost=randint(10,25)



    # Define onde o labirinto inicia e passa as regiões que possui distância maior que 1
    path,c = dijkstra(myMaze,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,start=(1,1))
    textLabel(myMaze,'Total Cost',c)

    # Cria a função que mostra o menor caminho sendo construído
    a = agent(myMaze,1,1,color=COLOR.cyan,filled=True,footprints=True)
    myMaze.tracePath({a:path})

    # Inicia a aplicação
    myMaze.run()