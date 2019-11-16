


13. What Now?

The Python Standard Library¶
https://docs.python.org/3.8/library/index.html#library-index

The Python Language Reference¶
https://docs.python.org/3.8/reference/index.html#reference-index

Installing Python Modules¶
https://docs.python.org/3.8/installing/index.html#installing-index

FAQ
https://docs.python.org/3.8/faq/index.html#faq-index

other resources...


14. Interactive Input Editing and History Substitution
14.1. Tab Completion and History Editing
14.2. Alternatives to the Interactive Interpreter


15. Floating Point Arithmetic: Issues and Limitations
Unfortunately, most decimal fractions cannot be represented exactly as binary fractions.
A consequence is that, in general, the decimal floating-point numbers you enter are only
approximated by the binary floating-point numbers actually stored in the machine.

Just remember, even though the printed result looks like the exact value of 1/10, the
actual stored value is the nearest representable binary fraction.

Note that this is in the very nature of binary floating-point: this is not a bug in Python, and
it is not a bug in your code either. You’ll see the same kind of thing in all languages that
support your hardware’s floating-point arithmetic (although some languages may not
display the difference by default, or in all output modes).

need to keep in mind that it’s not decimal arithmetic and that
every float operation can suffer a new rounding error.

For use cases which require exact decimal representation, try using the decimal module which
implements decimal arithmetic suitable for accounting applications and high-precision applications.

Another form of exact arithmetic is supported by the fractions module


15.1. Representation Error
Representation error refers to the fact that some (most, actually)
decimal fractions cannot be represented exactly as binary (base 2) fractions.


16. Appendix
16.1. Interactive Mode
16.1.1. Error Handling
16.1.2. Executable Python Scripts
16.1.3. The Interactive Startup File
16.1.4. The Customization Modules








