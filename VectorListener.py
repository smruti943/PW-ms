# Generated from Vector.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VectorParser import VectorParser
else:
    from VectorParser import VectorParser

# This class defines a complete listener for a parse tree produced by VectorParser.
class VectorListener(ParseTreeListener):

    # Enter a parse tree produced by VectorParser#compileUnit.
    def enterCompileUnit(self, ctx:VectorParser.CompileUnitContext):
        pass

    # Exit a parse tree produced by VectorParser#compileUnit.
    def exitCompileUnit(self, ctx:VectorParser.CompileUnitContext):
        pass


    # Enter a parse tree produced by VectorParser#infixExpr.
    def enterInfixExpr(self, ctx:VectorParser.InfixExprContext):
        pass

    # Exit a parse tree produced by VectorParser#infixExpr.
    def exitInfixExpr(self, ctx:VectorParser.InfixExprContext):
        pass


    # Enter a parse tree produced by VectorParser#unaryExpr.
    def enterUnaryExpr(self, ctx:VectorParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by VectorParser#unaryExpr.
    def exitUnaryExpr(self, ctx:VectorParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by VectorParser#funcExpr.
    def enterFuncExpr(self, ctx:VectorParser.FuncExprContext):
        pass

    # Exit a parse tree produced by VectorParser#funcExpr.
    def exitFuncExpr(self, ctx:VectorParser.FuncExprContext):
        pass


    # Enter a parse tree produced by VectorParser#numberExpr.
    def enterNumberExpr(self, ctx:VectorParser.NumberExprContext):
        pass

    # Exit a parse tree produced by VectorParser#numberExpr.
    def exitNumberExpr(self, ctx:VectorParser.NumberExprContext):
        pass


    # Enter a parse tree produced by VectorParser#parensExpr.
    def enterParensExpr(self, ctx:VectorParser.ParensExprContext):
        pass

    # Exit a parse tree produced by VectorParser#parensExpr.
    def exitParensExpr(self, ctx:VectorParser.ParensExprContext):
        pass

class KeyPrinter(VectorListener):
    def exitKey(self,ctx):
        print("Result is")

del VectorParser