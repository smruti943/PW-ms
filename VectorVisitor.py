# Generated from Vector.g4 by ANTLR 4.8
from antlr4 import *
from VectorAst import *
if __name__ is not None and "." in __name__:
    from .VectorParser import VectorParser
else:
    from VectorParser import VectorParser

# This class defines a complete generic visitor for a parse tree produced by VectorParser.
class VectorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VectorParser#compileUnit.
    def visitCompileUnit(self, ctx:VectorParser.CompileUnitContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by VectorParser#infixExpr.
    def visitInfixExpr(self, ctx:VectorParser.InfixExprContext):
        node = InfixExpressionNode()
        if ctx.OP_ADD():
            node.value = '+'
        elif ctx.OP_DIV():
            node.value = '/'
        elif ctx.OP_MUL():
            node.value = '*'
        elif ctx.OP_SUB():
            node.value = '-'
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node


    # Visit a parse tree produced by VectorParser#unaryExpr.
    def visitUnaryExpr(self, ctx:VectorParser.UnaryExprContext):
        if ctx.OP_ADD():
            return self.visit(ctx.expr())
        elif ctx.OP_SUB():
            return NegateNode(self.visit(ctx.expr()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VectorParser#funcExpr.
    def visitFuncExpr(self, ctx:VectorParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VectorParser#numberExpr.
    def visitNumberExpr(self, ctx:VectorParser.NumberExprContext):
        return NumberNode(value=int(str(ctx.NUM())))


    # Visit a parse tree produced by VectorParser#parensExpr.
    def visitParensExpr(self, ctx:VectorParser.ParensExprContext):
        return self.visit(ctx.expr())



del VectorParser
