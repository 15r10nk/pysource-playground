class name_1[*name_1]:

    async def name_1[**name_0](name_5: name_1, /): # type: 
        name_1

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
# SystemError: compiler_lookup_arg(name='name_1') with reftype=3 failed in <generic parameters of name_1>; freevars of code name_1: ('name_1',)
