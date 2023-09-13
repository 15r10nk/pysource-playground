
``` python
name_0
global name_0, name_5, name_3, name_2
```

output:
```
Traceback (most recent call last):
  File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
    compile(source,sys.argv[1],"exec")
  File "work/bug_82.py", line 2
    global name_0, name_5, name_3, name_2
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: name 'name_0' is used prior to global declaration

```
            