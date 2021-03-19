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