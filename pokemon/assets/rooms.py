rooms = {
        'Pallet Town' : { 
            'directions' : {"north": "Route 1","south": "Route 21"},
            'items'  : [ "Rainbow Scale" ],
            'pokemon': {'level': [0,5],
                'ids': [1,2,3,4,5,6]}
            },
        'Route 1' : {
            'directions' : {"north": "Viridian City", "south": "Pallet Town"},
            'items'  : [ "Rainbow Scale" ],
            'pokemon': {'level': [0,5],
                'ids': [1,2,3,4,5,6]}
            },

        'Viridian City' : {
            'directions' : {"north": "Pallet Town", "south": "Route 1"},
            'items'  : [ "Rainbow Scale" ],
            'pokemon': {'level': [0,5],
                'ids': [1,2,3,4,5,6]}
            },

        'Route 21' : {
            'directions' : {},
            'items'  : [ "Rainbow Scale" ],
            'pokemon': {'level': [0,5],
                'ids': [1,2,3,4,5,6]}
            }
        }
