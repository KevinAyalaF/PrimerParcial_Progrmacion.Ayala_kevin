# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
# un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y 
# devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

def remplazar_caracteres(cadena: str, caracter_por_remplazar: str, caracter_nuevo: str) -> None:
    cantidad_remplazo = cadena.count(caracter_por_remplazar)   #cuentos las ocurrencias
    cadena = cadena.replace(caracter_por_remplazar, caracter_nuevo)  #remplazo el viejo caracter por el nuevo
    print(cadena)     #lo imprimo
    print("la cantidad de cambios es", cantidad_remplazo)  #mprimo la cantidad


remplazar_caracteres("esto es una prueba", "a", "b")