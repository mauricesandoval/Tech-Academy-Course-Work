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

            StringBuilder sb = new StringBuilder();

            sb.Append("This is a sentence. ");
            sb.AppendFormat("My name is {0} and I live {1} ", "Derek", "Pennsylvania");

            sb.Replace("a", "e");

            sb.Remove(5, 7);
            Console.WriteLine(sb.ToString());
        }
    }
}
