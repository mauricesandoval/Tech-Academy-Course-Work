using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            double number1 = 10.5;
            double number2 = 15;

            Console.WriteLine("Math.Abs(number1)" + (Math.Abs(number1)));
            Console.WriteLine("Math.Ceiling(number1)" + (Math.Ceiling(number1)));
            Console.WriteLine("Math.Floor(number2)" + (Math.Floor(number2)));

            Random rand = new Random();
            Console.WriteLine("A random number between 1 and 10 is " + (rand.Next(1, 11)));

            

        }
    }
}
