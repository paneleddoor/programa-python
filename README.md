# Fase 5 – Evaluación Final POA · Fundamentos de Programación (UNAD)

**Estudiante:** Kevin Lopera Puerta  
**Grupo:** 213022A_2204  
**Problema:** 1 – Clasificación del nivel de compromiso de sesiones de clientes

## Descripción

Programa en Python que guarda en una matriz las sesiones de clientes de una plataforma digital con el formato:

```
[ID del cliente, Duración de la sesión (segundos), Número de clics]
```

Recorre la matriz con un ciclo `for`, clasifica cada sesión con la función `clasificar_compromiso()` y muestra un informe con el ID del cliente y su nivel de compromiso.

## Reglas de clasificación

| Nivel | Condición |
|-------|-----------|
| **Alto**  | duración > 180 s **y** clics > 8 |
| **Bajo**  | duración < 60 s **o** clics < 3 |
| **Medio** | cualquier otro caso |

## Cómo ejecutarlo

Requiere Python 3.8 o superior.

```bash
python compromiso_sesiones.py
```

## Salida esperada

```
ID Cliente    Duración (s)    Clics   Compromiso
CLI-001                245       12   Alto
CLI-002                 45       10   Bajo
CLI-003                120        5   Medio
CLI-004                200        2   Bajo
CLI-005                190        8   Medio
CLI-006                310       15   Alto
CLI-007                 60        3   Medio
Total de sesiones evaluadas: 7  (Alto: 2 · Medio: 3 · Bajo: 2)
```
