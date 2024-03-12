class ContaCorrente:
  def __init__(self, numero:int, saldo:float):
    self.__numero = numero
    self.__saldo = saldo

  @property
  def numero(self):
    return self.__numero
    
  @numero.setter
  def numero(self,numero):
    self.__numero = numero
    
  @property
  def saldo(self):
    return self.__saldo
    
  @saldo.setter
  def saldo(self,saldo):
    self.__saldo = saldo

  def depositar(self,numero, qtd):
    if numero == self.numero:
      self.saldo += qtd
      print(f'Depositou {qtd}$ \n Saldo atual:{self.saldo}')
    else:
      print("Conta inválida")

  def sacar(self, numero,qtd):
    if numero == self.numero:
      if qtd <= self.saldo:
        self.saldo -= qtd
        print(f'Sacou {qtd}$ \n Saldo atual: {self.saldo}')
        return self.saldo
      else:
        print("Saldo insuficiente")
    else:
      print("Conta invalida")


c1 = ContaCorrente(12345,0.0)

c1.depositar(c1.numero, 80.00)
c1.depositar(c1.numero, 80.00)
c1.depositar(c1.numero, 80.00)
c1.sacar(c1.numero, 80.00)
