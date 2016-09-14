include('inc/testing.js')

test.name = 'raw built-in test'

// FIXME: include messes this up... urgent!
//console.log('this point should not be reached')
raw('goto :eof', 'bat')
test.fail()
