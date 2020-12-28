from ...exprutils import ExprUtils

class InputValidator:

  def __init__(self, ctx):
    self.ctx = ctx

  def logical_not(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_not', 1, 1, self.ctx.valtypes.bool(), ops, [], attrs)

  def logical_and(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_and', 2, None, self.ctx.valtypes.bool(), ops, [], attrs)

  def logical_nand(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_nand', 2, None, self.ctx.valtypes.bool(), ops, [], attrs)

  def logical_or(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_or', 2, None, self.ctx.valtypes.bool(), ops, [], attrs)

  def logical_nor(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_nor', 2, None, self.ctx.valtypes.bool(), ops, [], attrs)

  def logical_xor(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_xor', 2, 2, self.ctx.valtypes.bool(), ops, [], attrs)

  def logical_xnor(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('logical_xnor', 2, 2, self.ctx.valtypes.bool(), ops, [], attrs)

  def implies(self, *ops, **attrs):
    ExprUtils.basicOpsAndAttrsCheck('implies', 2, 2, self.ctx.valtypes.bool(), ops, [], attrs)

class TypeInference:

  def __init__(self, ctx):
    self.ctx = ctx

  def logical_not(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def logical_and(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def logical_nand(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def logical_or(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def logical_nor(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def logical_xor(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def logical_xnor(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

  def implies(self, *ops, **attrs):
    return self.ctx.valtypes.bool()

class ValueInference:

  def __init__(self, ctx):
    self.ctx = ctx

  def logical_not(self, expr, op_value):
    return not op_value

  def logical_and(self, expr, *op_values):
    return all(op_values)

  def logical_nand(self, expr, *op_values):
    return not(all(op_values))

  def logical_or(self, expr, *op_values):
    return any(op_values)

  def logical_nor(self, expr, *op_values):
    return not(any(op_values))

  def logical_xor(self, expr, op_value0, op_value1):
    return op_value0 != op_value1

  def logical_xnor(self, expr,  op_value0, op_value1):
    return op_value0 == op_value1

  def implies(self, expr, op_value0, op_value1):
    return op_value1 or not op_value0