// this file is just for experimenting with raw statements and creating
// built-ins in smaragd directly

Date = []

Date.now = function() {
    raw('set %~1=ass', 'bat')
    raw('goto :eof'  , 'bat')
}
