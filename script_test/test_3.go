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