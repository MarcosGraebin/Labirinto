from maze import Maze
from state import State
from cardinal import *

class Problem:
    """Representação de um problema a ser resolvido por um algoritmo de busca clássica.
    A formulação do problema - instância desta classe - reside na 'mente' do agente."""


    def __init__(self):
        self.initialState = State(0,0)
        self.goalState = State(0,0)

    def createMaze(self, maxRows, maxColumns):
        """Este método instancia um labirinto - representa o que o agente crê ser o labirinto.
        As paredes devem ser colocadas fora desta classe porque este.
        @param maxRows: máximo de linhas do labirinto.
        @param maxColumns: máximo de colunas do labirinto."""
        self.mazeBelief = Maze(maxRows, maxColumns)
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.cost = [[0.0 for j in range(maxRows*maxColumns)]for i in range(8)]

    def defInitialState(self, row, col):
        """Define o estado inicial.
        @param row: linha do estado inicial.
        @param col: coluna do estado inicial."""
        self.initialState.row = row
        self.initialState.col = col

    def defGoalState(self, row, col):
        """Define o estado objetivo.
        @param row: linha do estado objetivo.
        @param col: coluna do estado objetivo."""
        self.goalState.row = row
        self.goalState.col = col

    def suc(self, state, action):
        """Função sucessora: recebe um estado e calcula o estado sucessor ao executar uma ação.
        @param state: estado atual.
        @param action: ação a ser realizado a partir do estado state.
        @return estado sucessor"""
        row = state.row
        col = state.col

        if action == NO or action == N or action == NE:
            row -= 1
        elif action == SE or action == S or action == SO:
            row += 1

        if action == NE or action == L or action == SE: #vai para leste
            col += 1
        elif action == SO or action == O or action == NO:
            col += 1

        # @TODO T_AAFP
        
        return State(row, col)

    def possibleActions(self, state):
        """Retorna as ações possíveis de serem executadas em um estado.
        O valor retornado é um vetor de inteiros.
        Se o valor da posição é -1 então a ação correspondente não pode ser executada, caso contrário valerá 1.
        Exemplo: se retornar [-1, -1, -1, 1, 1, -1, -1, -1] apenas as ações 3 e 4 podem ser executadas, ou seja, apenas SE e S.
        @param state: estado atual.
        @return ações possíveis"""
        actions = [1,1,1,1,1,1,1,1] # Supõe que todas as ações são possíveis
        
        row = state.row
        col = state.col

        if state.row == self.maxRows: #não vai para o sul
            actions[3] = -1
            actions[4] = -1
            actions[5] = -1
        elif state.row == 0: #não vai para o norte
            actions[-1] = -1
            actions[0] = -1
            actions[1] = -1

        if state.col == self.maxColumns: #não vai para o leste
            actions[1] = -1
            actions[2] = -1
            actions[3] = -1
        elif state.col == 0: #não vai para o oeste
            actions[-1] = -1
            actions[-2] = -1
            actions[-3] = -1

        #if self.maze.walls[self.row + 1] == 1: #não vai para o sul
        #    actions[4] = -1
        

    

        # @TODO T_AAFP 

        return actions

    def possibleActionsWithoutCollaterals(self, state):
        """Retorna as ações possíveis de serem executadas em um estado, desconsiderando movimentos na diagonal.
        O valor retornado é um vetor de inteiros.
        Se o valor da posição é -1 então a ação correspondente não pode ser executada, caso contrário valerá 1.
        Exemplo: se retornar [1, -1, -1, -1, -1, -1, -1, -1] apenas a ação 0 pode ser executada, ou seja, apena N.
        @param state: estado atual.
        @return ações possíveis"""
        
        actions = [1,-1,1,-1,1,-1,1,-1] # Supõe que todas as ações (menos na diagonal) são possíveis

        # @TODO T_AAFP


        return actions

    def getActionCost(self, action):
        """Retorna o custo da ação.
        @param action:
        @return custo da ação"""
        if (action == N or action == L or action == O or action == S):
            return 1.0
        else:
            return 1.5

    def goalTest(self, currentState):
        """Testa se alcançou o estado objetivo.
        @param currentState: estado atual.
        @return True se o estado atual for igual ao estado objetivo."""
         # @TODO T_AAFP
        return true # Utilizar Operador de igualdade definido em __eq__ no arquivo state.py
