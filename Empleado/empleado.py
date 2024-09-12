__author__ = "Leider Fabian Chipu"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "leider.chipu@campusucc.edu.co"

from Fecha import Fecha


class Empleado:
    # Aqui inicia la declaracion de la clase

    '''#__________________________________________________
    # Atributos
    ___________________________________________________#'''

    nombre = ""
    apellido = ""
    salario = 0

    '''#_____________________________________________________
    # 1 = Masculino, 2 = Femenino
    _____________________________________________________#'''

    sexo = 0

    '''#_______________________________________________
    #asociacion
    ____________________________________________________#'''

    FechaIngreso = Fecha()
    fechaNacimiento = Fecha()

    '''#_______________________________________________
    # Metodos
    ____________________________________________________#'''
    # Este metodo retorna el nombre del empleado
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre


    __method__ = "CambiarSalario"
    __parameter__ = "NuevoSalario"
    __returns__ = "salario"
    __descripcion__ = "metodo que actualiza el salario del empleado"


    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo
        self.salario = nuevoSalario

    # Retorna el salario del empleado
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario

    def ConsularFecahaIngreso(self):
        return self.FechaIngreso.DarFecha()

    __method__ = "CalcularSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "Sañario anual"
    __descripcion__ = "muestra el salario anual del empleado"

    def CalcularSalarioAnual(self):
        #aqui va mi codigo
        # Forma 1
       #total= self.salario*12
       # return total
        #forma 2
        return self.salario*12

    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "impuesto Sañario anual"
    __descripcion__ = "muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # Aqui inicia mi codigo
        # forma 1
        #SalarioAnual=self.CalcularSalarioAnual()
        #ImpuestoAnual=SalarioAnual*0.19
        #return ImpuestoAnual
        #forma 2
        return self.CalcularSalarioAnual()*0.19


    __method__ = "CalcularImpuestoMensual"
    __parameter__ = "Ninguno"
    __returns__ = "Impuesto salario mensual"
    __descripcion__ = "muestra el impuesto del salario mensual del empleado"
    def CalcularImpuestoSalarioMensual(self):
        return self.Darsalario()*0.19



