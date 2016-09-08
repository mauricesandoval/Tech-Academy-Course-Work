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
            
            //Relational Operators: > < >= <= == !=
            //Logical Operators: && || ^ !

            int age = 16;
            if ((age >= 5) && (age <= 7))
            {
                Console.WriteLine("Go to elementary school");
            } else if((age > 7) && (age < 13))
            {
                Console.WriteLine("Go to middle school");
            }else
            {
                Console.WriteLine("Go to high school");
            }
            
            /*
            switch (age)
            {
                case 0:
                    Console.WriteLine("Infant");
                    break;
                case 1:
                case 2:
                    Console.WriteLine("Toddler");
                default:
                    Console.WriteLine("Child");
                    break;
            }
           */

        }
    }
}
