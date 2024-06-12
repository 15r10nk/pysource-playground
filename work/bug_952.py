try:
    match name_4:
        case False:
            pass
except* name_5:
    pass
finally:
    name_5

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
