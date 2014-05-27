# DRY(Don't Repeat Yourself) printf style debugging

In beta, still need to figure out what to do with logging.

ex:

    d.debug_eval_print("a")

or    
    
    d.debug_eval_print("[l(s) for s in lst]")

prints result/value of the expression/variable(using eval, the reason
to use eval is so you can print out the variable name/expresion 
and what it evaluates to without specifying it twice) with line number, function name, type.
Soon it will print in color to stand out better.

    d.debug_message("some message")

just prints out a string(no eval) but with func name/line #/file

The calls to debug_eval_print or debug_message default to blue if you want
some of the expressions/messages to print in a different color just supply
a different colorscheme.

ex.

    d.debug_eval_print("p[0]", colorscheme=d.ColorSchemes.FORE_RED)