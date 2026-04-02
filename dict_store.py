diccionario = {"temp": 22.5, "color": "blue", "status": "ok"}
def temp_and_color(diccionario):
    if "temp" in diccionario and "color" in diccionario:
        return (diccionario["temp"], diccionario["color"])
    else:
        return (None, None)
    
resultado = temp_and_color(diccionario)
print(resultado)
