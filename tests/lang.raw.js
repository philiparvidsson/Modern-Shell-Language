include('inc/testing.js')

test.name = 'raw built-in test'

raw('goto :eof', 'bat')
test.fail()
