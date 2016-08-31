# Scopes:

```
...
```

**Kommentar:**
		
Vi kan antingen använda måsvingar för scopes (som JavaScript) eller indentering (som Python). Philip föredrar indentering eftersom måsvingar är fula samt indentering tvingar fram en vettig kod. Tvång är bra.

### Kommentarer:

```
# Kommentar.
```

**Kommentar:**
	
Kanske dålig idé med # som ledande tecken för kommentarer med tanke på kommentarer som spänner över flera rader?
Eventuellt kan man köra ## {kommentar med flera rader} ## för att få multiline?


### If-satser:

```
if expr:
    do_something()
elif expr2:
    do_something_2()
else:
    do_something_else()
```

**Kommentar:**
	
Poänglöst med onödiga nyckelord som then. 

### While-loopar:

```
while expr:
    do_something()
```

**Kommentar:**
	
…

### For-loopar:

```
for i in 1..10 step 2
    do_something()
```

**Kommentar:**
	
...

### Funktioner och funktionsanrop:

```
func foo(arg1, arg2):
    x = foo(arg1)
    y = bar(arg2)
    return x+y
```

**Kommentar:**
	
...

### Strängar:

```
s = 'some string'
```

**Kommentar:**
	
Single- eller double-quotes, det är frågan.

### Inbyggda funktioner:

print:
	Skriver ut en text till console. Ex. print "hej"
