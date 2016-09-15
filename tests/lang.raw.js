include('assert.js')

raw('goto :eof', 'bat')
Assert.isTrue(false, 'raw did not work properly')
