i := 99
for i > 1 {
	Printf(i)
	Printf(" bottles of beer on the wall, ")
	Printf(i)
	Printf(" bottles of beer.")
	Printf("")
	i := i - 1
	Printf("Take one down and pass it around, ")
	Printf(i)
	Printf(" bottles of beer on the wall.")
	Printf("")
}
Printf("No more bottles of beer on the wall, no more bottles of beer.")
Printf("Go to the store and buy some more, 99 bottles of beer on the wall...")

choice := Scanf("Inserire opzione desiderata (1-Saluto 2-Chi sono 3-Esci): ")
if choice == "1" {
	Printf("Ciao!")
} else if choice == "2" {
	Printf("Sono un interprete di Go realizzato da Dario e Marco.")
} else if choice == "3" {
	Printf("Grazie di avermi utilizzato.")
} else {
	Printf("Selezione non corretta.")
}