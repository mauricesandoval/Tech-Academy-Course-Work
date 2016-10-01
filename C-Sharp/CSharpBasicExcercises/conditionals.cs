using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            //Relational Operators: > < >= <= == !=
            //Logical Operators: && || ^ !

            int age = 4;
            if ((age >= 6) && (age <= 12))
            {
                Console.WriteLine("Go to elementary school");
            }
            else if ((age >= 13) && (age <= 14))
            {
                Console.WriteLine("Go to middle school");
            }
            else
            {
                Console.WriteLine("Go to high school");
            }


            switch (age)
            {
                case 0:
                    Console.WriteLine("Infant");
                    break;
            }

            switch (age)
            {
                case 1:
                    Console.WriteLine("Baby");
                    break;
            }

            switch (age)
            {
                default:
                    Console.WriteLine("Toddler");
                    break;

            }

        }
    }
}
