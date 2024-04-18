using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program54Cconsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Radius: ");
            double radius = double.Parse(Console.ReadLine());
            double pi = Math.PI;

            double area = (double)pi * radius * radius;
            double circ = (double)pi * 2 * radius;
            Console.Write("Area: " + area + "");
            Console.Write("Circumference: " + area);
            Console.ReadKey();
        }
    }
}
