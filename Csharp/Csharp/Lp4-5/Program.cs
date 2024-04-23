using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lp4_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the grade percentage: ");
            double grade = double.Parse(Console.ReadLine());
            char letgrade = ' ';
            if (grade >= 90)
            {
                letgrade = 'A';
            }
            else if (grade >= 80)
            {
                letgrade = 'b';
            }
            else if (grade >= 70)
            {
                letgrade = 'c';
            }
            else if (grade >= 60)
            {
                letgrade = 'd';
            }
            else
            {
                letgrade = 'f';
            }
            Console.WriteLine("The corresponding letter grades is; " + letgrade);
            Console.ReadKey();
        }
    }
}
