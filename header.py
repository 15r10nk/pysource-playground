class Generic:
    def __init__(self):
        self.stop_iter=False

    def __iter__(self):
        yield Generic()
        yield Generic()

    def __aiter__(self):
        return Generic()

    def __anext__(self):
        if self.stop_iter:
            raise StopIteration()
        else:
            self.stop_iter=True
        return Generic()

    def __call__(self,*a,**ka):
        return Generic()

    def __getitem__(self,key):
        return Generic()

    def __setitem__(self,key,value):
        pass

    def __getattr__(self,name):
        return Generic()

    def __setattr__(self,name,value):
        pass

    # Arithmetic operators
    def __add__(self, other): return Generic()
    def __sub__(self, other): return Generic()
    def __mul__(self, other): return Generic()
    def __matmul__(self, other): return Generic()
    def __truediv__(self, other): return Generic()
    def __floordiv__(self, other): return Generic()
    def __mod__(self, other): return Generic()
    def __divmod__(self, other): return Generic()
    def __pow__(self, other, modulo=None): return Generic()
    def __lshift__(self, other): return Generic()
    def __rshift__(self, other): return Generic()
    def __and__(self, other): return Generic()
    def __xor__(self, other): return Generic()
    def __or__(self, other): return Generic()

    # Reflected arithmetic operators
    def __radd__(self, other): return Generic()
    def __rsub__(self, other): return Generic()
    def __rmul__(self, other): return Generic()
    def __rmatmul__(self, other): return Generic()
    def __rtruediv__(self, other): return Generic()
    def __rfloordiv__(self, other): return Generic()
    def __rmod__(self, other): return Generic()
    def __rdivmod__(self, other): return Generic()
    def __rpow__(self, other, modulo=None): return Generic()
    def __rlshift__(self, other): return Generic()
    def __rrshift__(self, other): return Generic()
    def __rand__(self, other): return Generic()
    def __rxor__(self, other): return Generic()
    def __ror__(self, other): return Generic()

    # Unary operators
    def __neg__(self): return Generic()
    def __pos__(self): return Generic()
    def __abs__(self): return Generic()
    def __invert__(self): return Generic()

    # Comparison operators
    def __lt__(self, other): return Generic()
    def __le__(self, other): return Generic()
    def __eq__(self, other): return Generic()
    def __ne__(self, other): return Generic()
    def __gt__(self, other): return Generic()
    def __ge__(self, other): return Generic()

    # In-place operators
    def __iadd__(self, other): return Generic()
    def __isub__(self, other): return Generic()
    def __imul__(self, other): return Generic()
    def __imatmul__(self, other): return Generic()
    def __itruediv__(self, other): return Generic()
    def __ifloordiv__(self, other): return Generic()
    def __imod__(self, other): return Generic()
    def __ipow__(self, other, modulo=None): return Generic()
    def __ilshift__(self, other): return Generic()
    def __irshift__(self, other): return Generic()
    def __iand__(self, other): return Generic()
    def __ixor__(self, other): return Generic()
    def __ior__(self, other): return Generic()

    # Container operators
    def __contains__(self, item): return Generic()
    def __len__(self): return 1
    def __bool__(self): return True
    def __int__(self): return 1
    def __float__(self): return 1.0
    def __complex__(self): return complex(1, 0)
    def __index__(self): return 1
    def __str__(self): return "Generic"
    def __repr__(self): return "Generic()"
    def __hash__(self): return 0


for i in range(10):
    globals()[f"name_{i}"]=Generic()


def loop_limit(name,cache={}):
    if name not in cache:
        cache[name]=5

    if cache[name]==0:
        raise RuntimeError("break long loop")
    else:
        cache[name]-=1

def report_error(e,reported=[]):

    s=f"{type(e).__name__} {e}"
    if s in reported:
        return
    reported.append(s)
    print("catch error:",s)


