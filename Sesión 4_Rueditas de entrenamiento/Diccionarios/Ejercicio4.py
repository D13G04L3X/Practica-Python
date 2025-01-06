'''
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd
de <mes> de aaaa donde <mes> es el nombre del mes.
'''

# 01/10/2018                Clave del mes = 10
# 01 de octubre del 2018    Valor del mes = octubre
# Clave: valor
'''
meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
fecha = input('Por favor, escriba una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'del', fecha[2])
'''
# Recomendación: Hacer las validaciones en caso de una entrada falsa, por ejemplo un mes que no existe o mayor a 12, 
# también puede validar el día, que esté entre 1 y 31 y validar el año sea mayor a 2000 y menor a 9999

# Solución 2

meses = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
    7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

def es_fecha_valida(dia, mes, anio):
    if not (2000 <= anio <= 9999):
        return False
    if not (1 <= mes <= 12):
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        es_bisiesto = anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
        return dia <= 29 if es_bisiesto else dia <= 28
    return 1 <= dia <= 31

fecha = input('Por favor, escriba una fecha en formato dd/mm/aaaa: ')

# Validaciones
if '/' in fecha:
    partes = fecha.split('/')
    if len(partes) == 3 and all(parte.isdigit() for parte in partes):
        dia, mes, anio = map(int, partes)
        if es_fecha_valida(dia, mes, anio):
            print(f"{dia} de {meses[mes]} del {anio}")
        else:
            print("Fecha inválida.")
    else:
        print("El formato debe ser dd/mm/aaaa con valores numéricos.")
else:
    print("El formato debe incluir '/' para separar día, mes y año.")
