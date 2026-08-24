# Generated from /Volumes/External/Code/DPX-Php/grammars/PHPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PHPParser import PHPParser
else:
    from PHPParser import PHPParser

# This class defines a complete generic visitor for a parse tree produced by PHPParser.

class PHPParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PHPParser#phpFile.
    def visitPhpFile(self, ctx:PHPParser.PhpFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#declareStatement.
    def visitDeclareStatement(self, ctx:PHPParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#namespaceStatement.
    def visitNamespaceStatement(self, ctx:PHPParser.NamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useStatement.
    def visitUseStatement(self, ctx:PHPParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useDeclarationList.
    def visitUseDeclarationList(self, ctx:PHPParser.UseDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useItem.
    def visitUseItem(self, ctx:PHPParser.UseItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#topLevelStatement.
    def visitTopLevelStatement(self, ctx:PHPParser.TopLevelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classDeclaration.
    def visitClassDeclaration(self, ctx:PHPParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:PHPParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#traitDeclaration.
    def visitTraitDeclaration(self, ctx:PHPParser.TraitDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:PHPParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classMember.
    def visitClassMember(self, ctx:PHPParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useTraitStatement.
    def visitUseTraitStatement(self, ctx:PHPParser.UseTraitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#constDeclaration.
    def visitConstDeclaration(self, ctx:PHPParser.ConstDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#propertyDeclaration.
    def visitPropertyDeclaration(self, ctx:PHPParser.PropertyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:PHPParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:PHPParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#methodName.
    def visitMethodName(self, ctx:PHPParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#keywordAsIdentifier.
    def visitKeywordAsIdentifier(self, ctx:PHPParser.KeywordAsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#parameterList.
    def visitParameterList(self, ctx:PHPParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#parameter.
    def visitParameter(self, ctx:PHPParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classModifier.
    def visitClassModifier(self, ctx:PHPParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#memberModifier.
    def visitMemberModifier(self, ctx:PHPParser.MemberModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:PHPParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#qualifiedName.
    def visitQualifiedName(self, ctx:PHPParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#qualifiedSeparator.
    def visitQualifiedSeparator(self, ctx:PHPParser.QualifiedSeparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#type.
    def visitType(self, ctx:PHPParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#block.
    def visitBlock(self, ctx:PHPParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#statement.
    def visitStatement(self, ctx:PHPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#switchBlock.
    def visitSwitchBlock(self, ctx:PHPParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#expression.
    def visitExpression(self, ctx:PHPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:PHPParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#newExpression.
    def visitNewExpression(self, ctx:PHPParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#cloneExpression.
    def visitCloneExpression(self, ctx:PHPParser.CloneExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#closureExpression.
    def visitClosureExpression(self, ctx:PHPParser.ClosureExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#arrayExpression.
    def visitArrayExpression(self, ctx:PHPParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#arrayElement.
    def visitArrayElement(self, ctx:PHPParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#matchExpression.
    def visitMatchExpression(self, ctx:PHPParser.MatchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#matchArm.
    def visitMatchArm(self, ctx:PHPParser.MatchArmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#functionCall.
    def visitFunctionCall(self, ctx:PHPParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#memberAccess.
    def visitMemberAccess(self, ctx:PHPParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#argumentList.
    def visitArgumentList(self, ctx:PHPParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#argument.
    def visitArgument(self, ctx:PHPParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#literal.
    def visitLiteral(self, ctx:PHPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#operator.
    def visitOperator(self, ctx:PHPParser.OperatorContext):
        return self.visitChildren(ctx)



del PHPParser