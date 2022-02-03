class Estado:
    '''Clase para manejar los datos de los estados'''

    def __init__(self, nombre_estado: str = "Oaxaca", tamano_poblacion: int = 4143593):
        self.nombre = nombre_estado
        self.poblacion = tamano_poblacion

    def list_CasosDiarios(self, casos_diarios: list):
        """Establece la lista de casos diarios"""
        self.casosDiarios = casos_diarios

    def list_CasosAcumulados(self, casos_diarios: list):
        """Establece la lista de casos acumulados"""
        aux = 0
        self.casosAcumulados = []
        for cd in casos_diarios:
            aux += cd
            self.casosAcumulados.append(aux)

    def list_fecha(self, fechas: list):
        """Establecer la lista de las fechas"""
        self.fechas = fechas