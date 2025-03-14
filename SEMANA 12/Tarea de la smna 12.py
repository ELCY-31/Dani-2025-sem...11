# Definir las ciudades y los días de la semana
nombres_ciudades = ["Loja", "Quito", "Orellana", "Guayaquil" ]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Matriz 3D para las temperaturas
matriz_temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "Temp": 30},
            {"day": "Martes", "Temp": 29},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 32},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 25},
            {"day": "Domingo", "Temp": 39}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 25},
            {"day": "Martes", "Temp": 29},
            {"day": "Miércoles", "Temp": 27},
            {"day": "Jueves", "Temp": 38},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 23},
            {"day": "Domingo", "Temp": 39}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 31},
            {"day": "Martes", "Temp": 26},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 32},
            {"day": "Viernes", "Temp": 39},
            {"day": "Sábado", "Temp": 25},
            {"day": "Domingo", "Temp": 39}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 35},
            {"day": "Martes", "Temp": 39},
            {"day": "Miércoles", "Temp": 38},
            {"day": "Jueves", "Temp": 22},
            {"day": "Viernes", "Temp": 28},
            {"day": "Sábado", "Temp": 26},
            {"day": "Domingo", "Temp": 39}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "Temp": 29,},
            {"day": "Martes", "Temp": 36,},
            {"day": "Miércoles", "Temp": 30,},
            {"day": "Jueves", "Temp": 27,},
            {"day": "Viernes", "Temp": 34,},
            {"day": "Sábado", "Temp": 38,},
            {"day": "Domingo", "Temp": 25,}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 32,},
            {"day": "Martes", "Temp": 29,},
            {"day": "Miércoles", "Temp": 40,},
            {"day": "Jueves", "Temp": 26,},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 30,},
            {"day": "Domingo", "Temp": 37,}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 31},
            {"day": "Martes", "Temp": 26},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 32},
            {"day": "Viernes", "Temp": 39},
            {"day": "Sábado", "Temp": 25},
            {"day": "Domingo", "Temp": 39}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 35},
            {"day": "Martes", "Temp": 39},
            {"day": "Miércoles", "Temp": 38},
            {"day": "Jueves", "Temp": 22},
            {"day": "Viernes", "Temp": 28},
            {"day": "Sábado", "Temp": 26},
            {"day": "Domingo", "Temp": 39}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "Temp": 27},
            {"day": "Martes", "Temp": 34},
            {"day": "Miércoles", "Temp": 40},
            {"day": "Jueves", "Temp": 27},
            {"day": "Viernes", "Temp": 35},
            {"day": "Sábado", "Temp": 29},
            {"day": "Domingo", "Temp": 39}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 36},
            {"day": "Martes", "Temp": 39},
            {"day": "Miércoles", "Temp": 27},
            {"day": "Jueves", "Temp": 28},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 33},
            {"day": "Domingo", "Temp": 40}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 21},
            {"day": "Martes", "Temp": 36},
            {"day": "Miércoles", "Temp": 38},
            {"day": "Jueves", "Temp": 40},
            {"day": "Viernes", "Temp": 22},
            {"day": "Sábado", "Temp": 20},
            {"day": "Domingo", "Temp": 30}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 40},
            {"day": "Martes", "Temp": 25},
            {"day": "Miércoles", "Temp": 40},
            {"day": "Jueves", "Temp": 20},
            {"day": "Viernes", "Temp": 24},
            {"day": "Sábado", "Temp": 36},
            {"day": "Domingo", "Temp": 39}
        ]
    ],
    [  # Ciudad 4
        [  # Semana 1
            {"day": "Lunes", "Temp": 30},
            {"day": "Martes", "Temp": 29},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 38},
            {"day": "Viernes", "Temp": 32},
            {"day": "Sábado", "Temp": 25},
            {"day": "Domingo", "Temp": 39}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 35},
            {"day": "Martes", "Temp": 39},
            {"day": "Miércoles", "Temp": 30},
            {"day": "Jueves", "Temp": 40},
            {"day": "Viernes", "Temp": 21},
            {"day": "Sábado", "Temp": 23},
            {"day": "Domingo", "Temp": 40}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 21},
            {"day": "Martes", "Temp": 20},
            {"day": "Miércoles", "Temp": 29},
            {"day": "Jueves", "Temp": 36},
            {"day": "Viernes", "Temp": 39},
            {"day": "Sábado", "Temp": 35},
            {"day": "Domingo", "Temp": 29}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 25},
            {"day": "Martes", "Temp": 40},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 32},
            {"day": "Viernes", "Temp": 40},
            {"day": "Sábado", "Temp": 26},
            {"day": "Domingo", "Temp": 40}
        ]
    ]
]
# Calcular el promedio de las temperaturas para cada ciudad por semana
promedios_temperaturas = []

for ciudad in matriz_temperaturas:
    promedios_ciudad = []
    for semana in ciudad:
        suma_temperaturas = sum(dia["Temp"] for dia in semana)
        promedio_semana = suma_temperaturas / len(semana)
        promedios_ciudad.append(promedio_semana)
    promedios_temperaturas.append(promedios_ciudad)

# Mostrar el promedio de las temperaturas para cada ciudad y semana
for idx_ciudad, promedios_ciudad in enumerate(promedios_temperaturas):
    print(f"Promedio de temperaturas para la Ciudad de {nombres_ciudades[idx_ciudad]}:")
    for idx_semana, promedio in enumerate(promedios_ciudad):
        print(f"  Semana {idx_semana + 1}: {promedio:.2f}°C")