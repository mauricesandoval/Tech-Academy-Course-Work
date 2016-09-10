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
            string sampString = "A bunch of random words";

            Console.WriteLine("Index of bunch " + sampString.IndexOf("bunch"));
            Console.WriteLine("2nd Word " + sampString.Substring(2, 6));
            string sampString2 = "More random words";
            Console.WriteLine("Is empty " + String.IsNullOrEmpty(sampString2));
            Console.WriteLine("Strings Equal " + sampString.Equals(sampString2));
            Console.WriteLine("Starts with \"A bunch\" " + sampString.StartsWith("A bunch"));
            Console.WriteLine("Ends with words " + sampString.EndsWith("words"));
        }
    }
}
