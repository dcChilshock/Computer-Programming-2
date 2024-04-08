using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Helloname
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name);

            Console.Write("Enter your age: ");
            //int age = convert.toint32(Console.readline());
            int age = int.Parse(Console.ReadLine());
            Console.WriteLine("You are " + age + " years Old!");

            Console.ReadKey();
        }
    }
}
