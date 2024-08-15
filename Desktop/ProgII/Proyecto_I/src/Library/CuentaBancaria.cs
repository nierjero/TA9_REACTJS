namespace Library;

public class CuentaBancaria
{
   public string Titular { get; set; }
   public double Saldo { get; set; }
   
   public CuentaBancaria(String el_titular, double el_saldo)
   {
         this.Titular = el_titular;
         this.Saldo = el_saldo;

   }
   
    public void Depositar(double mas_plata)
    {
        this.Saldo += mas_plata;
    
    }

   
}
