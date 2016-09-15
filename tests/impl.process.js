include('inc/testing.js')

assert.areEqual(process.argv.length, 2, 'test should have received two args')
assert.areEqual(process.argv[0], 'abc', 'first arg not received')
assert.areEqual(process.argv[1], '123', 'second arg not received')

// FIXME: come up with a better test lol (add support for datetimes)
raw('set /a w1=!time:~6,2! * 100 + !time:~9,2!','bat')
process.sleep(1)
raw('set /a w2=!time:~6,2! * 100 + !time:~9,2!','bat')
raw('set /a d1=w2-w1','bat')
raw('set /a d2=w1-w2','bat')
raw('if !d2! lss !d1! (set d=!d1!) else (set d=!d2!)','bat')
raw('if !d! geq 80 (echo sleep works) else (echo sleep failed)','bat')
