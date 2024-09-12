__author__ = "Leider Fabian Chipu"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "leider.chipu@campusucc.edu.co"

from cuenta_corriente import cuenta_corriente
from cuenta_ahorros import cuenta_ahorros
from CDT import CDT


class simulador_bancario:
    # Aqui inicia la declaracion de la clase

    '''#__________________________________________________
    # Atributos
    ___________________________________________________#'''

    __nombre = ""
    __cedula = ''
    __MesActual = 0


    '''#_______________________________________________
    #asociacion
    ____________________________________________________#'''

    __CuentaCorriente = cuenta_corriente()
    __CuentaAhorros = cuenta_ahorros()
    __CDT = CDT()

    '''#_______________________________________________
    # Metodos
    ____________________________________________________#'''

    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "monto"
    __returns__ = "ninguno"
    __descripcion__ = "metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        self.__CuentaCorriente.ConsignarSaldo(monto)


    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "saldo total de todas las cuentas"
    __descripcion__ = "metodo que regresa el saldo total actual de todas las cuentas"

    def CalcularSaldoTotal(self):
        #aqui inicia mi codigo
        #metodo 1
        #total = self.__CuentaCorriente.DarSaldo()+self.__CuentaAhorros.DarSaldo()
        #return total
        return self.__CuentaCorriente.DarSaldo()+ self.__CuentaAhorros.DarSaldo()

    __method__ = "PasarAhorroACorriente"
    __parameter__ = "ninguno"
    __returns__ = "ninguna"
    __descripcion__ = "metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"

    def PasarAhorroACorriente(self):
        #aqui inicia mi codigo
        saldoAhorros = self.__CuentaAhorros.DarSaldo()
        self.__CuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__CuentaCorriente.ConsignarSaldo(saldoAhorros)

    __method__ = "Ahorrar"
    __parameter__ = "monto"
    __returns__ = "ninguna"
    __descripcion__ = "metodo que permite pasar saldo de la cuenta corriente a la cuenta de ahorros"

    def Ahorrar(self, monto):
        #aqui inicia mi codigo
        self.__CuentaCorriente.RetirarSaldo(monto)
        self.__CuentaAhorros.ConsignarSaldo(monto)

    __method__ = "RetirarAhorro"
    __parameter__ = "Monto"
    __returns__ = "saldo"
    __descripcion__ = "metodo que permite retirar un valor de la cuenta de ahorros"

    def RetirarAhorro(self, monto):
        return self.__CuentaAhorros.DarSaldo()-monto

    __method__ = "DarSaldoCorriente"
    __parameter__ = "ninguno"
    __returns__ = "saldo cuenta corriente"
    __descripcion__ = "metodo que retorna el saldo que hay en la cuenta corriente"

    def DarSaldoCorriente(self):
        return self.__CuentaCorriente.DarSaldo()

    __method__ = "RetirarTodo"
    __parameter__ = "ninguno"
    __returns__ = "ninguna"
    __descripcion__ = "metodo que retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros"

    def RetirarTodo(self):
        SaldoCorriente = self.__CuentaCorriente.DarSaldo()
        SaldoAhorros = self.__CuentaAhorros.DarSaldo()
        self.__CuentaCorriente.RetirarSaldo(SaldoCorriente)
        self.__CuentaAhorros.RetirarSaldo(SaldoAhorros)


    __method__ = "DuplicarAhorro"
    __parameter__ = "ninguno"
    __returns__ = "saldo duplicado"
    __descripcion__ = "metodo que duplica la cantidad de dinero que hay en la cuenta de ahorros"

    def DuplicarAhorro(self):
        return self.__CuentaAhorros.DarSaldo()*2








