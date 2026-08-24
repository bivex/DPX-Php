# Generated from /Volumes/External/Code/DPX-Php/grammars/PHPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PHPParser import PHPParser
else:
    from PHPParser import PHPParser

# This class defines a complete listener for a parse tree produced by PHPParser.
class PHPParserListener(ParseTreeListener):

    # Enter a parse tree produced by PHPParser#phpFile.
    def enterPhpFile(self, ctx:PHPParser.PhpFileContext):
        pass

    # Exit a parse tree produced by PHPParser#phpFile.
    def exitPhpFile(self, ctx:PHPParser.PhpFileContext):
        pass


    # Enter a parse tree produced by PHPParser#declareStatement.
    def enterDeclareStatement(self, ctx:PHPParser.DeclareStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#declareStatement.
    def exitDeclareStatement(self, ctx:PHPParser.DeclareStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#namespaceStatement.
    def enterNamespaceStatement(self, ctx:PHPParser.NamespaceStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#namespaceStatement.
    def exitNamespaceStatement(self, ctx:PHPParser.NamespaceStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#useStatement.
    def enterUseStatement(self, ctx:PHPParser.UseStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#useStatement.
    def exitUseStatement(self, ctx:PHPParser.UseStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#useDeclarationList.
    def enterUseDeclarationList(self, ctx:PHPParser.UseDeclarationListContext):
        pass

    # Exit a parse tree produced by PHPParser#useDeclarationList.
    def exitUseDeclarationList(self, ctx:PHPParser.UseDeclarationListContext):
        pass


    # Enter a parse tree produced by PHPParser#useItem.
    def enterUseItem(self, ctx:PHPParser.UseItemContext):
        pass

    # Exit a parse tree produced by PHPParser#useItem.
    def exitUseItem(self, ctx:PHPParser.UseItemContext):
        pass


    # Enter a parse tree produced by PHPParser#topLevelStatement.
    def enterTopLevelStatement(self, ctx:PHPParser.TopLevelStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#topLevelStatement.
    def exitTopLevelStatement(self, ctx:PHPParser.TopLevelStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#classDeclaration.
    def enterClassDeclaration(self, ctx:PHPParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#classDeclaration.
    def exitClassDeclaration(self, ctx:PHPParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:PHPParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:PHPParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#traitDeclaration.
    def enterTraitDeclaration(self, ctx:PHPParser.TraitDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#traitDeclaration.
    def exitTraitDeclaration(self, ctx:PHPParser.TraitDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:PHPParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:PHPParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#classMember.
    def enterClassMember(self, ctx:PHPParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by PHPParser#classMember.
    def exitClassMember(self, ctx:PHPParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by PHPParser#useTraitStatement.
    def enterUseTraitStatement(self, ctx:PHPParser.UseTraitStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#useTraitStatement.
    def exitUseTraitStatement(self, ctx:PHPParser.UseTraitStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#constDeclaration.
    def enterConstDeclaration(self, ctx:PHPParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#constDeclaration.
    def exitConstDeclaration(self, ctx:PHPParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#propertyDeclaration.
    def enterPropertyDeclaration(self, ctx:PHPParser.PropertyDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#propertyDeclaration.
    def exitPropertyDeclaration(self, ctx:PHPParser.PropertyDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:PHPParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:PHPParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PHPParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PHPParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#methodName.
    def enterMethodName(self, ctx:PHPParser.MethodNameContext):
        pass

    # Exit a parse tree produced by PHPParser#methodName.
    def exitMethodName(self, ctx:PHPParser.MethodNameContext):
        pass


    # Enter a parse tree produced by PHPParser#keywordAsIdentifier.
    def enterKeywordAsIdentifier(self, ctx:PHPParser.KeywordAsIdentifierContext):
        pass

    # Exit a parse tree produced by PHPParser#keywordAsIdentifier.
    def exitKeywordAsIdentifier(self, ctx:PHPParser.KeywordAsIdentifierContext):
        pass


    # Enter a parse tree produced by PHPParser#parameterList.
    def enterParameterList(self, ctx:PHPParser.ParameterListContext):
        pass

    # Exit a parse tree produced by PHPParser#parameterList.
    def exitParameterList(self, ctx:PHPParser.ParameterListContext):
        pass


    # Enter a parse tree produced by PHPParser#parameter.
    def enterParameter(self, ctx:PHPParser.ParameterContext):
        pass

    # Exit a parse tree produced by PHPParser#parameter.
    def exitParameter(self, ctx:PHPParser.ParameterContext):
        pass


    # Enter a parse tree produced by PHPParser#classModifier.
    def enterClassModifier(self, ctx:PHPParser.ClassModifierContext):
        pass

    # Exit a parse tree produced by PHPParser#classModifier.
    def exitClassModifier(self, ctx:PHPParser.ClassModifierContext):
        pass


    # Enter a parse tree produced by PHPParser#memberModifier.
    def enterMemberModifier(self, ctx:PHPParser.MemberModifierContext):
        pass

    # Exit a parse tree produced by PHPParser#memberModifier.
    def exitMemberModifier(self, ctx:PHPParser.MemberModifierContext):
        pass


    # Enter a parse tree produced by PHPParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:PHPParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by PHPParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:PHPParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by PHPParser#qualifiedName.
    def enterQualifiedName(self, ctx:PHPParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by PHPParser#qualifiedName.
    def exitQualifiedName(self, ctx:PHPParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by PHPParser#qualifiedSeparator.
    def enterQualifiedSeparator(self, ctx:PHPParser.QualifiedSeparatorContext):
        pass

    # Exit a parse tree produced by PHPParser#qualifiedSeparator.
    def exitQualifiedSeparator(self, ctx:PHPParser.QualifiedSeparatorContext):
        pass


    # Enter a parse tree produced by PHPParser#type.
    def enterType(self, ctx:PHPParser.TypeContext):
        pass

    # Exit a parse tree produced by PHPParser#type.
    def exitType(self, ctx:PHPParser.TypeContext):
        pass


    # Enter a parse tree produced by PHPParser#block.
    def enterBlock(self, ctx:PHPParser.BlockContext):
        pass

    # Exit a parse tree produced by PHPParser#block.
    def exitBlock(self, ctx:PHPParser.BlockContext):
        pass


    # Enter a parse tree produced by PHPParser#statement.
    def enterStatement(self, ctx:PHPParser.StatementContext):
        pass

    # Exit a parse tree produced by PHPParser#statement.
    def exitStatement(self, ctx:PHPParser.StatementContext):
        pass


    # Enter a parse tree produced by PHPParser#switchBlock.
    def enterSwitchBlock(self, ctx:PHPParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by PHPParser#switchBlock.
    def exitSwitchBlock(self, ctx:PHPParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by PHPParser#expression.
    def enterExpression(self, ctx:PHPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#expression.
    def exitExpression(self, ctx:PHPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:PHPParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:PHPParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#newExpression.
    def enterNewExpression(self, ctx:PHPParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#newExpression.
    def exitNewExpression(self, ctx:PHPParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#cloneExpression.
    def enterCloneExpression(self, ctx:PHPParser.CloneExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#cloneExpression.
    def exitCloneExpression(self, ctx:PHPParser.CloneExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#closureExpression.
    def enterClosureExpression(self, ctx:PHPParser.ClosureExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#closureExpression.
    def exitClosureExpression(self, ctx:PHPParser.ClosureExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#arrayExpression.
    def enterArrayExpression(self, ctx:PHPParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#arrayExpression.
    def exitArrayExpression(self, ctx:PHPParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#arrayElement.
    def enterArrayElement(self, ctx:PHPParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by PHPParser#arrayElement.
    def exitArrayElement(self, ctx:PHPParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by PHPParser#matchExpression.
    def enterMatchExpression(self, ctx:PHPParser.MatchExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#matchExpression.
    def exitMatchExpression(self, ctx:PHPParser.MatchExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#matchArm.
    def enterMatchArm(self, ctx:PHPParser.MatchArmContext):
        pass

    # Exit a parse tree produced by PHPParser#matchArm.
    def exitMatchArm(self, ctx:PHPParser.MatchArmContext):
        pass


    # Enter a parse tree produced by PHPParser#functionCall.
    def enterFunctionCall(self, ctx:PHPParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PHPParser#functionCall.
    def exitFunctionCall(self, ctx:PHPParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PHPParser#memberAccess.
    def enterMemberAccess(self, ctx:PHPParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by PHPParser#memberAccess.
    def exitMemberAccess(self, ctx:PHPParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by PHPParser#argumentList.
    def enterArgumentList(self, ctx:PHPParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by PHPParser#argumentList.
    def exitArgumentList(self, ctx:PHPParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by PHPParser#argument.
    def enterArgument(self, ctx:PHPParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PHPParser#argument.
    def exitArgument(self, ctx:PHPParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PHPParser#literal.
    def enterLiteral(self, ctx:PHPParser.LiteralContext):
        pass

    # Exit a parse tree produced by PHPParser#literal.
    def exitLiteral(self, ctx:PHPParser.LiteralContext):
        pass


    # Enter a parse tree produced by PHPParser#operator.
    def enterOperator(self, ctx:PHPParser.OperatorContext):
        pass

    # Exit a parse tree produced by PHPParser#operator.
    def exitOperator(self, ctx:PHPParser.OperatorContext):
        pass



del PHPParser