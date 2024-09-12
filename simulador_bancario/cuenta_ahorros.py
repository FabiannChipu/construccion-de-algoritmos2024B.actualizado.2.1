__author__ = "Leider Fabian Chipu"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "leider.chipu@campusucc.edu.co"


class cuenta_ahorros:

    # Aqui inicia la declaracion de la clase

    '''#__________________________________________________
    # Atributos
    ___________________________________________________#'''

    __saldo = 0
    __interes = 0

    '''#_______________________________________________
    # Metodos
    ____________________________________________________#'''

    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __returns__ = "saldo de la cuenta"
    __descripcion__ = "metodo que muestra el saldo de la cuenta"

    def DarSaldo(self):
        # Aqui inicia mi codigo
        return self.__saldo

    __method__ = "ConsiganarSaldo"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __descripcion__ = "metodo que permite consignar un monto a la cuenta"

    def ConsignarSaldo(self, Monto):
        # Aqui va mi codigo
        self.__saldo = self.__saldo+Monto


    __method__ = "RetirarSaldo"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __descripcion__ = "metodo que permite retirar un monto de la cuenta"


    def RetirarSaldo(self, monto):
        # Aqui va mi codigo
        self.__saldo = self.__saldo-monto


    __method__ = "DarInteresMensual"
    __parameter__ = "Ninguno"
    __returns__ = "Interes mensual"
    __descripcion__ = "metodo que retorna el valor del interes mensual "

    def DarInteresMensual(self):
        # Aqui va mi codigo
        return self.__interes

