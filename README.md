# Regex
CSCE 355 : See assignment pdf

*ARGS*

--no-op, --empty, --has-epsilon, --has-nonepsilon, --infinite, --starts-with a, --ends-with a,

--reverse, --prefixes, --suffixes, --b-before-a, --drop-one, --strip

-*Some example inputs*-

(a+b)*/

/(a+b)*

(abc)*/(cba)*+/(a+b+c)+(a*+b*+c*)/

(abcd)*(cdab)*

(aa)*+aa*

abc+a*b*c*

a+b+c*+d

(a+b+/*)(c+/*+d)(/*+e+f)

a/*+/*a

aa*+b*b

a+b+c+d

/*+/+/+a

a+bc+abc+d

/*******

(a+b)*/+c+d

a+ab+abc+abcd+/*

(a+b)(c+d)eeeee

abc+bcd+(abcde)*

ab*c

a*b+c

(a+b)c+d(a+(bc)*)

abcd

aaaa

ab*

a*b

(ab)*

a+b*

a*+b

(a+b)*

a+b+c+d+/*

ab+bc+cd+/

(a+b+c)(b+c+d)

(a+b)c+a(b+c)

(cd)*+((a+/*)bc(/*+d))*

(a+/*)(b+/*)(cd)*e

a(a+b+c+d)*

(dc)*+((d+/*)cb(/*+a))*

e(dc)*(b+/*)(a+/*)

(a+b+c+d)*a

/abc

/*abc

abc/

abc/*

(abc)*

bc(abc)*

(abc)*ab

(caaaa+ab)*a+bb

(a+b)(b+c)(c+d)(d+a)

(ab(c+/*))*

(ab+bc(a+d)*)*
