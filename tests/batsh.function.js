include('assert.js')

/**
 * This test is taken from the Batsh test suite.
 *
 * See https://github.com/BYVoid/Batsh for more information.
 */

// Function call
function func1(p1, p2) {
    assert.equal(p1, 'Hello', 'batsh test failed 1')
    assert.equal(p2, 'World', 'batsh test failed 2')
}
func1("Hello", "World");

// Global and local variables
v1 = "Global V1";
v2 = "Global V2";
v3 = "Global V3";
function func2(p) {
    v1 = "Local " + p;
    assert.equal(v1, 'Local Var', 'batsh test failed 3')
    assert.equal(v2, 'Global V2', 'batsh test failed 4')
    v3 = "V3 Modified.";
}
func2("Var");
// mshl has no global keyword like batsh, so all global (or outer-scope) refs
// mutate the value. line below is thus expected to fail
//assert.equal(v1, 'Global V1', 'batsh test failed 5')
assert.equal(v3, 'V3 Modified.', 'batsh test failed 6')

// Return value
function func3(num) {
  // FIXME: unfortunately we have to do a cast by multiplying with one. this
  // should be fixed in some future release.
  return 1*num + 41;
}
func3(4);
ret = func3(1);
assert.equal(ret, 42, 'batsh test failed 7')

// Argument containing space
function g(text) {
  return text;
}
function f(text) {
  return g(text);
}
test = f("Param with space");
assert.equal(test, 'Param with space', 'batsh test failed 8')
