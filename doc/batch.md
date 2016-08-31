## Batch Quirks

### Variable evaluation using %var%
Varje if- eller for-clause är som ett helt statement, och alla variabler inuti ett helt statement parsas en enda gång för hela statement. Så om man kör följande kod:
```bat
set x=a
set y=b
if 1==1 (
  set x=c
  set y=d
  set z=%x%, %y%
)
echo x: %x%
echo y: %y%
echo z: %z%
```
Så blir resultatet:
```bat
:: output
x: c
y: d
z: a, b
```
Vill man ha runtime-evaluation är det följande kod som gäller:
```bat
:: notera att följande rad slår igång !-evaluering
setlocal EnableDelayedExpansions

set x=a
set y=b
if 1==1 (
  set x=c
  set y=d
  set z=!x!, !y!
)
echo x: %x%
echo y: %y%
echo z: %z%

:: output
x: c
y: d
z: c, d
```
## Batch Language Constructs (flow control, function definitions, etc)

### for i in 1..5
```bat
for %%i in (1 2 3 4 5) do (
  set var%%i=%%i
  echo var%%i: !var%%i!
)

:: output
var1: 1
var2: 2
var3: 3
var4: 4
var5: 5
```

### for i in ["hej", "yay", "nej"]
```bat
for %%s in (hej yay nej) do (
  echo %%s
)

:: output
hej
yay
nej
```
