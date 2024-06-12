try:
    pass
except* {}:
    pass
finally:
    match name_1:
        case False:
            pass
name_3()

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
