#  DRY(Don't Repeat Yourself) printf style debugging

currently alpha state

ex:

    d.debug_print("a")

prints result/value of the expression/variable(using eval, the reason
to use eval is so you can print out the variable name/epresion 
and what it evaluates to without specifying it twice) with line number, function name, type.
Soon it will print in color to stand out better.

    d.debug_message("some message")

just prints out a string(no eval) but with func name/line #/file
