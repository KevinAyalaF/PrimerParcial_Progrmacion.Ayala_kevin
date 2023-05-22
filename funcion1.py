#Ayala Fleitas Kevin
# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y 
# devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main

def aplicar_aumento(valor) -> float:
    aumento = valor * 5 / 100   #obtengo el 5% del valor
    valor = valor + aumento   #le sumo el aumento al valor recibido
    return valor



print(aplicar_aumento(100))