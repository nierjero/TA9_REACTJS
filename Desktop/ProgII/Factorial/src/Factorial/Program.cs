
namespace Library;
public class Program
{

public static void Main(string[] args)
{
    int valor_for = 5;
    int valor_while = 5;
    Console.WriteLine($"El factorial de {valor_for} es {CalcularFactorialFor.FactoFor(valor_for)}");
    Console.WriteLine($"El factorial de {valor_while} es {CalcularFactorialWhile.FactoWhile(valor_while)}");
}
}
