temperatures = {
    "sensor_1": 85.5,
    "sensor_2": 90.2,
    "sensor_3": 78.8,
    "sensor_4": 92.3
}

def trigger_alarm(temperatures, threshold = 80):
    lista = []
    for key, value in temperatures.items():
        if value > threshold:
            lista.append(key)
    return lista


