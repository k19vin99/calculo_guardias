import pulp

def optimizar_turnos(guardias, sucursales, turnos):
    # Modelo
    model = pulp.LpProblem("Optimización_Turnos", pulp.LpMinimize)

    # Variables
    x = pulp.LpVariable.dicts("x", ((g.id, s.id, t.id) for g in guardias for s in sucursales for t in turnos), cat="Binary")

    # Función objetivo: Minimizar costos de desplazamiento
    model += pulp.lpSum(x[g.id, s.id, t.id] * t.costo_desplazamiento for g in guardias for s in sucursales for t in turnos)

    # Restricciones:
    # 1. Cada turno debe ser cubierto
    for s in sucursales:
        for t in turnos:
            model += pulp.lpSum(x[g.id, s.id, t.id] for g in guardias) >= s.requerimiento_turnos

    # 2. Disponibilidad de guardias
    for g in guardias:
        model += pulp.lpSum(x[g.id, s.id, t.id] for s in sucursales for t in turnos) <= g.disponibilidad_horas

    # Resolver
    model.solve()

    return model
