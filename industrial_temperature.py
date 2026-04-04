temperatures = {
    "sensor_1": 85.5,
    "sensor_2": 90.2,
    "sensor_3": 78.8,
    "sensor_4": 92.3
}
threshold = 88

def trigger_alarm(temperatures, threshold):
    lista = []
    for key, value in temperatures.items():
        if value > threshold:
            lista.append(key)
    return lista


