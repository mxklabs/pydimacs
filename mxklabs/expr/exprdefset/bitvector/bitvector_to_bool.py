from .exprdef import BitvectorExprDef
from ...exprutils import ExprUtils

class BitvectorToBool(BitvectorExprDef):

  def __init__(self, **kwargs):
    BitvectorExprDef.__init__(self, **kwargs)

  def validate(self, ops, attrs):
    # Expecting one or more operands, all boolean, no attributes.
    ExprUtils.basic_attrs_check(self.id(), {'index':int}, attrs)
    valtype_checker = lambda valtype, index: self._ctx.valtype.is_bitvector(valtype)
    ExprUtils.basic_ops_check(self.id(), 1, 1, valtype_checker, ops)

    if (attrs['index'] < 0 or attrs['index'] >= ops[0].valtype().attrs()['width']):
      raise RuntimeError(f"'{self.id}' invalid value for 'index' (got {attrs['index']}, expected value in [{0, attrs['width']}-1])")

  def valtype(self, ops, attrs, op_valtypes):
    return self._ctx.valtype.bool()

  def evaluate(self, expr, op_values):
    return op_values[expr.index]

  def has_feature(self, featurestr):
    if featurestr == 'simplify':
      return True
    return False

  def simplify(self, expr):
    index = [expr.attrs()['index']]
    print(f"index={expr.attrs()['index']}")
    print(f"ops={expr.ops()}")
    # bitvector_to_bool(e0, ..., e_i=const, .., e_8, index=i) => e_i
    if self._ctx.is_constant(expr.ops()[0]):
      return self._ctx.constant(value=expr.valtype().valtype_def().convert_value_to_booltup(expr.valtype(), expr.value())[index], valtype=self._ctx.valtype.bool())

    # Can't simplify.
    return expr


