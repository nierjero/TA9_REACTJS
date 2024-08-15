class tarjeta :
  def __init__ (self, numero, titular, fecha, codigo, limite) :
    self.numero = numero
    self.titular = titular
    self.fecha = fecha
    self.codigo = codigo
    self.limite = limite

  def __str__(self):
        estado = f"Tarjeta de Crédito\n"
        estado += f"Número: {self.numero}\n"
        estado += f"Titular: {self.titular}\n"
        estado += f"Fecha de Vencimiento: {self.fecha}\n"
        estado += f"CVV: {self.cvv}\n"
        estado += f"Límite de Crédito: ${self.limite}\n"
        estado += f"Saldo Actual: ${self.saldo()}\n"
        estado += f"\nHistorial de Pagos:\n{self.obtener_historico_pagos()}"
        return estado

tarjeta1 = tarjeta("1234567890123456", "Adela Sanchez", "12/26", "123", 2000)
tarjeta2 = tarjeta("9876543210987654", "Juan Oreste", "06/25", "456", 1500)

print(tarjeta1)

def realizar_pago(self, monto, motivo):
        if self.saldo() + monto <= self.limite:
            pago = {"monto": monto, "motivo": motivo}
            self.historico_pagos.append(pago)
            print(f"Se realizó un pago de ${monto} con la tarjeta {self.numero} - Motivo: {motivo}")
        else:
            print("No se puede realizar el pago. Límite de crédito excedido.")

realizar_pago(tarjeta1,500,"Compra en línea")

