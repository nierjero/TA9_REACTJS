using System.ComponentModel;

namespace Library
{
public class Program 
{
public static void Main(string[] args)
{
   
    var lista1 = new List<int>{1,2,3};
    var lista2 = new List<int>{3,4,5};
    List<int> resultado = DiferenciaListas.SymDiff(lista1, lista2);
    
    Console.Write(string.Join("," ,DiferenciaListas.SymDiff(lista1, lista2)));
}
}
}