===========
debug_print
===========

In beta, still need to figure out what to do with logging.

ex

```python
import debug_print as d
a = [1,2,3,4,5]
d.debug_eval_print("a")
```

prints

![ex1](debug_print_example1.png)

or

```python
d.debug_eval_print("[x+1 for x in range(len(a))]")
```

which prints

![ex2](debug_print_example2.png)

prints result/value of the expression/variable(using eval, the reason
to use eval is so you can print out the variable name/expresion
and what it evaluates to without specifying it twice) with line number, function name, type.
Soon it will print in color to stand out better.

```python
d.debug_message("some message")
```

![ex3](debug_print_example3.png)

just prints out a string(no eval) but with func name/line #/file

The calls to debug_eval_print or debug_message default to blue if you want
some of the expressions/messages to print in a different color just supply
a different colorscheme.

ex.

```python
  d.debug_eval_print("a[0]", colorscheme=d.ColorSchemes.FORE_RED)
```

prints

![ex4](debug_print_example4.png)
