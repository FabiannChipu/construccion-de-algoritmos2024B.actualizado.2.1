__author__ = "Leider Fabian Chipu"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "leider.chipu@campusucc.edu.co"

class Fecha:
    # Aqui inicia la declaracion de mi clase

    '''#_____________________________________
    # Atributos
    ___________________________________________#'''

    dia = 0
    mes = 0
    anio = 0
    '''#_______________________________________________
    # Metodos
    ____________________________________________________#'''

    __method__ = "DsrDia"
    __parameter__ = "Ninguno"
    __returns__ = "dia"
    __descripcion__ = "metodo que regresa el dia"

    def DarDia(self):
        # Aqui va mi codigo

     __method__ = "DarMes"
    __parameter__ = "Ninguno"
    __returns__ = "Mes"
    __descripcion__ = "metodo que regresa el mes"


    def DarMes(self):
        # Aqui va mi codigo

     __method__ = "DarAnio"
    __parameter__ = "Ninguno"
    __returns__ = "Anio"
    __descripcion__ = "metodo que regresa el año"

    def DarAnio(self):
      # Aqui va mi codigo

     __method__ = "DarFecha"
    __parameter__ = "Ninguno"
    __returns__ = "La fecha de la clase"
    __descripcion__ = "metodo que regresa la fecha digitada por el usuario"

    def DarFecha(self):
      return self.dia+'/'+self.mes+'/'+self.anio

