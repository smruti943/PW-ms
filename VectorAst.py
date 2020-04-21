from llvmlite import ir

class NumberNode():
    def __init__(self, builder, module, value=None):
        self.builder = builder
        self.module = module
        self.value = value

class NegateNode():
    def __init__(self, builder, module, node):
        self.builder = builder
        self.module = module
        self.value = -1 * node.value

class InfixExpressionNode():
    def __init__(self, builder, module, left=None, right=None, value=None):
        self.builder = builder
        self.module = module
        self.value = value

class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, value])