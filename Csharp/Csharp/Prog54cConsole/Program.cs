using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prog54cConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Radius: ");
            double radius = double.Parse(Console.ReadLine());

            double circumfrence = 2 * Math.PI * radius;
            double area = Math.PI * (radius * radius);
            Console.WriteLine("Radius: "+ radius);
            Console.WriteLine("Circumfrence: " + Math.Round(circumfrence, 2));
            Console.WriteLine("Area: " + Math.Round(area, 2));
            Console.ReadKey();
        }
    }
}
