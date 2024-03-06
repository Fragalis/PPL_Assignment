from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

# scope[0]: local -> decl -> scope[0]
# finder: all scopes
# scope[last]: global
# if id is var: scope[scope][id] = 0
# if id is func: scope[scope][id] = param_list

class Iden:
    # name : str
    # typ  : Type
    # modifier : str
    def __init__(self, name, typ, modifier):
        self.name = name
        self.typ = typ
        self.modifier = modifier

class StaticChecker(BaseVisitor, Utils):
    def visitProgram(self, ctx:Program, scope):
        scope = [[]]
        for decl in ctx.decl:
            scope = self.visit(decl, scope)
        
    def visitVarDecl(self, ctx:VarDecl, scope):
        name = self.visit(ctx.name, scope)
        # Redeclared Error
        for iden_list in scope:
            for iden in iden_list:
                if name == iden.name:
                    raise Redeclared(Variable(), name)

        # Declaration
        var_type = self.visit(ctx.varType, scope)
        modifier = self.visit(ctx.modifier, scope)
        value = self.visit(ctx.varInit, scope)
        var_decl = [Iden(name, type(value), None)]
        if modifier == None and type(value) is not type(var_type):
            raise TypeMismatchInStatement(ctx)
        elif modifier == "dynamic":
            var_decl.modifier = "dynamic"
        scope += var_decl
        return scope
            
    def visitFuncDecl(self, ctx:FuncDecl, scope):
        name = self.visit(ctx.name, scope)
        # Redeclared Error
        for iden_list in scope:
            for iden in iden_list:
                if name == iden.name:
                    raise Redeclared(Function(), name)

        # Declaration
        pass


    def visitNumberType(self, ctx:NumberType, scope):
        return NumberType()

    def visitBoolType(self, ctx:BoolType, scope):
        return BoolType()

    def visitStringType(self, ctx:StringType, scope):
        return StringType()

    def visitArrayType(self, ctx:ArrayType, scope):
        pass

    def visitBinaryOp(self, ctx:BinaryOp, scope):
        left_type = self.visit(ctx.left, scope)
        right_type = self.visit(ctx.right, scope)
        if type(left_type) is not type(right_type):
            raise TypeMismatchInExpression(ctx)
        ret_type = left_type    
        if ctx.op in ["...", "=="]:
            if ret_type is StringType: return StringType() if ctx.op == "..." else BoolType()
            else: raise TypeMismatchInExpression(ctx)
        elif ctx.op in ["=", "!=", "<", ">", "<=", ">="]:
            if ret_type is NumberType: return BoolType()
            else: raise TypeMismatchInExpression(ctx)
        elif ctx.op in ["and", "or"]:
            if ret_type is BoolType: return BoolType()
            else: raise TypeMismatchInExpression(ctx)
        else:
            if ret_type is NumberType: return NumberType()
            else: raise TypeMismatchInExpression(ctx)
        

    def visitUnaryOp(self, ctx:UnaryOp, scope):
        ret_type = self.visit(ctx.operand, scope)
        if ((ctx.op == "not") and (ret_type is BoolType)) or ((ctx.op == "-") and (ret_type is NumberType)):
            return ret_type
        raise TypeMismatchInExpression(ctx)

    def visitCallExpr(self, ctx:CallExpr, scope):
        pass
        
    def visitId(self, ctx:Id, scope):
        for id_list in scope:
            for id in id_list:
                if ctx.name == id:
                    return id
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx:ArrayCell, scope):
        pass

    def visitBlock(self, ctx:Block, scope):
        block_scope = [[]] + scope
        for stmt in ctx.stmt:
            self.visit(stmt, block_scope)

    def visitIf(self, ctx:If, scope):
        cond_expr = self.visit(ctx.expr ,scope)
        if type(cond_expr) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt, scope)
        for elif_clause in ctx.elifStmt:
            elif_cond_expr = self.visit(elif_clause[0], scope)
            if type(elif_cond_expr) is not BoolType:
                raise TypeMismatchInStatement(ctx)
            self.visit(elif_clause[1], scope)
        self.visit(ctx.elseStmt, scope)

    def visitFor(self, ctx:For, scope):
        name = self.visit(ctx.name, scope)
        if type(name) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        cond_expr = self.visit(ctx.condExpr, scope)
        if type(cond_expr) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        update_expr = self.visit(ctx.updExpr, scope)
        if type(update_expr) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.body, scope)

    def visitContinue(self, ctx:Continue, scope):
        pass

    def visitBreak(self, ctx:Break, scope):
        pass

    def visitReturn(self, ctx:Return, scope):
        expr = self.visit(ctx.expr,scope)
        return type(expr) if expr else VoidType()

    def visitAssign(self, ctx:Assign, scope):
        pass     

    def visitCallStmt(self, ctx:CallStmt, scope):
        pass

    def visitNumberLiteral(self, ctx:NumberLiteral, scope):
        return NumberType()

    def visitBooleanLiteral(self, ctx:BooleanLiteral, scope):
        return BoolType()

    def visitStringLiteral(self, ctx:StringLiteral, scope):
        return StringType()

    def visitArrayLiteral(self, ctx:ArrayLiteral, scope):
        pass