namespace Library;

public class LeapVerifier
{
public static bool leapTime(int year)
{
    bool LeapConfirmation = false;
    if (year % 4 == 0 && year % 100 != 0 || year % 400==0)
        {
            LeapConfirmation = true;
        }
    return LeapConfirmation;
}
}
