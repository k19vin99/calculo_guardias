import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula de Haversine para calcular la distancia en kilómetros
    R = 6371  # Radio de la Tierra en km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def calcular_distancia(lat1, lon1, lat2, lon2):
    if not all([lat1, lon1, lat2, lon2]):
        return float('inf')  # Retorna infinito si alguna coordenada falta
    
    # Convertir grados a radianes
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Fórmula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radio de la Tierra en kilómetros
    return round(c * r, 2)  # Retorna la distancia en kilómetros


