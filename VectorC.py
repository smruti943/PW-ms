import sys
from antlr4 import *
from VectorLexer import VectorLexer
from VectorParser import VectorParser
from VectorVisitor import VectorVisitor
from EvaluateExpressionVisitor import EvaluateExpressionVisitor
from Vectorcodegen import CodeGen
from VectorAst import *
def main(argv):
    while True:
        fname = "input.Vector"
        with open(fname) as f:
            text_input = f.read()
        text = InputStream(input("->"))
        lexer = VectorLexer(text)
        stream = CommonTokenStream(lexer)
        codegen = CodeGen()

        module = codegen.module
        builder = codegen.builder
        printf = codegen.printf
        parser = VectorParser(stream,module,builder,printf)
        codegen.create_ir()
        codegen.save_ir("output.ll")
        ast = VectorVisitor().visitCompileUnit(tree)
        value = EvaluateExpressionVisitor().visit(ast)
        print('=', value)
if __name__ == '__main__':
 main(sys.argv)