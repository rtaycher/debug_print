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

<span style="color:blue">File: ./example.py</span> | <span style="color:darkblue">Line:4</span> | <span style="color:blue">Func:`main`</span>
<span style="color:blue">Expr: a</span> | <span style="color:darkblue">type:`<type 'list'>`</span> |  <span style="color:blue">result:[1, 2, 3, 4, 5]</span>


or

```
d.debug_eval_print("[x+1 for x in range(len(a))]")
```

which prints

<span style="color:blue">File: ./example.py</span> | <span style="color:darkblue">Line:5</span> | <span style="color:blue">Func:`main`</span>
<span style="color:blue">Expr: [x+1 for x in range(len(a))]</span> | <span style="color:darkblue">type:`<type 'list'>`</span> |  <span style="color:blue">result:[1, 2, 3, 4, 5]</span>

prints result/value of the expression/variable(using eval, the reason
to use eval is so you can print out the variable name/expresion 
and what it evaluates to without specifying it twice) with line number, function name, type.
Soon it will print in color to stand out better.

```python
d.debug_message("some message")
```
<span style="color:blue">File: ./example.py</span> | <span style="color:darkblue">Line:8</span> | <span style="color:blue">Func:main</span>
<span style="color:darkblue">some message</span>

just prints out a string(no eval) but with func name/line #/file

The calls to debug_eval_print or debug_message default to blue if you want
some of the expressions/messages to print in a different color just supply
a different colorscheme.

ex.

```python
d.debug_eval_print("a[0]", colorscheme=d.ColorSchemes.FORE_RED)
```

<span style="color:red">File: ./example.py</span> | <span style="color:darkred">Line:5</span> | <span style="color:red">Func:`main`</span>
<span style="color:red">Expr: a[0]</span> | <span style="color:darkred">type:`<type 'int'>`</span> |  <span style="color:red">1</span>
