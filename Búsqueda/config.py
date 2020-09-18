#este fichero nos permite configurtar cosas del juego
configuration = {
"text_size": 300, 
"tile_size": 80, 
"type": "load", #random, se crea un grip aleatorio del que especifica el tamanio de map size
"seed": None,
"file": "./student/map.txt", #carga la ruta del fichero 
"map_size": [10, 7], #columnas y filas
"delay": 0.05,
"debugMap": False,
"debug": False,
"save": False, #True cuando cargamos un mapa aleatorio se guarda en un map.txt, y luego lo cargamos con un load
"hazards": False,
"basicTile": "street",
"maxBags": 2, #maxima carga del repartidor de pipsas menos el numero que me como yo
"agent":{
    "graphics":{ 
        "default": "game/graphics/logistics/bicycle100.png"
        },
    "id": "agent",
    "marker": 'A',
    "start": [0,0],
    },
"maptiles": { #casilla por donde se puede ir
    "street": {
        "graphics":{ 
            "default": "game/graphics/logistics/street100.png",
            "traversed": "game/graphics/logistics/street100Traversed.png"
            },
        "id":  "street",
        "marker": 'T',
        "num": 0, #casillas de ese tipo cuando se crea un mapa aleatorio
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "pizza": {
        "graphics":{ 
            "default": "game/graphics/logistics/restaurant100.png",
            "traversed": "game/graphics/logistics/restaurant100.png"
            },
        "id":  "pizza",
        "marker": 'Z',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "customer0": { #casillas de tipo cliente con sus atributos, hay de tres tipos de clientes, con cuantas pipsas piden.
        "graphics":{ 
            "default": "game/graphics/logistics/customer100.png",
            "traversed": "game/graphics/logistics/customer100.png"
            },
        "id":  "customer0",
        "marker": '0',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 0},
        },
    "customer1": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100_1.png",
            "traversed": "game/graphics/logistics/customer100_1.png"
            },
        "id":  "customer1",
        "marker": '1',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 1},
        },
    "customer2": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100_2.png",
            "traversed": "game/graphics/logistics/customer100_2.png"
            },
        "id":  "customer2",
        "marker": '2',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 2},
        },
    "customer3": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100_3.png",
            "traversed": "game/graphics/logistics/customer100_3.png"
            },
        "id":  "customer3",
        "marker": '3',
        "num": 3,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 3},
        },
    "start": {
        "graphics":{ 
            "default": "game/graphics/logistics/base100.png",
            "traversed": "game/graphics/logistics/base100.png"
            },
        "id":  "start",
        "marker": 'W',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "building": {
        "graphics":{ 
            "default": "game/graphics/logistics/building100.png",
            "traversed": "game/graphics/logistics/building100.png"
            },
        "id":  "building",
        "marker": 'X',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "blocked": True},
        },
    "hill": {
        "graphics":{
            "default": "game/graphics/terrains/hills100.png",
            "traversed": "game/graphics/terrains/hillsTraversed100.png"
            },
        "id":  "hill",
        "marker": 'H',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 8},
        },
    "forest": {
        "graphics":{
            "default": "game/graphics/terrains/forest100.png",
            "traversed": "game/graphics/terrains/forestTraversed100.png"
            },
        "id":  "forest",
        "marker": 'F',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 3},
        },
    "desert": {
        "graphics":{
            "default": "game/graphics/terrains/desert100.png",
            "traversed": "game/graphics/terrains/desertTraversed100.png"
            },
        "id":  "desert",
        "marker": 'D',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 9},
        },
    "plains": {
        "graphics":{
            "default": "game/graphics/terrains/plains100.png",
            "traversed": "game/graphics/terrains/plainsTraversed100.png"
            },
        "id":  "plain",
        "marker": 'P',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 5},
        },
    "seas": {
        "graphics":{
            "default": "game/graphics/terrains/sea100.png",
            "traversed": "game/graphics/terrains/seaTraversed100.png"
            },
        "id":  "sea",
        "marker": 'S',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 10},
        }             
    }   
}
