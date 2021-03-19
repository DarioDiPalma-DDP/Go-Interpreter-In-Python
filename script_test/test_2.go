var a, b int = 7
var x = 2 + b
var c = 10
var d string = "Ciao"
var e, f, g, h = 1, 2, 3, 4
k := Scanf("Inserisci il tuo nome: ")
Printf(d + " " + k + " " + "Iniziamo")
Printf(e + f + g + h)

Printf("")
Printf("If condition")
if x > 9 {
	Printf("sono uguale a 9")
} else if c == 10 && x != 9 {
	Printf("c è uguale a 12")
} else {
	Printf("Condition not satisfied")
}

Printf("")
Printf("Comparison Operators (b=7,c=10):")
Printf("b+3==c && b != c && b<=c || b>=c && b!=c-2")
Printf(b+3 == c && b != c && b <= c || b >= c && b != c-2)

Printf("")
Printf("!(b+3 == c && b != c && b <= c || b >= c && b != c-2)")
Printf(!(b+3 == c && b != c && b <= c || b >= c && b != c-2))