using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Linq;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            List<int> numList = new List<int>();

            numList.Add(5);
            numList.Add(15);
            numList.Add(25);

            int[] randArray = { 1, 2, 3, 4, 5 };
            numList.AddRange(randArray);

            //Copy an Array into a list
            List<int> numList2 = new List<int>(randArray);

            List<int> numList3 = new List<int>(new int[] { 1, 2, 3, 4 });

            numList.Insert(1, 10);

            numList.Remove(5);

            numList.RemoveAt(2);

            for (int i = 0; i < numList.Count; i++)
            {
                Console.WriteLine(numList[i]);
            }

            Console.WriteLine("4 i in index " + numList3.IndexOf(4));

            Console.WriteLine("5 in list " + numList.Contains(5));

            List<string> strList = new List<string>(new string[] { "Tom", "Paul" });

            Console.WriteLine("Tom in list " + strList.Contains("tom", StringComparer.OrdinalIgnoreCase));

            strList.Sort();



        }
    }
}
