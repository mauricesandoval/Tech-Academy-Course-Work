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
            

            int[] randNumArray;

            int[] randArray = new int[5];

            int[] randArray2 = { 1, 2, 3, 4, 5 };

            Console.WriteLine("Array Length " + randArray2.Length);

            Console.WriteLine("Item 0 " + randArray2[0]);

            for (int i = 0; i<randArray2.Length;i++)
            {
            Console.WriteLine("{0} : {1}", i,randArray2[i]);
            }
           
            foreach(int num in randArray2)
            {
                Console.WriteLine(num);
            }

            

        }
    }
}
