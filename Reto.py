from ast import Index


Seleccion=({
20170136837:{
"nombres" : "Jorge Juan",
"apellidos" : "Moreno López",
"documento" : 88481595,
"programa" : "ARQU",
"materias" : [
{
"facultad" : "Arquitectura",
"codigo" : "ARQU-2113",
"nota" : 2.97,
"creditos" : 2,
"retirada" : "Si",
},
{
"facultad" : "Arquitectura",
"codigo" : "ARQU-5048",
"nota" : 4.26,
"creditos" : 0,
"retirada" : "No",
},
]
},
20130225137:{
"nombres" : "Sara Carolina",
"apellidos" : "Gómez Fernández",
"documento" : 58770043,
"programa" : "ARQD",
"materias" : [
{
"facultad" : "Arquitectura",
"codigo" : "ARQD-7738",
"nota" : 3.36,
"creditos" : 3,
"retirada" : "No",
},
{
"facultad" : "Arquitectura",
"codigo" : "ARQD-7698",
"nota" : 1.59,
"creditos":4,
"retirada": "Si",},
]
} })
def quitar_tildes(palabra:str):
    palabras={'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',}
    for x in palabra:  
        vocales=str(palabra)
        if x in palabras.keys():
           indice_tilde=vocales.index(x)
           palabra=palabra.replace(x, palabras[x])
           return palabra
print(quitar_tildes('dsáf'))
def correo():
    id=Seleccion[20170136837]
    nombres:str=id['nombres']
    nombres=nombres.split()
    apellidos:str=id['apellidos']
    apellidos=apellidos.split()
    nombre_completo=[]
    for x, y in nombres, apellidos:
        minusculas_x:str=x.lower()
        minusculas_y=y.lower()
        nombre_completo.append(minusculas_x)
        nombre_completo.append(minusculas_y)
correo()