using System;
using System.Collections.Generic;

namespace AdventOfCode2019Day4
{
    class Program
    {
        static void Main(string[] args)
        {
            Part1();
            Part2();
        }
        static void Part2()
        {
            int from = 264360;
            int to = 746325;
            int counter = 0;

            for (int i = from; i < to; i++)
            {
                List<int> temp = GetIntArray(i);
                if (((temp[0] == temp[1] && temp[1] != temp[2]) || (temp[1] == temp[2] && temp[0] != temp[1] && temp[2] != temp[3]) || (temp[2] == temp[3] && temp[1] != temp[2] && temp[3] != temp[4]) ||
                    (temp[3] == temp[4] && temp[2] != temp[3] && temp[4] != temp[5]) || (temp[4] == temp[5] && temp[3] != temp[4])) &&
                    (temp[0] <= temp[1] && temp[1] <= temp[2] && temp[2] <= temp[3] && temp[3] <= temp[4] && temp[4] <= temp[5]))
                    counter++;
            }
            Console.WriteLine(counter);
        }

        static void Part1()
        {
            int from = 264360;
            int to = 746325;
            int counter = 0;

            for (int i = from; i < to; i++)
            {
                List<int> temp = GetIntArray(i);
                if ((temp[0] == temp[1] || temp[1] == temp[2] || temp[2] == temp[3] || temp[3] == temp[4] || temp[4] == temp[5]) &&
                    (temp[0] <= temp[1] && temp[1] <= temp[2] && temp[2] <= temp[3] && temp[3] <= temp[4] && temp[4] <= temp[5]))
                    counter++;
            }
            Console.WriteLine(counter);
        }

        static List<int> GetIntArray(int num)
        {
            List<int> listOfInts = new List<int>();
            while (num > 0)
            {
                listOfInts.Add(num % 10);
                num /= 10;
            }
            listOfInts.Reverse();
            return listOfInts;
        }
    }
}