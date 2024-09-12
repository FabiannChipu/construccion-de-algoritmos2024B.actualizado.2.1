__author__ = "Leider Fabian Chipu"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "leider.chipu@campusucc.edu.co"

class cuenta_corriente:

    # Aqui inicia la declaracion de la clase

    '''#__________________________________________________
    # Atributos
    ___________________________________________________#'''

    __saldo = 0

    '''#__________________________________________________
    # metodos
    ___________________________________________________#'''

    __method__ = "Darsaldo"
    __parameter__ = "Ninguno"
    __returns__ = "saldo de la cuenta"
    __descripcion__ = "metodo que retorna el saldo de la cuenta"

    def DarSaldo(self):
        return self.__saldo

    __method__ = "ConsignarSaldo"
    __parameter__ = "monto"
    __returns__ = "ninguno"
    __descripcion__ = "metodo que permite consignar un monto a la cuenta"

    def ConsignarSaldo(self, monto):
        #aqui inicia mi codigo
        self.__saldo = self.__saldo+monto

    __method__ = "RetirarSaldo"
    __parameter__ = "monto"
    __returns__ = "ninguno"
    __descripcion__ = "metodo que permite retirar un monto de la cuenta"

    def RetirarSaldo(self, monto):
        # aqui inicia mi codigo
        self.__saldo = self.__saldo-monto








