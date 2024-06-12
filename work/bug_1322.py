with None:
    try:
        pass
    except* name_5:
        pass
    finally:
        if name_4:
            pass
        else:
            pass

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
