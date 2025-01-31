# int and operation(arithmetic)

# a and b are two variables of int type

a_int = 2
b_int = 3

print("a_int and b_int are two variables of int type with values:", a_int, "and", b_int)

print("Type of a_int:", type(a_int), "Type of b_int:", type(b_int))
# addition
print("Addition of a_int and b_int (int) = ", a_int, "+", b_int, "=", a_int + b_int)
# subtraction
print("Subtraction of a_int and b_int (int) = ", a_int, "-", b_int, "=", a_int - b_int)
# multiplication
print("Multiplication of a_int and b_int (int) = ", a_int, "*", b_int, "=", a_int * b_int)
# division
print("Division of a_int and b_int (int) = ", a_int, "/", b_int, "=", a_int / b_int)
# modulus
print("Modulus of a_int and b_int (int) = ", a_int, "%", b_int, "=", a_int % b_int)
# floor division
print("Floor division of a_int and b_int (int) = ", a_int, "//", b_int, "=", a_int // b_int)
# exponentiation
print("Exponentiation of a_int and b_int (int) = ", a_int, "**", b_int, "=", a_int ** b_int)
print("\n\n")

# float operations(arithmetic)

# c and d are two variables of float type
# we can make c and d user defined by float(input())

c_float = float(input("Enter a float value for c_float: "))
d_float = float(input("Enter a float value for d_float: "))

print("c_float and d_float are two variables of float type with values:", c_float, "and", d_float)

print("Type of c_float:", type(c_float), "Type of d_float:", type(d_float))
# addition
print("Addition of c_float and d_float (float) = ", c_float, "+", d_float, "=", c_float + d_float)
# substraction
print("Subtraction of c_float and d_float (float) = ", c_float, "-", d_float, "=", c_float - d_float)
# multiplication
print("Multiplication of c_float and d_float (float) = ", c_float, "*", d_float, "=", c_float * d_float)
# division
print("Division of c_float and d_float (float) = ", c_float, "/", d_float, "=", c_float / d_float)
# modulus
print("Modulus of c_float and d_float (float) = ", c_float, "%", d_float, "=", c_float % d_float)
# floor division
print("Floor division of c_float and d_float (float) = ", c_float, "//", d_float, "=", c_float // d_float)
# exponentiation
print("Exponentiation of c_float and d_float (float) = ", c_float, "**", d_float, "=", c_float ** d_float)
print("\n\n")

# order of arithmetic operations
print("Order of arithmetic operations for 10 + 2 * 3 ** 2 - (5 // 2)")
result = 10 + 2 * 3 ** 2 - (5 // 2)
print("Result of the expression 10 + 2 * 3 ** 2 - (5 // 2) =", result)

''' 1.Parentheses ()
    2.Exponentiation **
    3.Unary plus and minus +x, -x
    4.Multiplication, Division, Floor Division, and Modulo *, /, //, % (evaluated from left to right)
    5.Addition and Subtraction +, - (evaluated from left to right)'''
print("1.Parentheses ()\n2.Exponentiation **\n3.Unary plus and minus +x, -x\n4.Multiplication, Division, Floor Division, and Modulo *, /, //, % (evaluated from left to right)\n5.Addition and Subtraction +, - (evaluated from left to right)")
print("\n\n")


# boolean operations
# e and f are two variables of boolean type

e_bool = True
f_bool = False

print("e_bool and f_bool are two variables of boolean type with values:", e_bool, "and", f_bool)

print("Type of e_bool:", type(e_bool), "Type of f_bool:", type(f_bool))
# and operation
print("AND operation between e_bool and f_bool = ", e_bool, "and", f_bool, "=", e_bool and f_bool)
# or operation
print("OR operation between e_bool and f_bool = ", e_bool, "or", f_bool, "=", e_bool or f_bool)
# not operation
print("NOT operation on e_bool =", "not", e_bool, "=", not e_bool)
print("\n\n")


# bitwise operations
# g and h are two variables of int type

g_int = 2
h_int = 3

print("g_int and h_int are two variables of int type with values:", g_int, "and", h_int)

print("Type of g_int:", type(g_int), "Type of h_int:", type(h_int))
# bitwise and operation
print("Bitwise AND operation between g_int and h_int = ", g_int, "&", h_int, "=", g_int & h_int)
print("Explanation: Bitwise AND compares each bit of g_int and h_int. If both bits are 1, the result is 1. Otherwise, it is 0.")
# bitwise or operation
print("Bitwise OR operation between g_int and h_int = ", g_int, "|", h_int, "=", g_int | h_int)
print("Explanation: Bitwise OR compares each bit of g_int and h_int. If at least one of the bits is 1, the result is 1. Otherwise, it is 0.")
# bitwise xor operation
print("Bitwise XOR operation between g_int and h_int = ", g_int, "^", h_int, "=", g_int ^ h_int)
print("Explanation: Bitwise XOR compares each bit of g_int and h_int. If the bits are different, the result is 1. Otherwise, it is 0.")
# bitwise not operation
print("Bitwise NOT operation on g_int =", "~", g_int, "=", ~g_int)
print("Explanation: Bitwise NOT inverts all the bits of g_int. Each 0 becomes 1 and each 1 becomes 0.")
# bitwise left shift operation
print("Bitwise left shift operation on g_int by 1 =", g_int, "<< 1 =", g_int << 1)
print("Explanation: Bitwise left shift shifts all the bits of g_int to the left by 1 position. A 0 is added on the right.")
# bitwise right shift operation
print("Bitwise right shift operation on g_int by 1 =", g_int, ">> 1 =", g_int >> 1)
print("Explanation: Bitwise right shift shifts all the bits of g_int to the right by 1 position. The leftmost bit is discarded.")
print("\n\n")


# relational operations

i_int = 2
j_int = 3

print("i_int and j_int are two variables of int type with values:", i_int, "and", j_int)

# greater than operation
print("Greater than operation between i_int and j_int =", i_int, ">", j_int, "=", i_int > j_int)
# less than operation
print("Less than operation between i_int and j_int =", i_int, "<", j_int, "=", i_int < j_int)
# greater than or equal to operation
print("Greater than or equal to operation between i_int and j_int =", i_int, ">=", j_int, "=", i_int >= j_int)
# less than or equal to operation
print("Less than or equal to operation between i_int and j_int =", i_int, "<=", j_int, "=", i_int <= j_int)
# equal to operation
print("Equal to operation between i_int and j_int =", i_int, "==", j_int, "=", i_int == j_int)
# not equal to operation
print("Not equal to operation between i_int and j_int =", i_int, "!=", j_int, "=", i_int != j_int)
print("\n\n")


# identity operations

k_int = 3
l_int = 4

print("k_int and l_int are two variables of int type with values:", k_int, "and", l_int)

# is operation
print("Identity operation (is) between k_int and l_int =", k_int, "is", l_int, "=", k_int is l_int)
# is not operation
print("Identity operation (is not) between k_int and l_int =", k_int, "is not", l_int, "=", k_int is not l_int)
print("\n\n")


# membership operations
# m is a variable of string type

m_str = "hello"

print("m_str is a variable of string type with value:", m_str)

print("Type of m_str:", type(m_str))
# in operation
print("Membership operation (in) to check if 'h' is in m_str =", "'h' in", m_str, "=", 'h' in m_str)
# not in operation
print("Membership operation (not in) to check if 'h' is not in m_str =", "'h' not in", m_str, "=", 'h' not in m_str)
print("\n\n")


# assignment operations

n_int = 2
o_int = 3

print("n_int and o_int are two variables of int type with values:", n_int, "and", o_int)

# assignment operation
print("Assignment operation: n_int =", n_int)  
# addition assignment operation
n_int += o_int
print("Addition assignment operation: n_int += o_int =", n_int)
# subtraction assignment operation
n_int -= o_int
print("Subtraction assignment operation: n_int -= o_int =", n_int)
# multiplication assignment operation
n_int *= o_int
print("Multiplication assignment operation: n_int *= o_int =", n_int)
# division assignment operation
n_int /= o_int
print("Division assignment operation: n_int /= o_int =", n_int)
# modulus assignment operation
n_int %= o_int
print("Modulus assignment operation: n_int %= o_int =", n_int)
# floor division assignment operation
n_int //= o_int
print("Floor division assignment operation: n_int //= o_int =", n_int)
# exponentiation assignment operation
n_int **= o_int
print("Exponentiation assignment operation: n_int **= o_int =", n_int)