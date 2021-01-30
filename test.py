function foo(s):
  n=int(s)
  assert n!=0,"n is zero!"
  return 10/n
def test_foo():
  assert foo(10)==1
