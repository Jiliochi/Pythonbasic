#include <stdio.h>

int fibonacci();

int main (void)
{
    int q;
    printf ("How many times do you want to iterate:\n");
    scanf ("%i", &q);
    int n;
    printf ("Fibonacci series number?\n");
    scanf ("%i", &n);

    for (int i = 0; i < q; i++, n++)
    {
        printf("%i\n", fibonacci(n));
    }
    return 0;

}

int fibonacci(n)
{
    if (n == 1)
    {
        return 1;
    }
    else if (n == 2)
    {
        return 2;
    }
    else if (n > 2)
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    else
    {
        return 1;
    }
}
