from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Var:
    # name: str
    # typ: Type
    # modifier: str
    def __init__(self, name, typ) -> None:
        self.name = name
        self.typ = typ
        
class Func:
    # name: str
    # param: list[Var]
    # typ: Type
    # body: Stmt
    def __init__(self, name, param, typ, body = None) -> None:
        self.name = name
        self.param = param
        self.typ = typ
        self.body = body

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ctx):
        self.ctx = ctx
        self.symtab = [[
            Func("readNumber", [], NumberType()),
            Func("readBool", [], BoolType()),
            Func("readString", [], StringType()),
            Func("writeNumber", [Var("", NumberType())], VoidType()),
            Func("writeBool", [Var("", BoolType())], VoidType()),
            Func("writeString", [Var("", StringType())], VoidType()),
        ]]
        self.currentVariable = None
        self.noEntryPoint = True
        self.isCalled = False
        self.inferred = False
        self.inLoop = []
        self.returnType = None
        self.noBodyFunction = []
        self.hasReturn = False
        self.returnList = []
        self.arrayLiteral = []
        self.currentFunction = None
        pass

    def infer(self, expr, typ, symtab):
        if type(expr) is Id:
            for sym in symtab:
                id_sym = self.lookup(expr.name, sym, lambda x: x.name)
                if id_sym is not None and type(id_sym) is Var:
                    id_sym.typ = typ
                    
        elif type(expr) in [CallStmt, CallExpr]:
            for func_sym in symtab[-1]:
                if type(func_sym) is Func and func_sym.name == expr.name.name and func_sym.typ is None:
                    func_sym.typ = typ
                    self.isCalled = True
                    self.visit(
                        FuncDecl(
                            Id(func_sym.name),
                            list(map(lambda x: VarDecl(Id(x.name), x.typ, None, None), func_sym.param)),
                            func_sym.body
                        ),
                        symtab
                    )
                    self.isCalled = False
        
        else:
            if type(typ) is not ArrayType:
                self.inferred = False
            else:
                for val in expr.value:
                    if len(typ.size) == 1:
                        self.infer(val, typ.eleType, symtab)
                    else:
                        self.infer(val, ArrayType(typ.size[1:], typ.eleType, symtab))
                
    def check(self):
        self.visitProgram(self.ctx, self.symtab)

    # decl: List[Decl]  # empty list if there is no statement in block
    def visitProgram(self, ctx:Program, symtab):
        for decl in ctx.decl:
            symtab = self.visit(decl, symtab)
        if self.noBodyFunction != []:
            raise NoDefinition(self.noBodyFunction[0].name.name)
        for func in symtab[-1]:
            if type(func) is Func and func.name == "main" and type(func.typ) is VoidType and func.param == []:
                self.noEntryPoint = False
                break
        if self.noEntryPoint:
            raise NoEntryPoint()
        
    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ctx:VarDecl, symtab):
        if self.lookup(ctx.name.name, symtab[0], lambda x: x.name):
            raise Redeclared(Variable(), ctx.name.name)
    
        self.currentVariable = ctx.name.name
        l_type = ctx.varType
        if ctx.varInit is not None:
            r_type = self.visit(ctx.varInit, symtab)
            if (l_type is None and r_type is None) or (type(l_type) is not type(r_type)):
                raise TypeMismatchInStatement(ctx)
            
            if type(l_type) is ArrayType:
                if l_type.size[:len(r_type.size)] != r_type.size:
                    raise TypeMismatchInStatement(ctx)
                if r_type.eleType is None:
                    self.infer(ctx.varInit, l_type, symtab)
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                else:
                    if type(r_type.eleType) is not type(l_type.eleType):
                        raise TypeMismatchInStatement(ctx)
            symtab[0] += [Var(ctx.name.name, l_type)]
        
        else:
            if r_type is None:
                if l_type is None:
                    raise TypeCannotBeInferred(ctx)
                else:
                    if type(ctx.varInit) in [Id, CallExpr, ArrayLiteral]:
                        self.infer(ctx.varInit, l_type, symtab)
                        if self.inferred == False:
                            raise TypeCannotBeInferred(ctx)
                        symtab[0] += [Var(ctx.name.name, l_type)]
                    else:
                        raise TypeCannotBeInferred(ctx)
            else:
                symtab[0] += [Var(ctx.name.name, r_type)]
        self.arrayLiteral = []
        self.currentVariable = None

    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ctx:FuncDecl, symtab):
        # Lookup the function name
        func = self.lookup(ctx.name.name, symtab[-1], lambda x: x.name)
        # if it's declared WITH the body
        if func is not None and func.body is not None and self.isCalled == False:
            raise Redeclared(Function(), ctx.name.name)
        
        # Parameter in function Scope
        params = []
        for param in ctx.param:
            if self.lookup(param.name.name, params, lambda x: x.name) is not None:
                raise Redeclared(Parameter(), param.name.name)
            params += [Var(param.name.name, self.visit(param.varType, symtab))]
        
        symtab = [params] + symtab
        
        # if Prototype
        if ctx.body is None:
            if self.isCalled == False:
                self.noBodyFunction += [ctx]
            symtab[-1] += [Func(ctx.name.name, params, None, None)]
        # if not Prototype
        else:
            for f in self.noBodyFunction:
                if f.name.name == ctx.name.name:
                    self.noBodyFunction.remove(f)
                    
        # Function check
        func_found = False
        for func_sym in symtab[-1]:
            # If function found
            if type(func_sym) is Func and func_sym.name == ctx.name.name:
                func_found = True
                # If the number of params not match
                if len(func_sym.param) != len(params):
                    raise Redeclared(Function(), ctx.name.name)
                # If param type doesn't match
                for param_idx in range(len(params)):
                    l_type = func_sym.param[param_idx].typ
                    r_type = params[param_idx].typ
                    # if unmatch scalar type
                    if type(l_type) is not type(r_type):
                        raise Redeclared(Function(), ctx.name.name)
                    # if both are array type
                    if type(l_type) is ArrayType:
                        # if unmatch element type
                        if type(l_type.eleType) is not type(r_type.eleType):
                            raise Redeclared(Function(), ctx.name.name)
                        # if unmatch dimensions
                        if len(l_type.size) != len(r_type.size):
                            raise Redeclared(Function(), ctx.name.name)
                        # if unmatch sizes
                        for idx in range(len(l_type.size)):
                            if l_type.size[idx] != r_type.size[idx]:
                                raise Redeclared(Function(), ctx.name.name)
                # If here means it's the same function
                self.visit(ctx.body, symtab)
                # return type
                func_sym.typ = self.returnType if self.returnType else (VoidType() if self.returnList == [] else None)
                break    
            
            # if first declaration:
            if not func_found:
                func_sym = Func(ctx.name.name, params, self.returnType, self.body)
                self.visit(ctx.body, symtab)
                ret_type = self.returnType if self.returnType else (VoidType() if self.returnList == [] else None)
                if func_sym.typ is None:
                    func_sym.typ = ret_type
                symtab += [func_sym]
        self.returnType = None
        self.hasReturn = False
        symtab = symtab[1:]
        self.returnList = []

    def visitNumberType(self, ctx:NumberType, symtab):
        return NumberType()

    def visitBoolType(self, ctx:BoolType, symtab):
        return BoolType()

    def visitStringType(self, ctx:StringType, symtab):
        return StringType()

    # size: List[float]
    # eleType: Type
    def visitArrayType(self, ctx:ArrayType, symtab):
        return ArrayType(ctx.size, self.visit(ctx.eleType, symtab))

    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ctx:BinaryOp, symtab):
        l_type = self.visit(ctx.left, symtab)
        r_type = self.visit(ctx.right, symtab)
        if ctx.op in ['+', '-', "*", "/", "%", "=", "!=", "<", ">", "<=", ">="]:
            if l_type is None:
                if type(ctx.left) in [Id, CallExpr]:
                    self.infer(ctx.left, NumberType(), symtab)
                    if self.inferred == False:
                        return None
                    l_type = NumberType()
                return None
            if r_type is None:
                if type(ctx.right) in [Id, CallExpr]:
                    self.infer(ctx.right, NumberType(), symtab)
                    if self.inferred == False:
                        return None
                    r_type = NumberType()
                return None
            if type(l_type) is not NumberType() or type(r_type) is not NumberType():
                raise TypeMismatchInExpression(ctx)
            return NumberType() if ctx.op in ['+', '-', "*", "/", "%"] else BoolType()

        elif ctx.op in ["and", "or"]:
            if l_type is None:
                if type(ctx.left) in [Id, CallExpr]:
                    self.infer(ctx.left, BoolType(), symtab)
                    if self.inferred == False:
                        return None
                    l_type = BoolType()
                return None
            if r_type is None:
                if type(ctx.right) in [Id, CallExpr]:
                    self.infer(ctx.right, BoolType(), symtab)
                    if self.inferred == False:
                        return None
                    r_type = BoolType()
                return None
            if type(l_type) is not BoolType() or type(r_type) is not BoolType():
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        
        else:
            if l_type is None:
                if type(ctx.left) in [Id, CallExpr]:
                    self.infer(ctx.left, StringType(), symtab)
                    if self.inferred == False:
                        return None
                    l_type = StringType()
                return None
            if r_type is None:
                if type(ctx.right) in [Id, CallExpr]:
                    self.infer(ctx.right, StringType(), symtab)
                    if self.inferred == False:
                        return None
                    r_type = StringType()
                return None
            if type(l_type) is not StringType() or type(r_type) is not StringType():
                raise TypeMismatchInExpression(ctx)
            return StringType() if ctx.op == "..." else BoolType()
        
    # op: str
    # operand: Expr
    def visitUnaryOp(self, ctx:UnaryOp, symtab):
        expr_type = self.visit(ctx.operand, symtab)
        # - unary => number type
        if ctx.op == '-':
            # if no type => infer is needed
            if expr_type is None:
                # if operand is ArrayCell
                if type(ctx.operand) not in [Id, CallExpr]:
                    return None
                # if it's Id / CallExpr
                self.infer(ctx.operand, NumberType(), symtab)
                if self.inferred == False:
                    return None
                return NumberType()
            # if there is a type
            else:
                # if not NumberType
                if type(expr_type) is not NumberType:
                    raise TypeMismatchInExpression(ctx)
            return NumberType()
        
        # not unary => bool type
        else:
            # if no type => infer is needed
            if expr_type is None:
                # if operand is ArrayCell
                if type(ctx.operand) not in [Id, CallExpr]:
                    return None
                # if it's Id / CallExpr
                self.infer(ctx.operand, BoolType(), symtab)
                if self.inferred == False:
                    return None
                return BoolType()
            # if there is a type
            else:
                # if not BoolType
                if type(expr_type) is not BoolType:
                    raise TypeMismatchInExpression(ctx)
            return BoolType()

    # name: Id
    # args: List[Expr]
    def visitCallExpr(self, ctx:CallExpr, symtab):
        if self.currentVariable is not None and ctx.name.name == self.currentVariable:
            raise TypeMismatchInExpression(ctx)
        
        self.inferred = True
        local_symtab = symtab[:-1]
        for para in local_symtab:
            if self.lookup(ctx.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInExpression(ctx)
        
        found = self.lookup(ctx.name.name, symtab[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not Func):
            raise Undeclared(Function(), ctx.name.name)
        
        if type(found.typ) is VoidType:
            raise TypeMismatchInExpression(ctx)
        if len(ctx.args) != len(found.param):
            raise TypeMismatchInExpression(ctx)
        
        for idx in range(len(ctx.args)):
            arg_typ = self.visit(ctx.args[idx], symtab)
            if arg_typ is None:
                if type(ctx.args[idx]) not in [Id, CallExpr, ArrayLiteral]:
                    return None
                self.infer(ctx.args[idx], found.param[idx].typ, symtab)
                if self.inferred == False:
                    return None
                arg_typ = found.param[idx].typ
            else:
                if type(arg_typ) is not type(found.param[idx].typ):
                    raise TypeMismatchInExpression(ctx)
                if type(arg_typ) is ArrayType:
                    if arg_typ.size[:len(found.param[idx].typ.size)] != found.param[idx].typ.size:
                        raise TypeMismatchInExpression(ctx)
                    if arg_typ.eleType is None:
                        if type(ctx.value) in [Id, CallExpr, ArrayLiteral]:
                            self.infer(ctx.value, found.param[idx].typ, symtab)
                            if self.inferred == False:
                                return None
                            arg_typ = found.param[idx].typ
                        return None
                    if type(arg_typ.eleType) is not type(found.param[idx].typ.eleType) or arg_typ.size != found.param[idx].typ.size:
                        raise TypeMismatchInExpression(ctx)
        return found.typ
                
    # name: str
    def visitId(self, ctx:Id, symtab):
        # number x <- x => x is undeclared
        if self.currentVariable is not None and ctx.name == self.currentVariable:
            raise Undeclared(Identifier(), ctx.name)
        
        self.inferred = True
        # Find Id in the symtab
        for sym in symtab:
            varsym = self.lookup(ctx.name, sym, lambda x: x.name)
            # if Id is found
            if varsym is not None and type(varsym) is Var:
                # find and return the Id type
                for var in sym:
                    if var.name == ctx.name and type(var) is Var:
                        return var.typ
        # Can't find Id => raise exception
        raise Undeclared(Identifier(), ctx.name)
                
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ctx:ArrayCell, symtab):
        self.inferred = True
        arr_typ = self.visit(ctx.arr)
        if arr_typ is None:
            self.inferred = False
            return None
        if type(arr_typ) is not ArrayType or len(arr_typ.size) < len(ctx.idx):
            raise TypeMismatchInExpression(ctx)

        for cell in ctx.idx:
            typ = self.visit(cell, symtab)
            if typ is None:
                if type(cell) in [Id, CallExpr]:
                    self.infer(cell, NumberType(), symtab)
                    if self.inferred == False:
                        return None
                    typ = NumberType()
                return None
            if type(typ) is not NumberType:
                raise TypeMismatchInExpression(ctx)
        if len(arr_typ.size) == len(ctx.idx):
            return arr_typ.eleType
        return ArrayType(arr_typ.size[len(ctx.idx):], arr_typ.eleType)

    def visitBlock(self, ctx:Block, symtab):
        symtab = [[]] + symtab
        for stmt in ctx.stmt:
            self.visit(stmt, symtab)
        self.hasReturn = False
        symtab = symtab[1:]
        self.arrayLiteral = []

    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ctx:If, symtab):
        cond_typ = self.visit(ctx.expr, symtab)
        if cond_typ is None:
            if type(ctx.expr) not in [Id, CallExpr, ArrayLiteral]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.expr, BoolType(), symtab)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            cond_typ = BoolType()
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt)
        self.hasReturn = False
        for elif_expr, elif_stmt in ctx.elifStmt:
            cond_typ = self.visit(elif_expr, symtab)
            if cond_typ is None:
                if type(elif_expr) not in [Id, CallExpr]:
                    raise TypeCannotBeInferred(ctx)
                self.infer(elif_expr, BoolType(), symtab)
                if self.inferred == False:
                    raise TypeCannotBeInferred(ctx)
                cond_typ = BoolType()
            if type(cond_typ) is not BoolType:
                raise TypeMismatchInStatement(ctx)
            self.visit(ctx.elif_stmt)
        if ctx.elseStmt:
            self.visit(ctx.elseStmt, symtab)
        self.arrayLiteral = []
            
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    def visitFor(self, ctx:For, symtab):
        self.inLoop = [1]
        itr = self.visit(ctx.name, symtab)
        if itr is None:
            self.infer(ctx.name, NumberType(), symtab)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            itr = NumberType()
        if type(itr) is not NumberType:
            raise TypeMismatchInStatement(ctx)
    
        cond_typ = self.visit(ctx.condExpr, symtab)
        if cond_typ is None:
            if type(ctx.condExpr) not in [Id, CallExpr]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.condExpr, BoolType(), symtab)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            cond_typ = BoolType()
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        
        update_typ = self.visit(ctx.updExpr, symtab)
        if update_typ is None:
            if type(ctx.updExpr) not in [Id, CallExpr]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.updExpr, NumberType(), symtab)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            update_typ = NumberType()
        if type(update_typ) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        
        self.visit(ctx.body, symtab)
        self.arrayLiteral = []
        self.inLoop = self.inLoop[:-1]

    def visitContinue(self, ctx:Continue, symtab):
        if self.inLoop == []:
            return MustInLoop(ctx)
        self.arrayLiteral = []

    def visitBreak(self, ctx:Break, symtab):
        if self.inLoop == []:
            return MustInLoop(ctx)
        self.arrayLiteral = []
        
    # expr: Expr = None  # None if there is no expression after return
    def visitReturn(self, ctx:Return, symtab):
        # if there is already a return statement
        if self.hasReturn:
            return
        # the function has a return statement
        self.hasReturn = True
        # if VoidType()
        if ctx.expr is None:
            self.returnType = VoidType()
        # if type
        else:    
            ret_type =  self.visit(ctx.expr, symtab)
            func = self.lookup(self.currentFunction, symtab[-1], lambda x: x.name)
            if func.typ is None:
                if ret_type is None:
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                    self.returnList += [ctx]
                else:
                    self.returnType = ret_type
                    func.typ = ret_type
                    while self.returnList != []:
                        if type(self.returnList[0].expr) not in [Id, CallExpr, ArrayLiteral]:
                            raise TypeCannotBeInferred(self.returnList[0])
                        self.infer(self.returnList[0], ret_type, symtab)
                        if self.inferred == False:
                            raise TypeCannotBeInferred(ctx)
                        self.returnList = self.returnList[1:]
            else:
                if type(func.typ) is VoidType:
                    raise TypeMismatchInStatement(ctx)
                if ret_type is None:
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                    if type(ctx.expr) not in [Id, CallExpr, ArrayLiteral]:
                        raise TypeCannotBeInferred(ctx)
                    self.infer(ctx.expr, func.typ, symtab)
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                else:
                    # scalar type
                    if type(func.typ) is not type(ret_type):
                        raise TypeMismatchInStatement(ctx)
                    # array type
                if type(func) is ArrayType:
                    if func.size[:len(ret_type.size)] != ret_type.size:
                        raise TypeMismatchInStatement(ctx)
                    if func.eleType is None:
                        if type(ctx.value) in [Id, CallExpr, ArrayLiteral]:
                            self.infer(ctx.value, ret_type, symtab)
                            if self.inferred == False:
                                return None
                            func = ret_type
                        return None
                    if type(func.eleType) is not type(ret_type.eleType) or func.size != ret_type.size:
                        raise TypeMismatchInStatement(ctx)
        self.arrayLiteral = []
                
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ctx:Assign, symtab):
        r_type, l_type = self.visit(ctx.exp, symtab), self.visit(ctx.lhs)
        if r_type is None and l_type is None:
            raise TypeCannotBeInferred(ctx)


    def visitCallStmt(self, ctx:CallStmt, symtab):
        self.inferred = True
        local_symtab = symtab[:-1]
        for para in local_symtab:
            if self.lookup(ctx.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInStatement(ctx)
        
        found = self.lookup(ctx.name.name, symtab[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not Func):
            raise Undeclared(Function(), ctx.name.name)
        
        if found.typ is not None and type(found.typ) is not VoidType:
            raise TypeMismatchInStatement(ctx)
        if len(ctx.args) != len(found.param):
            raise TypeMismatchInStatement(ctx)
        
        for idx in range(len(ctx.args)):
            arg_typ = self.visit(ctx.args[idx], symtab)
            if arg_typ is None:
                if type(ctx.args[idx]) not in [Id, CallExpr, ArrayLiteral]:
                    return None
                self.infer(ctx.args[idx], found.param[idx].typ, symtab)
                if self.inferred == False:
                    return None
                arg_typ = found.param[idx].typ
            else:
                if type(arg_typ) is not type(found.param[idx].typ):
                    raise TypeMismatchInStatement(ctx)
                if type(arg_typ) is ArrayType:
                    if arg_typ.size[:len(found.param[idx].typ.size)] != found.param[idx].typ.size:
                        raise TypeMismatchInStatement(ctx)
                    if arg_typ.eleType is None:
                        if type(ctx.value) in [Id, CallExpr, ArrayLiteral]:
                            self.infer(ctx.value, found.param[idx].typ, symtab)
                            if self.inferred == False:
                                return None
                            arg_typ = found.param[idx].typ
                        return None
                    if type(arg_typ.eleType) is not type(found.param[idx].typ.eleType) or arg_typ.size != found.param[idx].typ.size:
                        raise TypeMismatchInStatement(ctx)
        if found.typ is None:
            self.infer(ctx, VoidType(), symtab)
        self.arrayLiteral = []

    def visitNumberLiteral(self, ctx:NumberLiteral, symtab):
        return NumberType()

    def visitBooleanLiteral(self, ctx:BooleanLiteral, symtab):
        return BoolType()

    def visitStringLiteral(self, ctx:StringLiteral, symtab):
        return StringType()

    # value: List[Expr]
    def visitArrayLiteral(self, ctx:ArrayLiteral, symtab):
        if ctx not in self.arrayLiteral:
            self.arrayLiteral += [ctx]
            
        typ = None
        for val in ctx.value:
            typ = self.visit(val, symtab)
            if typ is not None:
                break
        
        if typ is not None:
            for val in ctx.value:
                val_typ = self.visit(val, symtab)
                if typ is None:
                    if type(val_typ) in [Id, CallExpr, ArrayLiteral]:
                        self.infer(val_typ, typ, symtab)
                        if self.inferred == False:
                            return None
                        val_typ = typ
                    return None
                if type(val_typ) is not type(typ):
                    raise TypeMismatchInExpression(self.arrayLiteral[0])
                if type(val_typ) is ArrayType:
                    if val_typ.size[:len(typ.size)] != typ.size:
                        raise TypeMismatchInExpression(self.arrayLiteral[0])
                    if val_typ.eleType is None:
                        if type(ctx.value) in [Id, CallExpr, ArrayLiteral]:
                            self.infer(ctx.value, typ, symtab)
                            if self.inferred == False:
                                return None
                            val_typ = typ
                        return None
                    if type(val_typ.eleType) is not type(typ.eleType) or val_typ.size != typ.size:
                        raise TypeMismatchInExpression(self.arrayLiteral[0])
        
            if type(typ) is not ArrayType:
                self.arrayLiteral = self.arrayLiteral[:-1]
                return ArrayType([len(ctx.value)], typ)
            self.arrayLiteral = self.arrayLiteral[:-1]
            return ArrayType([len(ctx.value)] + typ.size, typ.eleType)