namespace Library;
using System.Collections.Generic;
public class DiferenciaListas
{

public static List<int> SymDiff(List<int> lista1, List<int> lista2)
{
     var diferencia = new List<int>{};
    foreach (var número in lista1)
    {
        if (!lista2.Contains(número))
        {
            diferencia.Add(número);
        }
    }
    foreach (var número2 in lista2)
    {
        if (!lista1.Contains(número2))
        {
            diferencia.Add(número2);
        }
    }
    
    return diferencia;
}
}
    


