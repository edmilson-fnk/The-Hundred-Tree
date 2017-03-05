# The Hundred Tree project

Application designed to solve the following problem:

Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

Run it with Python using the Pyramid Framework. The app package does all the logic job.

Try it: http://edmilsonfrank.dyndns-ip.com:6543

To run the application, just download it and run the pserve script to the development.ini file. The application was originally made with Windows, so be sure to run the appropriate pserve.

# The solution

The problem is straight and simple, a brute force solution will quickly solve it and even enable some variations to the problem, so the focus during the development of the solution was on providing the web application with the minimum requirements that the problem demanded and even provide a way to solve variations of the problem.

The methodology adopted for the brute force was: create a Binary Tree with the numbers in [min, max] interval in the leafs, while the internal nodes would be filled with all the different operators. A in-order visit of the full tree would get the expression, so an eval() function could get its result and compare to the expected output. Naming the project was motivated by the binary tree.

A simple model for the problem was created: the Node class in a node.py file, with the minimum required aspects of a tree to work, and a builder.py file, responsible for validating the parameters submitted and building a template tree. The Node module build all the possibilities itself, but it's something that could be easily extracted in the future, if needed.
