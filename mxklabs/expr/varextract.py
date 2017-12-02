from mxklabs.expr.exprvisitor import ExprVisitor
from mxklabs.utils import memoise


class VarExtractor(ExprVisitor):
    """
    This class can be used to find all variables used in an expression.
    """

    @staticmethod
    def extract(expr):
        """
        Return the variables used in an expression.
        :param expr: The Expr object to evaluate.
        :return: A set object containing Var objects.
        """
        ee = VarExtractor()
        return expr.visit(ee)

    def __init__(self):
        """
        There is no need to instantiate this class manually. Use the extract
        method instead. This constructor is called internally.
        """
        ExprVisitor.__init__(self)

    @memoise
    def _visit_const(self, expr):
        '''
        Internal method for working the variables used in a Const object.
        :param expr: A Const object.
        :return: A empty set object.
        '''
        return self._visit_default(expr)

    @memoise
    def _visit_var(self, expr):
        '''
        Internal method for working the variables used in a Var object.
        :param expr: A Var object.
        :return: A set object containing just expr.
        '''
        return set([expr])

    @memoise
    def _visit_logical_and(self, expr):
        '''
        Internal method for working the variables used in a LogicalAnd object.
        :param expr: A LogicalAnd object.
        :return: A set object containing variables used in expr.
        '''
        return self._visit_default(expr)

    @memoise
    def _visit_logical_or(self, expr):
        '''
        Internal method for working the variables used in a LogicalOr object.
        :param expr: A LogicalOr object.
        :return: A set object containing variables used in expr.
        '''
        return self._visit_default(expr)

    @memoise
    def _visit_logical_not(self, expr):
        '''
        Internal method for working the variables used in a LogicalNot object.
        :param expr: A LogicalNot object.
        :return: A set object containing variables used in expr.
        '''
        return self._visit_default(expr)

    @memoise
    def _visit_equals(self, expr):
        '''
        Internal method for working the variables used in a Equals object.
        :param expr: An Equals object.
        :return: A set object containing variables used in expr.
        '''
        return self._visit_default(expr)

    @memoise
    def _visit_if_then_else(self, expr):
        '''
        Internal method for working the variables used in a IfThenElse object.
        :param expr: An IfThenElse object.
        :return: A set object containing variables used in expr.
        '''
        return self._visit_default(expr)

    @memoise
    def _visit_default(self, expr):
        '''
        Internal method for working out the variables used in an expression.
        :param expr: An Expr object.
        :return: A set object containing variables used in expr.
        '''
        result = set()

        for child in expr.children():
            result = result.union(child.visit(self))

        return result
