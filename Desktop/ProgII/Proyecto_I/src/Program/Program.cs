namespace Library 
{
    using System;
    public class Program 
    {
        public static void Main(string[] args)
        {
            CuentaBancaria cuenta1 = new CuentaBancaria("Pedro", 100);
            cuenta1.Depositar(200);
            Console.WriteLine(cuenta1.Saldo);
        }
    }
}