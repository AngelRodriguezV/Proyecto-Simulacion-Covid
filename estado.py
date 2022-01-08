
class Estado:
    '''Clase para los estados'''

    def __init__(self, nombre_estado: str = "Oaxaca", tamano_poblacion: int = 4143593):
        self.nombre = nombre_estado
        self.poblacion = tamano_poblacion

    def list_CasosDiarios(self, casos_diarios: list):
        """Establece la lista de casos diarios
        ----------
        casos_diarios : list
            Lista de casos diarios"""
        self.casosDiarios = casos_diarios

    def list_CasosAcumulados(self, casos_diarios: list):
        """Establece la lista de casos acumulados
        ----------
        casos_diarios : list
            Lista de casos diarios"""
        aux = 0
        self.casosAcumulados = []
        for cd in casos_diarios:
            aux += cd
            self.casosAcumulados.append(aux)
    
def main():
    es = Estado()
    es.list_CasosDiarios([1,1,2,4,2,8])
    es.list_CasosAcumulados([1,1,2,4,2,8])
    print(es.casosAcumulados)

if __name__ == '__main__':
    main()