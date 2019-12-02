using System;
using System.Collections.Generic;

/*
--- Day 2: 1202 Program Alarm ---

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. 
The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate 
the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
*/

namespace AdventOfCode2019Day2
{
    class Program
    {
        static void Main(string[] args)
        {
            Part2();
        }
        static void Part1()
        {
            List<int> input = new List<int>() { 1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 13, 27, 1, 10, 27, 31, 2, 31, 13,
            35, 1, 10, 35, 39, 2, 9, 39, 43, 2, 43, 9, 47, 1, 6, 47, 51, 1, 10, 51, 55, 2, 55, 13, 59, 1, 59, 10, 63, 2, 63, 13, 67, 2, 67, 9, 71, 1, 6, 71, 75, 2, 75,
            9, 79, 1, 79, 5, 83, 2, 83, 13, 87, 1, 9, 87, 91, 1, 13, 91, 95, 1, 2, 95, 99, 1, 99, 6, 0, 99, 2, 14, 0, 0 };

            for (int i = 0; i <= input.Count; i += 4)
            {
                if (input[i] == 1)
                {
                    input[input[i + 3]] = input[input[i + 2]] + input[input[i + 1]];
                }
                else if (input[i] == 2)
                {
                    input[input[i + 3]] = input[input[i + 2]] * input[input[i + 1]];
                }
                else if (input[i] == 99)
                {
                    break;
                }
            }
            Console.WriteLine(input[0]);
        }

        static void Part2()
        {
            int noun = 0;
            int verb = 0;

            for (int x = 0; x <= 99; x++)
            {
                int tempcheck = 0;
                for (int y = 0; y <= 99; y++)
                {
                    List<int> input = new List<int>() {1, x, y, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 13, 27, 1, 10, 27, 31, 2, 31, 13,
                    35, 1, 10, 35, 39, 2, 9, 39, 43, 2, 43, 9, 47, 1, 6, 47, 51, 1, 10, 51, 55, 2, 55, 13, 59, 1, 59, 10, 63, 2, 63, 13, 67, 2, 67, 9, 71, 1, 6, 71, 75, 2, 75,
                    9, 79, 1, 79, 5, 83, 2, 83, 13, 87, 1, 9, 87, 91, 1, 13, 91, 95, 1, 2, 95, 99, 1, 99, 6, 0, 99, 2, 14, 0, 0 };
                    
                    for (int i = 0; i <= input.Count; i += 4)
                    {
                        if (input[i] == 1)
                        {
                            input[input[i + 3]] = input[input[i + 2]] + input[input[i + 1]];
                        }
                        else if (input[i] == 2)
                        {
                            input[input[i + 3]] = input[input[i + 2]] * input[input[i + 1]];
                        }
                        else if (input[i] == 99)
                        {
                            break;
                        }
                    }
                    if (input[0] == 19690720)
                    {
                        tempcheck = input[0];
                        verb = y;
                        break;
                    }
                }
                if (tempcheck == 19690720)
                {
                    noun = x;
                    break;
                }
            }
            Console.WriteLine(100 * noun + verb);
        }
    }
}
