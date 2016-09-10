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

            Console.WriteLine("Where is 1 " + Array.IndexOf(randArray2, 1));

            string[] names = { "Tom", "Paul", "Sally" };

            string nameStr = string.Join(", ", names);

            string[] nameArray = nameStr.Split(',');

            Console.WriteLine("test " + nameStr);

        }
    }
}
