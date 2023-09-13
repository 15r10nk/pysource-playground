
``` python
class name_0:

    async def name_2[*name_4]() -> lambda: name_4: # type: ignoresome text
        pass
```

output:
```
Traceback (most recent call last):
  File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
    compile(source,sys.argv[1],"exec")
  File "work/bug_64.py", line 3
    async def name_2[*name_4]() -> lambda: name_4: # type: ignoresome text
                                   ^^^^^^^^^^^^^^
SyntaxError: Cannot use lambda in annotation scope within class scope

```
            