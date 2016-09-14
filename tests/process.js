include('inc/testing.js')

assert.areEqual(process.argv.length, 2, 'test should have received two args')
assert.areEqual(process.argv[0], 'abc', 'first arg not received')
assert.areEqual(process.argv[1], '123', 'second arg not received')

// FIXME: come up with a better test lol
console.log('testing process.sleep... you should see a delay now')
process.sleep(5)
console.log('sleep test done')
