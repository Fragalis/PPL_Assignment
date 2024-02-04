# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#structure.
    def visitStructure(self, ctx:ZCodeParser.StructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlinelist.
    def visitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#predeclist.
    def visitPredeclist(self, ctx:ZCodeParser.PredeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#postdeclist.
    def visitPostdeclist(self, ctx:ZCodeParser.PostdeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keywords_decl.
    def visitKeywords_decl(self, ctx:ZCodeParser.Keywords_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typename.
    def visitTypename(self, ctx:ZCodeParser.TypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydecl.
    def visitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numberlit_list.
    def visitNumberlit_list(self, ctx:ZCodeParser.Numberlit_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrpass_value.
    def visitArrpass_value(self, ctx:ZCodeParser.Arrpass_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrvalue_list.
    def visitArrvalue_list(self, ctx:ZCodeParser.Arrvalue_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrvalueprime.
    def visitArrvalueprime(self, ctx:ZCodeParser.ArrvalueprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrvalue.
    def visitArrvalue(self, ctx:ZCodeParser.ArrvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prototypedecl.
    def visitPrototypedecl(self, ctx:ZCodeParser.PrototypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#completed_funcdecl.
    def visitCompleted_funcdecl(self, ctx:ZCodeParser.Completed_funcdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typeparamdecl.
    def visitTypeparamdecl(self, ctx:ZCodeParser.TypeparamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrparramdecl.
    def visitArrparramdecl(self, ctx:ZCodeParser.ArrparramdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#main_func.
    def visitMain_func(self, ctx:ZCodeParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nonempt_newlnlist.
    def visitNonempt_newlnlist(self, ctx:ZCodeParser.Nonempt_newlnlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifclause.
    def visitIfclause(self, ctx:ZCodeParser.IfclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliflist.
    def visitEliflist(self, ctx:ZCodeParser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifclause.
    def visitElifclause(self, ctx:ZCodeParser.ElifclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseclause.
    def visitElseclause(self, ctx:ZCodeParser.ElseclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#otherstmt.
    def visitOtherstmt(self, ctx:ZCodeParser.OtherstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrelement.
    def visitArrelement(self, ctx:ZCodeParser.ArrelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#contstmt.
    def visitContstmt(self, ctx:ZCodeParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcallstmt.
    def visitFuncallstmt(self, ctx:ZCodeParser.FuncallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentlist.
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argprime.
    def visitArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argument.
    def visitArgument(self, ctx:ZCodeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringop.
    def visitStringop(self, ctx:ZCodeParser.StringopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relationalop.
    def visitRelationalop(self, ctx:ZCodeParser.RelationalopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicalop.
    def visitLogicalop(self, ctx:ZCodeParser.LogicalopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#addop.
    def visitAddop(self, ctx:ZCodeParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mulop.
    def visitMulop(self, ctx:ZCodeParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicalop1.
    def visitLogicalop1(self, ctx:ZCodeParser.Logicalop1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#signop.
    def visitSignop(self, ctx:ZCodeParser.SignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functioncall.
    def visitFunctioncall(self, ctx:ZCodeParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_expression.
    def visitElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexop.
    def visitIndexop(self, ctx:ZCodeParser.IndexopContext):
        return self.visitChildren(ctx)



del ZCodeParser