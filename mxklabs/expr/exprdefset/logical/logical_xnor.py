from .exprdef import LogicalExprDef
from ...cnftarget import CnfTarget
from ...exprutils import ExprUtils

class LogicalXnor(LogicalExprDef):

  def __init__(self, **kwargs):
    LogicalExprDef.__init__(self, **kwargs)

  def validate(self, ops, attrs):
    # Expecting two operands, all boolean, no attributes.
    ExprUtils.basic_ops_check(self.id(), 2, 2, self._ctx.valtype.bool(), ops)
    ExprUtils.basic_attrs_check(self.id(), [], attrs)

  def valtype(self, ops, attrs, op_valtypes):
    return self._ctx.valtype.bool()

  def evaluate(self, expr, op_values):
    return any(op_values)

  def has_feature(self, featurestr):
    if featurestr == 'decompose':
      return True
    return False

  def decompose(self, ops, attrs):
    return self._ctx.expr.logical_not(self._ctx.expr.logical_xor(ops))
