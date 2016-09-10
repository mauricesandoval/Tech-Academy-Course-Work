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

            string sampString2 = "More random words";

            sampString = sampString.Replace("words", "characters");

            Console.WriteLine("This string was changed:  " + sampString);

            sampString = sampString.Remove(0,2);

            Console.WriteLine("Removed some stuff: " + sampString);

            string[] names = new string[3] { "Matt", "Joe", "Bill" };

            Console.WriteLine("Name List " + String.Join(", ", names));

        }
    }
}
