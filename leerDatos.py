from csv import reader
import estado

def leer_csv(archivo: str = 'ejemplo.csv'):
    '''Lee un archivo csv'''
    lista_csv = []
    with open(archivo) as csvfile:
        csvreader = reader(csvfile)
        lista_csv = list(csvreader)
    return lista_csv

def obtecion_datos(archivo: str = 'ejemplo.csv'):
    '''Obtiene los datos del archivo'''
    list_csv = leer_csv(archivo)
    fecha = list_csv[0]
    fecha = fecha[3:len(fecha)]
    list_csv = list_csv[1:len(list_csv)]
    estados = []
    for e in list_csv:
        aux = estado.Estado(nombre_estado=e[2],tamano_poblacion=int(e[1]))
        aux.list_CasosDiarios(int_list(e[3:len(e)]))
        aux.list_CasosAcumulados(aux.casosDiarios)
        aux.list_fecha(fecha)
        estados.append(aux)
    return estados

def int_list(Lista: list):
    '''Combierte una lista de str a int'''
    aux = []
    for i in Lista:
        aux.append(int(i))
    return aux

datos = obtecion_datos(archivo='Datos\\Casos_Diarios.csv')
for i in datos:
    print(str(len(i.casosDiarios))+","+str(len(i.fechas)))