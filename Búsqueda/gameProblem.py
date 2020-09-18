 
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''


from simpleai.search import SearchProblem
# from simpleai.search import breadth_first,depth_first,astar,greedy
import simpleai.search
import math

class GameProblem(SearchProblem):

    # Object attributes, can be accessed in the methods below
    
    MAP=None
    POSITIONS=None
    INITIAL_STATE=None
    GOAL=None
    CONFIG=None
    AGENT_START=None
    SHOPS=None
    CUSTOMERS=None
    MAXBAGS = 2
    MOVES = ('West','North','East','South')

   # --------------- Common functions to a SearchProblem -----------------

    def actions(self, state): # devuelve las aplicaciones aplicables en un estado
	'''Returns a LIST of the actions that may be executed in this state
	'''
	#Comenzamos por establecer los limites por los que tendra que regirse el repartidor
	limitedcha= self.CONFIG['map_size'][0]
	limiteabajo= self.CONFIG['map_size'][1]

	#creamos la lista de acciones que se generara nueva para cada estado, teniendo diferentes
	#posibilidades para cada uno de ellos
	acciones = []
	#siempre que haya espacio y estemos en una pizzeria podremos coger pizzas
	if state[0] in self.POSITIONS["pizza"] and state[1]<self.MAXBAGS:
		    acciones.append('CogerPipsa')

	#comprobamos si el estado en el que estamos es la casilla de algun cliente y si quedan pizzas por repartir
	for i in range (1,4):
		if ((state[0],i) in state[2]) and state[1]>0:
			acciones.append('DejarPipsa')
	
	#siempre que no se salga de los limites de las casillas, y no sea una casilla de edificio el
	#repartidor puede moverse por esa casilla
	if (((state[0][0], state[0][1]-1) in self.POSITIONS['building']) == False and (state[0][0]>=0 and state[0][0]<limitedcha and (state[0][1]-1)>=0 and (state[0][1]-1)<limiteabajo)):
		acciones.append('North')
	
	if (((state[0][0], state[0][1]+1) in self.POSITIONS['building']) == False and (state[0][0]>=0 and state[0][0]<limitedcha and (state[0][1]+1)>=0 and (state[0][1]+1)<limiteabajo)):
		acciones.append('South')
	
	if (((state[0][0]+1, state[0][1]) in self.POSITIONS['building']) == False and ((state[0][0]+1)>=0 and (state[0][0]+1)<limitedcha and state[0][1]>=0 and state[0][1]<limiteabajo)):
		acciones.append('East')
	
	if (((state[0][0]-1, state[0][1]) in self.POSITIONS['building']) == False and ((state[0][0]-1)>=0 and (state[0][0]-1)<limitedcha and state[0][1]>=0 and state[0][1]<limiteabajo)):
		acciones.append('West')
	
	#printeamos el estado en el que estamos y las acciones que realiza
	print state, acciones
	
	return acciones
    
    def result(self, state, action):
        '''Returns the state reached from this state when the given action is executed
        '''
	#con las acciones de moviemiento el repartidor de dirige hacia una nueva posicion
	if (action == 'North'):
		next_state = ((state[0][0],state[0][1]-1), state[1], state[2])
	
	if (action == 'South'):
		next_state = ((state[0][0],state[0][1]+1), state[1], state[2])
	
	if (action == 'East'):
		next_state = ((state[0][0]+1,state[0][1]), state[1], state[2])
	
	if (action == 'West'):
		next_state = ((state[0][0]-1,state[0][1]), state[1], state[2])

	#al coger pizzas tan solo se cogen de una en una y aumenta nuestro state[1] que
    #que es la cantidad de pizza que el repartidor lleva en un determinado momento
	if (action == 'CogerPipsa'):
		next_state = ((state[0][0],state[0][1]), state[1]+1, state[2])

	#el state[2] es la tupla de tuplas con la ubicacion de un cliente y el numero de pizzas
	#a repartir en dicha casilla, dado que un estado no se puede modificar sino que debe 
	#generarse uno nuevo, con esta accion se crea un nuevo estado basandose en el anterior
	#que disminuira en 1 a la cantidad de pizzas a entregar en esa casilla cliente y dejando
	#el resto igual.
	if (action == 'DejarPipsa'):
		new_state = ()
		for elem in state[2]:
			if elem[0] == state[0]:
				new_state = new_state + ((elem[0],elem[1]-1),)
			else:
				new_state = new_state + (elem,)
		
		next_state = ((state[0][0],state[0][1]), state[1]-1, new_state)

	return next_state
        
    def is_goal(self, state):
        '''Returns true if state is the final state
        '''
	    #el estado final sera aquel definido en un inicio con la funcion setup
        if (state == self.GOAL):
            return True

        return False


    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''    
        #en caso de que solo haya casillas street el coste de moverse por ellas sera
        #tan solo de 1, mientras que si hay casillas de otro tipo el coste variara
        #dependiendo del terreno.
        #Primero, sera necesario comprobar que existe un terreno en POSITIONS y luego,
        #se ve si el estado que comprobamos se encuentra en ese tipo de lista.
        #Ademas, al coste final se le aniadira por cada pizza que lleve encima un coste
        #extra por llevarla
        costs = 1
        if ('sea' in self.POSITIONS):
            if (state[0] in self.POSITIONS['sea']): #s
                costs = 10
        if ('plain' in self.POSITIONS):
            if (state[0] in self.POSITIONS['plain']): #p
                costs = 5
        if ('desert' in self.POSITIONS):
            if (state[0] in self.POSITIONS['desert']): #d
                costs = 9
        if ('forest' in self.POSITIONS):
            if (state[0] in self.POSITIONS['forest']): #f
                costs = 3
        if ('hill' in self.POSITIONS):
            if (state[0] in self.POSITIONS['hill']): #h
                costs = 8
        return costs + state[1]

    def heuristic(self, state):
        '''Returns the heuristic for `state`
        ''' 
        #HEURISTICA DE MANHATTAN CON COSTES INTERMEDIOS.
        #Seria necesario comentarla entera para la parte basica
        #creamos una tupla de minimos que en un inicio esta vacia
        minimo = ()  
        #comprobamos para cada cliente en el estado[2] 
        for cliente in state[2]:
        #si dicho cliente tiene pedidos pendientes
            if cliente[1] > 0:
            #comprobamos si el repartidor lleva pizzas encima
                if(state[1]==0):
                #en caso de que no lleve pizzas encima comprobamos la heuristica de manhattan para 
                #cada pizzeria, introduciendo cada valor en una tupla de minimos y luego hacemos return
                #del minimo de esos numeros
                    for elem in self.POSITIONS['pizza']:
                        heuristica = abs(state[0][0]-elem[0]) + abs(state[0][1]-elem[1]) 
                        minimo = minimo + (heuristica,)
                    return min(minimo)
                #en el caso de que si lleve pizza el repartidor calculamos la heuristica de manhattan
                #para cada cliente desde el estado actual, introduciendo cada valor en la tupla de minimos
                heuristica = abs(state[0][0]-cliente[0][0]) + abs(state[0][1]-cliente[0][1])
        #en el caso de que no quede ningun cliente por atender implica que tan solo nos queda ir 
        #a nuestra casilla de fin por lo que se hara la heuristica de manhattan para la posicion
        #final
        if(minimo == ()):
            return (abs(state[0][0]-self.GOAL[0][0]) + abs(state[0][1]-self.GOAL[0][1]))
        #se hace return de la mas baja de las heuristicas
        return min(minimo)
        
        #HEURISTICA DE MANHATTAN para la parte basica   
        manhattan = abs(state[0][0]-self.GOAL[0][0]) + abs(state[0][1]-self.GOAL[0][1])
        #HEURISTICA DE MAXIMOS entre las x y las y
        maximum = max(abs(state[0][0]-self.GOAL[0][0]), abs(state[0][1]-self.GOAL[0][1]))
        #HEURISTICA DE MINIMOS entre las x y las y
        minimum = min(abs(state[0][0]-self.GOAL[0][0]), abs(state[0][1]-self.GOAL[0][1]))
        return manhattan


    def setup (self): #definir aqui estado inicial, final y algoritmo de busqueda
        '''This method must create the initial state, final state (if desired) and specify the algorithm to be used.
           This values are later stored as globals that are used when calling the search algorithm.
           final state is optional because it is only used inside the is_goal() method

           It also must set the values of the object attributes that the methods need, as for example, self.SHOPS or self.MAXBAGS
        '''	
        #creamos tuplas de clientes y fin que se usaran para crear nuestro state[2] que consiste
        #en saber las casillas en las que hay un cliente y cuantas pizzas hay que entregar en cada una
        #de dichas casillas.
        #Para clientes recorreremos POSITIONS en busqueda de las casillas de clientes, cogiendo si 
        #posicion y aniadiendo el numero de pizzas dependiendo que tipo de customer se haya buscado
        #Para fin, haremos la misma busqueda pero los pedidos pendientes deben estar a 0
        clientes = ()
        fin = ()
        if 'customer1' in self.POSITIONS:
        	for quantity in range (0, len(self.POSITIONS['customer1'])):
        		clientes = clientes + (((self.POSITIONS['customer1'][quantity]), 1),)
        if 'customer2' in self.POSITIONS:
        	for quantity in range (0, len(self.POSITIONS['customer2'])):
        		clientes = clientes + (((self.POSITIONS['customer2'][quantity]), 2),)
        if 'customer3' in self.POSITIONS:
        	for quantity in range (0, len(self.POSITIONS['customer3'])):
        		clientes = clientes + (((self.POSITIONS['customer3'][quantity]), 3),)
        if 'customer1' in self.POSITIONS:
        	for quantity in range (0, len(self.POSITIONS['customer1'])):
        		fin = fin + (((self.POSITIONS['customer1'][quantity]), 0),)
        if 'customer2' in self.POSITIONS:
        	for quantity in range (0, len(self.POSITIONS['customer2'])):
        		fin = fin + (((self.POSITIONS['customer2'][quantity]), 0),)
        if 'customer3' in self.POSITIONS:
        	for quantity in range (0, len(self.POSITIONS['customer3'])):
        		fin = fin + (((self.POSITIONS['customer3'][quantity]), 0),)
	

        #Establecemos las casillas de inicio y de fin, siendo la casilla de inicio igual a la de final(state[0])
        #teniendo que llevar 0 pizzas encima state[1] y las tuplas de clientes y fin insertadas en el estado 
        #correspondiente
        casillainit = ((self.AGENT_START), 0, clientes)
        casillafin = ((self.AGENT_START), 0, fin)
        print '\nMAP: ', self.MAP, '\n'
        print 'POSITIONS: ', self.POSITIONS, '\n'
        print 'CONFIG: ', self.CONFIG, '\n'
        
        initial_state = casillainit
        final_state= casillafin
        #el algoritmo que produce los mejores resultados es el de A*
        algorithm= simpleai.search.astar
        #Asimismo establecemos la cantidad de tiendas que hay
        self.SHOPS = len(self.POSITIONS['pizza'])
        #y la cantidad de pizzas como maximo que puede llevar el repartidor
        self.MAXBAGS=2

        return initial_state,final_state,algorithm
        
    def printState (self,state):
        '''Return a string to pretty-print the state '''
        #imprimimos el estado actual indicando que es cada cosa
        pps= 'casilla: ' ,state[0], ' carrying: ' ,state[1], ' clients: ', state[2]
        return (pps)

    def getPendingRequests (self,state):
        ''' Return the number of pending requests in the given position (0-N). state
            MUST return None if the position is not a customer.
            This information is used to show the proper customer image.
        '''
        #dependiendo de la casilla en la que estemos si es un cliente, y por lo tanto se encuentra
        #en nuestro state[2], devolvera el numero de pizzas pedidas que le quedan por ser entregadas
        #en caso contrario devolvera None
        for i in range (0,4):
       		if ((state[0]),i) in state[2]:
        		return i
	
        return None

    # -------------------------------------------------------------- #
    # --------------- DO NOT EDIT BELOW THIS LINE  ----------------- #
    # -------------------------------------------------------------- #

    def getAttribute (self, position, attributeName):
        '''Returns an attribute value for a given position of the map
           position is a tuple (x,y)
           attributeName is a string
           
           Returns:
               None if the attribute does not exist
               Value of the attribute otherwise
        '''
        tileAttributes=self.MAP[position[0]][position[1]][2]
        if attributeName in tileAttributes.keys():
            return tileAttributes[attributeName]
        else:
            return None

    def getStateData (self,state):
        stateData={}
        pendingItems=self.getPendingRequests(state)
        if pendingItems >= 0:
            stateData['newType']='customer{}'.format(pendingItems)
        return stateData
        
    # THIS INITIALIZATION FUNCTION HAS TO BE CALLED BEFORE THE SEARCH
    def initializeProblem(self,map,positions,conf,aiBaseName):
        self.MAP=map
        self.POSITIONS=positions
        self.CONFIG=conf
        self.AGENT_START = tuple(conf['agent']['start'])

        initial_state,final_state,algorithm = self.setup()
        if initial_state == False:
            print ('-- INITIALIZATION FAILED')
            return True
      
        self.INITIAL_STATE=initial_state
        self.GOAL=final_state
        self.ALGORITHM=algorithm
        super(GameProblem,self).__init__(self.INITIAL_STATE)
            
        print ('-- INITIALIZATION OK')
        return True
        
    # END initializeProblem 

