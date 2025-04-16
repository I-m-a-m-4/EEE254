# EEE254

Recursion

 recursion is just when a function kinda “calls itself” to handle smaller bits of a problem until it hits a simple case it knows how to solve. You always need two things:

Base case – the simplest scenario, where you just return a value without calling yourself again.

Recursive case – you break the problem into a smaller chunk, call the same function on that, then combine results.

“Recursion is a programming technique where a function calls itself to solve problems by breaking them into smaller subproblems” 
GeeksforGeeks

“Recursion is breaking a component down into smaller components using the same function... until the base problem is identified and solved.” 
Codecademy

Power Set Example (All Subsets)
A power set of a set is just every possible subset of it. If your set is [1,2,3], the power set is:

css

[ [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] ]
Recursion makes this super clean.

How it works
Base case: if the array is empty, there’s only one subset—the empty one: [[]].

Recursive case:

Take the first element off (e.g., 1)

Recursively get the power set of the rest ([2,3]) → say that’s withoutFirst

For each subset in withoutFirst, make a new subset that also has the first element → withFirst

Combine both lists and return

This splits the problem into “smaller” bits over and over—exactly recursion’s jam 
