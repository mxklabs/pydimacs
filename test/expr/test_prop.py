import mxklabs.expr
import pytest

def test_evaluate_not():
  ctx = mxklabs.expr.ExprContext()

  a = ctx.prop.variable(name="a")
  expr = ctx.prop.logical_not(a)

  assert(True == ctx.evaluate(expr, {a : False}))
  assert(False == ctx.evaluate(expr, {a : True}))

def test_evaluate_and():
  ctx = mxklabs.expr.ExprContext()

  a = ctx.prop.variable(name="a")
  b = ctx.prop.variable(name="b")
  expr = ctx.prop.logical_and(a, b)

  assert(False == ctx.evaluate(expr, {a : False, b : False}))
  assert(False == ctx.evaluate(expr, {a : False, b : True}))
  assert(False == ctx.evaluate(expr, {a : True, b : False}))
  assert(True == ctx.evaluate(expr, {a : True, b : True}))

def test_evaluate_or():
  ctx = mxklabs.expr.ExprContext()

  a = ctx.prop.variable(name="a")
  b = ctx.prop.variable(name="b")
  expr = ctx.prop.logical_or(a, b)

  assert(False == ctx.evaluate(expr, {a : False, b : False}))
  assert(True == ctx.evaluate(expr, {a : False, b : True}))
  assert(True == ctx.evaluate(expr, {a : True, b : False}))
  assert(True == ctx.evaluate(expr, {a : True, b : True}))

def test_expr_hash():
  ctx = mxklabs.expr.ExprContext()

  a1 = ctx.prop.variable(name="a")
  b1 = ctx.prop.variable(name="b")
  not1 = ctx.prop.logical_not(a1)
  not2 = ctx.prop.logical_not(a1)
  and1 = ctx.prop.logical_and(a1, b1)
  and2 = ctx.prop.logical_and(a1, b1)
  or1 = ctx.prop.logical_or(a1, b1)
  or2 = ctx.prop.logical_or(a1, b1)

  assert(hash(not1) == hash(not2))
  assert(hash(and1) == hash(and2))
  assert(hash(or1) == hash(or2))

  assert(hash(a1) != hash(b1))
  assert(hash(a1) != hash(not1))
  assert(hash(a1) != hash(and1))
  assert(hash(a1) != hash(or1))
  assert(hash(b1) != hash(not1))
  assert(hash(b1) != hash(and1))
  assert(hash(b1) != hash(or1))
  assert(hash(not1) != hash(and1))
  assert(hash(not1) != hash(or1))
  assert(hash(and1) != hash(or1))

def test_expr_pool():
  ctx = mxklabs.expr.ExprContext()
  a1 = ctx.prop.variable(name="a")
  not1 = ctx.prop.logical_not(a1)
  not2 = ctx.prop.logical_not(a1)
  assert(id(a1) != id(not2))
  assert(id(not1) == id(not2))

def test_expr_transform():
  ctx1 = mxklabs.expr.ExprContext(load_default_expr_class_sets=False)
  ctx1.load_expr_class_set("mxklabs.expr.definitions.prop")

  a = ctx1.prop.variable(name="a")
  b = ctx1.prop.variable(name="b")
  expr = ctx1.prop.logical_or(a, b)

  ctx2 = mxklabs.expr.ExprContext(load_default_expr_class_sets=False)
  ctx2.load_expr_class_set("mxklabs.expr.definitions.cnf")

  #ctx_mapping = ctx1.map_onto(ctx2)

def test_logical_not_simplify():
  ctx = mxklabs.expr.ExprContext()
  a = ctx.prop.variable(name="a")
  not_a = ctx.prop.logical_not(a)
  b = ctx.prop.variable(name="b")
  not_b = ctx.prop.logical_not(b)
  t = ctx.prop.constant(value=True)
  f = ctx.prop.constant(value=False)

  # not(True) => False
  assert(f == ctx.prop.logical_not(t))

  # not(False) => True
  assert(t == ctx.prop.logical_not(f))

  # not(not(a)) => a
  assert(a == ctx.prop.logical_not(ctx.prop.logical_not(a)))

  # not(and(a, not(b))) => or(not(a),b))
  expr1 = ctx.prop.logical_not(ctx.prop.logical_and(a, not_b))
  expr2 = ctx.prop.logical_or(not_a, b)
  assert(expr1 == expr2)

  # not(or(a, not(b))) => and(not(a),b)
  expr1 = ctx.prop.logical_not(ctx.prop.logical_or(a, not_b))
  expr2 = ctx.prop.logical_and(not_a, b)
  assert(expr1 == expr2)


ctx = mxklabs.expr.ExprContext()
a1 = ctx.prop.variable(name="a")
not1 = ctx.prop.logical_not(a1)
not2 = ctx.prop.logical_not(a1)
assert(id(a1) != id(not2))
assert(id(not1) == id(not2))

