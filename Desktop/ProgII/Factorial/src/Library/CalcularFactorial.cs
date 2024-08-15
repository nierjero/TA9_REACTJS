using System.Data;
using System.Reflection.Metadata.Ecma335;

namespace Library;

public class CalcularFactorialFor
{
public static int FactoFor(int valor_for)
{
    int factorial_for = 1;
    for (int i = 1; i <= valor_for ; i++)
    {
         factorial_for = i*factorial_for;
    }
    return factorial_for;


    
}
}

public class CalcularFactorialWhile
{
    public static int FactoWhile(int valor_while)
    {
        int factorial_while = 1;
        int i = 1;
        while (i <= valor_while)
        {
              factorial_while = i*factorial_while;
               i++;

        }
        return factorial_while;
    }
}

