include('inc/testing.js')

// This file contains some challenging syntax constructs.

a=0?1:2
b=  a
    ?
    1
    :
    2

c
    =
    function
(x
)
{
    return x*10
}
assert
    .areEqual ( c(b),
                10,
              'something is not right')

// TODO: Do more weird syntax here.
