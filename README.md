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

<font color="blue">File: ./example.py</span> | <font color="darkblue">Line:4</span> | <font color="blue">Func:`main`</span>

<font color="blue">Expr: a</span> | <font color="darkblue">type:`<type 'list'>`</span> |  <font color="blue">result:[1, 2, 3, 4, 5]</span>


or

```
d.debug_eval_print("[x+1 for x in range(len(a))]")
```

which prints

<font color="blue">File: ./example.py</span> | <font color="darkblue">Line:5</span> | <font color="blue">Func:`main`</span>

<font color="blue">Expr: [x+1 for x in range(len(a))]</span> | <font color="darkblue">type:`<type 'list'>`</span> |  <font color="blue">result:[1, 2, 3, 4, 5]</span>

prints result/value of the expression/variable(using eval, the reason
to use eval is so you can print out the variable name/expresion 
and what it evaluates to without specifying it twice) with line number, function name, type.
Soon it will print in color to stand out better.

```python
d.debug_message("some message")
```
<font color="blue">File: ./example.py</span> | <font color="darkblue">Line:8</span> | <font color="blue">Func:main</span>

<font color="darkblue">some message</span>

just prints out a string(no eval) but with func name/line #/file

The calls to debug_eval_print or debug_message default to blue if you want
some of the expressions/messages to print in a different color just supply
a different colorscheme.

ex.

```python
d.debug_eval_print("a[0]", colorscheme=d.ColorSchemes.FORE_RED)
```

<font color="red">File: ./example.py</span> | <font color="darkred">Line:5</span> | <font color="red">Func:`main`</span>

<font color="red">Expr: a[0]</span> | <font color="darkred">type:`<type 'int'>`</span> |  <font color="red">1</span>
