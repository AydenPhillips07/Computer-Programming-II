﻿// See https://aka.ms/new-console-template for more information
Console.Write("Enter the grade percentage: ");
double grade = double.Parse(Console.ReadLine());
char letgrade = ' ';
if (grade >= 90)
    letgrade = 'A';
else if (grade >= 80)
    letgrade = 'B';
else if (grade >= 70)
    letgrade = 'C';
else if (grade >= 60)
    letgrade = 'D';
else
    letgrade = 'F';

Console.WriteLine("The corresponding letter grade is: " + letgrade);
Console.ReadKey();  
