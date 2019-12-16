using System;
using System.Collections.Generic;

/*
--- Day 1: The Tyranny of the Rocket Equation ---

uel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
*/

namespace AdventOfCode2019Day1
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> input = new List<int>() { 70219,93253,79077,75104,142278,65798,148578,136159,60033,51629,57239,77808,142016,92225,136933,95933,109170,83012,135771,59064,101361,86997,79026
            ,50825,79671,143898,65548,84651,53043,84997,87226,65816,81088,143976,109917,103744,131433,81899,80901,146112,65084,84439,73939,102337,99794,107113,62081,98484,55246,131950,129633
            ,98380,118568,100632,127493,90804,120735,124932,115165,73091,77960,67435,63132,114453,104379,82371,51259,104055,127984,108215,53174,139459,58530,86994,149064,90062,139593,128406,
            136288,140669,125298,144444,80296,135065,121641,108842,59336,64720,121706,78017,142674,89214,100171,80836,110919,102218,54834,104544,81501,128610};

            int answer = 0;

            foreach (int element in input)
            {
                int temp = (element / 3 - 2);
                while (temp > 0)
                {
                    answer = answer + temp;
                    temp = (temp / 3 - 2);
                }
                
            }
            Console.WriteLine(answer);
        }
    }
}
