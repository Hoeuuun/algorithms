""" 
CF.1

A function that adds two numbers.

Example

For param1 = 1 and param2 = 2, the output should be
add(param1, param2) = 3.

Input/Output

[time limit] 4000ms (py3)
[input] integer param1
Constraints:
-100 <= param1 <= 1000.
[input] integer param2
Constraints:
-100 <= param2 <= 1000.
[output] integer
The sum of the two inputs.

"""

def add(param1, param2):
    return param1 + param2


param1 = int(raw_input("Enter first number: "))
if param1 < -100 or param1 > 1000:
    print "invalid number"

param2 = int(raw_input("Enter second number: "))
if param2 < -100 or param2 > 1000:
    print "invalid number"

result = add(param1,param2)
print result
