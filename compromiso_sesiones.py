"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programación (213022)
Fase 5 - Evaluación Final POA
Problema 1: Nivel de compromiso de sesiones de clientes

Estudiante: Kevin Lopera Puerta
Grupo: 213022A_2204

Descripción:
    Una matriz guarda las sesiones de clientes de una plataforma digital.
    Cada fila tiene el formato:
        [ID del cliente, Duración de la sesión (segundos), Número de clics]
    El programa recorre la matriz, clasifica cada sesión como "Alto",
    "Medio" o "Bajo" según su duración y sus clics, y muestra un informe
    con el ID del cliente y su clasificación final.
"""

# ---------------------------------------------------------------------
# Constantes: umbrales de la lógica de negocio
# (si la empresa cambia las reglas, solo se modifican aquí)
# ---------------------------------------------------------------------
DURACION_MIN_ALTO = 180   
CLICS_MIN_ALTO = 8        
DURACION_MAX_BAJO = 60    
CLICS_MAX_BAJO = 3        


# ---------------------------------------------------------------------
# Datos iniciales: matriz de sesiones (7 filas x 3 columnas)
# Columna 0 = ID del cliente, columna 1 = duración, columna 2 = clics
# ---------------------------------------------------------------------
sesiones = [
    ["CLI-001", 245, 12],   
    ["CLI-002", 45, 10],    
    ["CLI-003", 120, 5],   
    ["CLI-004", 200, 2],    
    ["CLI-005", 190, 8],   
    ["CLI-006", 310, 15],   
    ["CLI-007", 60, 3],     
]


def clasificar_compromiso(duracion, clics):
    """
    Recibe la duración (segundos) y el número de clics de una sesión
    y retorna su clasificación de compromiso: "Alto", "Medio" o "Bajo".

    Las condiciones se revisan en este orden:
      1. Primero se revisa "Alto" (deben cumplirse las DOS condiciones: and).
      2. Si no es Alto, se revisa "Bajo" (basta con UNA condición: or).
      3. Si no es ninguno de los anteriores, es "Medio" (caso por defecto).
    """
    if duracion > DURACION_MIN_ALTO and clics > CLICS_MIN_ALTO:
        clasificacion = "Alto"
    elif duracion < DURACION_MAX_BAJO or clics < CLICS_MAX_BAJO:
        clasificacion = "Bajo"
    else:
        clasificacion = "Medio"
    return clasificacion


def mostrar_informe(matriz):
    """
    Recorre la matriz de sesiones con un ciclo for, clasifica cada fila
    usando la función clasificar_compromiso e imprime el informe.
    También cuenta cuántas sesiones quedaron en cada nivel.
    """
    contador_alto = 0
    contador_medio = 0
    contador_bajo = 0

    print("=" * 62)
    print("      INFORME DE COMPROMISO DE SESIONES DE CLIENTES")
    print("=" * 62)
    print(f"{'ID Cliente':<12}{'Duración (s)':>14}{'Clics':>9}   {'Compromiso':<12}")
    print("-" * 62)

    for fila in matriz:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]

        nivel = clasificar_compromiso(duracion, clics)

        # Acumuladores: contar sesiones por nivel
        if nivel == "Alto":
            contador_alto += 1
        elif nivel == "Medio":
            contador_medio += 1
        else:
            contador_bajo += 1

        print(f"{id_cliente:<12}{duracion:>14}{clics:>9}   {nivel:<12}")

    print("-" * 62)
    print(f"Total de sesiones evaluadas: {len(matriz)}")
    print(f"  Compromiso Alto : {contador_alto}")
    print(f"  Compromiso Medio: {contador_medio}")
    print(f"  Compromiso Bajo : {contador_bajo}")
    print("=" * 62)


def main():
    """Función principal: inicia el programa."""
    mostrar_informe(sesiones)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
