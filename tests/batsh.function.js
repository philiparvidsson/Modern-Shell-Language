include('assert.js')

// Function call
function func1(p1, p2) {
    Assert.equal(p1, 'Hello', 'batsh test failed 1')
    Assert.equal(p2, 'World', 'batsh test failed 2')
}
func1("Hello", "World");

// Global and local variables
v1 = "Global V1";
v2 = "Global V2";
v3 = "Global V3";
function func2(p) {
    v1 = "Local " + p;
    Assert.equal(v1, 'Local Var', 'batsh test failed 3')
    Assert.equal(v2, 'Global V2', 'batsh test failed 4')
    v3 = "V3 Modified.";
}
func2("Var");
Assert.equal(v1, 'Global V1', 'batsh test failed 5')
Assert.equal(v3, 'V3 Modified.', 'batsh test failed 6')

// Return value
function func3(num) {
  return num + 41;
}
func3(4);
ret = func3(1);
Assert.equal(ret, 42, 'batsh test failed 7')

// Argument containing space
function g(text) {
  return text;
}
function f(text) {
  return g(text);
}
test = f("Param with space");
Assert.equal(test, 'Param with space', 'batsh test failed 8')
