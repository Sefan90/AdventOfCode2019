using System;
using System.Collections.Generic;

namespace AdventOfCode2019Day16
{
    class Program
    {
        static void Main(string[] args)
        {
            //int inputList = 59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608;
            //List<int> splitedList = GetIntArray(inputList);
            List<int> splitedList = new List<int>() { 0, 3, 0, 3, 6, 7, 3, 2, 5, 7, 7, 2, 1, 2, 9, 4, 4, 0, 6, 3, 4, 9, 1, 5, 6, 5, 4, 7, 4, 6, 6, 4 };
            List<int> tempList = new List<int>();
            for (int i = 0; i < 10; i++)
            {
                tempList.AddRange(splitedList);
            }
            splitedList = tempList;
            List<List<int>> patternList = MakePattern(splitedList);

            for(int x = 0; x < 100; x++)
            {
                List<int> newList = new List<int>();
                for(int i = 1; i < splitedList.Count+1; i++)
                {
                    int output = 0;
                    int bp = 0;
                    for(int item = 0; item < splitedList.Count; item++)
                    {
                        output = splitedList[item] * patternList[i-1][bp];
                        bp += 1;
                        bp %= patternList.Count;
                    }
                    newList.Add(Math.Abs(output) % 10);
                }
                splitedList = newList;
            }
            Console.WriteLine(splitedList[0] + "" + splitedList[1] + "" + splitedList[2] + "" + splitedList[3] + "" + splitedList[4] + "" + splitedList[5] + "" + splitedList[6] + "" + splitedList[7]);
        }

        private static List<int> GetIntAray(int number)
        {
            List<int> result = new List<int>();

            while (number > 0)
            {
                result.Insert(0, number % 10);
                number /= 10;
            }
            if (result.Count == 0)
                result.Add(0);
            return result;
        }

        static List<List<int>> MakePattern(List<int> inputList)
        {
            List<List<int>> listPattern = new List<List<int>>();
            List<int> basePattern = new List<int>() { 0, 1, 0, -1 };
            List<int> bigPattern = new List<int>() { 1, 0, -1, 0};

            for (int i = 2; i < inputList.Count + 2; i++)
            {
                for (int b = 1; b < basePattern.Count; b++)
                    bigPattern.Insert(i * b, basePattern[b]);
                listPattern.Add(bigPattern);
            }
            return listPattern;
        }
    }
}
