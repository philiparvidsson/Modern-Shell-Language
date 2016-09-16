include('assert.js')

raw('goto :eof', 'bat')
assert.isTrue(false, 'raw did not work properly')
