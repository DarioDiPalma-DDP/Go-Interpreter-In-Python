array := [4]int{1, 2, 3, 4}

Printf("Checking with if: ")
if array[0] == 1 && array[2] < 10 {
	Printf("Condition satisfied")
} else {
	Printf("condition not satisfied")
}

Printf("")
Printf("For Cycle with increment of index")
for x := 0; x < 4; x++ {
	Printf(array[x])
}
Printf("")

var a = 5
var b = 3
Printf("Starting operation code with a=5 and b=3:")
Printf("Sum a+b: ")
Printf(a + b)
Printf("Subtraction a-b: ")
Printf(a - b)
Printf("Multiplication a*b: ")
Printf(a * b)
Printf("Division a/b: ")
Printf(a / b)
Printf("Grouped expression (10+(2*((a+b)*b)+a))/b : ")
Printf((10 + (2*((a+b)*b) + a)) / b)