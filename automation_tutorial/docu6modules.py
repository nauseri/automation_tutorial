


# 6. modules
# put definitions, statements, functions etc in a file and use them in a script
# this is called module and can be imported to other modules
# file name with suffix .py
import p_tut_6_fibo
print(p_tut_6_fibo.fib(10))
print(p_tut_6_fibo.fib2(10))
print(p_tut_6_fibo.__name__)  # in a module, the module name is called with .__name__
# assign a local name if function is used often!
fibi = p_tut_6_fibo.fib
print(fibi(40))

# variant of the import statement that imports names from a module
# directly into the importing module’s symbol table
# this does not put p_tut_6_fibo into local symbol table, so its not defined...
from p_tut_6_fibo import fib, fib2
print(fib(100))
print(fib2(100))
# import all names of a modul with a star, no used usually...
from p_tut_6_fibo import *
print(fib(200))
print(fib2(200))
# If the module name is followed by as,
# then the name following as is bound directly to the imported module.
import p_tut_6_fibo as fib
print(p_tut_6_fibo.fib(500))
# can also be used when utilising from
from p_tut_6_fibo import fib as fibonacci
print(fibonacci(500))


# 6.1.1. Executing modules as scripts
# 6.1.2. The Module Search Path
6.1.3. “Compiled” Python files











