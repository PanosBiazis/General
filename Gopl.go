// package main // go run Gopl.go

// import (
// 	"fmt" // import "fmt" to use fmt.Println() for printing values.
// 	"strings"
// )

// const pi = 3.14
// const s = 9.27

// func main() { // main function, the entry point of a Go program.
// 	fmt.Println("Hello World")                      // Print Hello World.
// 	fmt.Println("Hello World 2")                    /* Print Hello World 2 */
// 	var a int                                       // Declare an integer variable named 'a'.
// 	a = 20                                          // Assign 20 to 'a'.
// 	fmt.Println(a)                                  // Print the value of 'a'.
// 	fmt.Println(a + 10)                             // Print the sum of 'a' and 10.
// 	fmt.Println(pi * 2)                             // Print the value of 'pi' times 2.
// 	var hexvalue int                                // Declare an integer variable named 'hexvalue'.
// 	hexvalue = 0xFF                                 // Declare an integer variable named 'hexvalue'.
// 	fmt.Println(hexvalue)                           // Print the value of 'hexvalue'.
// 	var octvalue int = 034                          // Declare an integer variable named 'octvalue' and assign 034 to it.
// 	fmt.Println(octvalue)                           // Declare an integer variable named 'octvalue' and assign 034 to it.
// 	var binvalue int = 0b1010                       // Declare an integer variable named 'binvalue' and assign 0b1010 to it.
// 	fmt.Println(binvalue)                           // Declare an integer variable named 'binvalue' and assign 0b1010 to it.
// 	var abc = true                                  // Declare a boolean variable named 'abc' and assign true to it.
// 	var abcd bool = false                           // Declare a boolean variable named 'abcd' and assign false to it.
// 	fmt.Println(abc)                                // Print the value of 'abc'.
// 	fmt.Println(abcd)                               // Print the value of 'abcd'.
// 	var mystr string = "Hello"                      // declare a string variable named 'mystr' and assign "Hello" to it.
// 	var mystr2 string = "\t "                       // declare a string variable named 'mystr2' and assign "\t " to it.
// 	mystrSlice := []string{mystr}                   // declare a string slice variable named 'mystrSlice' and assign "Hello" to it.
// 	mystr3 := strings.Join(mystrSlice, mystr2)      // declare a string variable named 'mystr3' and assign "Hello" to it.
// 	var mystr4 string = "World\n"                   //declare a string variable named 'mystr4' and assign "World\n" to it.
// 	var mystr5 string = mystr3 + mystr4             // declare a string variable named 'mystr5' and assign "HelloWorld\n" to it.
// 	fmt.Println(mystr5)                             // Print the value of 'mystr5'.
// 	mystr6, my := fmt.Println(mystr + " " + mystr4) // declare a string variable named 'mystr6' and assign "Hello World\n" to it.
// 	fmt.Println(mystr6, my)                         // Print the value of 'mystr6' and 'my'.
// 	var num uint = 1                                // declare a unsigned integer variable named 'num' and assign 1 to it.
// 	fmt.Println(num)                                // Print the value of 'num'.
// 	var num2 int64 = 2                              // declare an integer variable named 'num2' and assign 2 to it.
// 	fmt.Println(num2)                               // Print the value of 'num2'.
// 	var num3 uint = 3                               // declare an unsigned integer variable named 'num3' and assign 3 to it.
// 	fmt.Println(num3)                               // Print the value of 'num3'.
// 	var num4 int64 = 4                              // declare an integer variable named 'num4' and assign 4 to it.
// 	fmt.Println(num4)                               // Print the value of 'num4'.
// 	var num5 uint64 = 5                             // declare an unsigned integer variable named 'num5' and assign 5 to it.
// 	fmt.Println(num5)                               // Print the value of 'num5'.
// 	var num6 complex128 = 6                         // declare an complex number variable named 'num6' and assign 6 to it.
// 	fmt.Println(num6)                               // Print the value of 'num6'.
// 	var num7 complex64 = 7                          // declare an complex number variable named 'num7' and assign 7 to it.
// 	fmt.Println(num7)                               // Print the value of 'num7'.
// 	var num8 float64 = 8                            // declare a float number variable named 'num8' and assign 8 to it.
// 	fmt.Println(num8)                               // Print the value of 'num8'.
// 	var num9 float32 = 9                            // declare a float number variable named 'num9' and assign 9 to it.
// 	fmt.Println(num9)                               // Print the value of 'num9'.
// 	var num10 float64 = 10                          // declare a float number variable named 'num10' and assign 10 to it.
// 	fmt.Println(num10)                              // Print the value of 'num10'.
// 	var myarray [3]int = [3]int{1, 2, 3}            // declare an array variable named 'myarray' and assign [1, 2, 3] to it.
// 	fmt.Println(myarray)                            // Print the value of 'myarray'.
// 	var check = [3]float32{50.0, 7.0, 8.0}          // declare an array variable named 'check' and assign [50.0, 7.0, 8.0] to it.
// 	fmt.Println(check)                              // Print the value of 'check'.
// 	var myarray2 = [...]int{1, 2, 3}                // declare an array variable named 'myarray2' and assign [1, 2, 3] to it.
// 	fmt.Println(myarray2)                           // Print the value of 'myarray2'.
// 	var myarray3 = [...]int{1, 2, 3, 4, 5, 6, 7}    // declare an array variable named 'myarray3' and assign [1, 2, 3, 4, 5, 6, 7] to it.
// 	fmt.Println(myarray3)                           // Print the value of 'myarray3'.
// 	// Two-dimensional array
// 	var myarray2d [3][3]int = [3][3]int{[3]int{1, 2, 3}, [3]int{4, 5, 6}, [3]int{7, 8, 9}}
// 	fmt.Println(myarray2d)

// 	// Three-dimensional array
// 	var myarray3d [2][2][2]int = [2][2][2]int{[2][2]int{[2]int{1, 2}, [2]int{3, 4}}, [2][2]int{[2]int{5, 6}, [2]int{7, 8}}}
// 	fmt.Println(myarray3d)
// 	//accessing the array elements
// 	checks := check[0]
// 	fmt.Println(checks)

// 	// Multidimensional array
// 	var myarray4 = [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
// 	fmt.Println(myarray4)
// 	var a2 = [2][3]int{{1, 2, 3}, {2, 3, 4}} // declare an array variable named 'a2' and assign [1, 2, 3] to it.
// 	fmt.Println(a2)                          // Print the value of 'a2'.
// 	var sample int = 10                      // declare an integer variable named 'sample' and assign 10 to it.
// 	fmt.Println("%", &sample)                // Print the value of 'sample'.
// 	var mypnt *int = &sample                 // declare a pointer variable named 'mypnt' and assign the address of 'sample' to it.
// 	fmt.Println("%", mypnt)                  // Print the value of 'mypnt'.
// 	mypnt2 := sample                         // declare a pointer variable named 'mypnt2' and assign the value of 'sample' to it.
// 	fmt.Println("%", mypnt2)                 // Print the value of 'mypnt2'.
// 	//structures
// 	//structures
// 	type Person struct {
// 		name string
// 		age  int
// 	}

// 	var p1 Person
// 	p1.name = "John"
// 	p1.age = 30
// 	fmt.Println(p1.name, p1.age)
// 	var Employee struct {
// 		firstname string
// 		lastname  string
// 		fulltime  bool
// 	}
// 	Employee.firstname = "Ross"
// 	Employee.lastname = "Bing"
// 	Employee.fulltime = true
// 	fmt.Printf("The employee %s %s is %t\n", Employee.firstname, Employee.lastname, Employee.fulltime)

// 	var Employee2 struct {
// 		firstname string
// 		lastname  string
// 		salary    int
// 		fulltime  bool
// 	}

// 	Employee2.firstname = "Ross"
// 	Employee2.lastname = "Bing"
// 	Employee2.salary = 1200
// 	Employee2.fulltime = true
// 	fmt.Printf("The employee %s %s is %d and is %t\n", Employee2.firstname, Employee2.lastname, Employee2.salary, Employee2.fulltime)
// 	fmt.Println(Employee2)

// 	/* ross := Employee2{
// 		firstname: "Ross",
// 		lastname:  "Bing",
// 		salary:    1200,
// 		fulltime:  true,
// 	} */

// 	type Employee3 struct {
// 		firstname string
// 		lastname  string
// 		salary    int
// 		fulltime  bool
// 	}

// 	var ross Employee3 = Employee3{
// 		firstname: "Ross",
// 		lastname:  "Bing",
// 		salary:    1200,
// 		fulltime:  true,
// 	}

// 	/*var ross Employee2 = Employee2{
// 		firstname: "Ross",
// 		lastname:  "Bing",
// 		salary:    1200,
// 		fulltime:  true,
// 	} */

// 	fmt.Printf("The employee %s %s is %d and is %t\n", ross.firstname, ross.lastname, ross.salary, ross.fulltime)

// 	type Employee4 struct {
// 		firstname string
// 		lastname  string
// 		salary    int
// 		fulltime  bool
// 	}
// 	Panos := Employee4{"Panos", "Biazis", 1500, false}

// 	fmt.Printf("The employee %s %s is %d and is %t\n", Panos.firstname, Panos.lastname, Panos.salary, Panos.fulltime)

// 	//maps data structure is a type of fast key lookup structure which  helps in indexing to individual elements in a collection of elements
// 	//The map is an unordered collection of key-value pairs.
// 	//the keys and values can be of any type except a channel or function.
// 	//the keys are unique and the values can be duplicated.
// 	//the keys are simple  objects that is used in the retrieval of the values.
// 	//the keys are not ordered.
// 	//the keys are not stored in the map.
// 	//Once the value is stored in the map object,it can be retrieved using its unique key.
// 	var mymap map[string]string = make(map[string]string)
// 	mymap["key1"] = "value1"
// 	mymap["key2"] = "value2"
// 	mymap["key3"] = "value3"
// 	fmt.Println(mymap)

// 	//Accessing elements from the map
// 	fmt.Println(mymap["key1"])
// 	fmt.Println(mymap["key2"])
// 	fmt.Println(mymap["key3"])
// 	fmt.Println(mymap["key4"])

// 	//Delete element from the map
// 	delete(mymap, "key1")
// 	fmt.Println(mymap)

// 	//Iterate over all items in the map
// 	for key, value := range mymap {
// 		fmt.Println(key, value)
// 	}

// 	//Create nested maps (or dictionaries)
// 	var mymap2 map[string]map[string]string = make(map[string]map[string]string)
// 	mymap2["key1"] = make(map[string]string)
// 	mymap2["key1"]["key1.1"] = "value1.1"
// 	mymap2["key1"]["key1.2"] = "value1.2"
// 	mymap2["key2"] = make(map[string]string)
// 	mymap2["key2"]["key2.1"] = "value2.1"
// 	mymap2["key2"]["key2.2"] = "value2.2"
// 	fmt.Println(mymap2)

// 	//Accessing inner items
// 	fmt.Println(mymap2["key1"]["key1.1"])
// 	fmt.Println(mymap2["key1"]["key1.2"])
// 	fmt.Println(mymap2["key2"]["key2.1"])
// 	fmt.Println(mymap2["key2"]["key2.2"])

// 	//Check if a key exists in the map
// 	if _, ok := mymap2["key1"]; ok {
// 		fmt.Println("key1 exists")
// 	} else {
// 		fmt.Println("key1 does not exist")
// 	}

// 	//Check if an item exists in the inner map
// 	if _, ok := mymap2["key1"]["key1.1"]; ok {
// 		fmt.Println("key1.1 exists")
// 	} else {
// 		fmt.Println("key1.1 does not exist")
// 	}

// 	/*//Use nil to create uninitialized maps
// 	var mymap3 map[string]string = nil
// 	mymap3["key1"] = "value1"
// 	mymap3["key2"] = "value2"
// 	mymap3["key3"] = "value3"
// 	fmt.Println(mymap3)

// 	//Delete an entry from the map
// 	delete(mymap3, "key1")
// 	fmt.Println(mymap3)

// 	//Iterate over all entries of the map
// 	for key, value := range mymap3 {
// 		fmt.Println(key, value)
// 	}

// 	//making a map using map literal
// 	mymap4 := map[string]string{
// 		"key1": "value1",
// 		"key2": "value2",
// 		"key3": "value3",
// 	}
// 	fmt.Println(mymap4)
// 	*/
// 	var mmap = make(map[string]int)
// 	mmap["a"] = 2

// 	fmt.Println(mmap)

// 	var mmap2 = map[string]int{
// 		"a": 1,
// 		"b": 2,
// 		"c": 3,
// 	}
// 	fmt.Println(mmap2)
// 	mmap["b2"] = 22

// 	fmt.Println(mmap)

// 	mmap2["d"] = 4
// 	fmt.Println(mmap2)

// 	//Check if a key exists in the map
// 	if _, ok := mmap["b2"]; ok {
// 		fmt.Println("key b2 exists")
// 	} else {
// 		fmt.Println("key b2 does not exist")
// 	}
// 	var z3 int = 20

// 	x2 := z3 + 10
// 	fmt.Println(x2)
// 	s2 := s(int)
// 	y2 := x2 + z3*s2
// 	fmt.Println(y2)

// 	//Decision Making

// 	if z3 > 10 {
// 		fmt.Println("z3 is greater than 10")
// 	} else {
// 		fmt.Println("z3 is less than or equal to 10")
// 	}

// 	/*six conditional statements:

// 	1. if
// 	2. if else
// 	3. the select statement
// 	4. nested if
// 	5. switch
// 	6.if else if else
// 	if var declaration; condition{

// 	} else if var declaration; condition{

// 	}
// 	*/
// 	var value = 2

// 	switch value {

// 	case 1:
// 		fmt.Println("value is 1")

// 	case 2:
// 		fmt.Println("value is 2")

// 	case 3:
// 		fmt.Println("value is 3")

// 	case 4:
// 		fmt.Println("value is 4")

// 	case 5:
// 		{
// 			fmt.Println("value is 5")
// 		}
// 	default:
// 		fmt.Println("value is not 1, 2, or 3")

//		}
//	}
// package main // go run Gopl.go

// import (
// 	"fmt"     // import "fmt" to use fmt.Println() for printing values.
// 	"strings" // import "strings" to use strings.Join() for joining strings.
// )

// const pi = 3.14
// const s = 9.27

// func main() { // main function, the entry point of a Go program.
// 	fmt.Println("Hello World")                      // Print Hello World.
// 	fmt.Println("Hello World 2")                    /* Print Hello World 2 */
// 	var a int                                       // Declare an integer variable named 'a'.
// 	a = 20                                          // Assign 20 to 'a'.
// 	fmt.Println(a)                                  // Print the value of 'a'.
// 	fmt.Println(a + 10)                             // Print the sum of 'a' and 10.
// 	fmt.Println(pi * 2)                             // Print the value of 'pi' times 2.
// 	var hexvalue int                                // Declare an integer variable named 'hexvalue'.
// 	hexvalue = 0xFF                                 // Assign 0xFF to 'hexvalue'.
// 	fmt.Println(hexvalue)                           // Print the value of 'hexvalue'.
// 	var octvalue int = 034                          // Declare an integer variable named 'octvalue' and assign 034 to it.
// 	fmt.Println(octvalue)                           // Print the value of 'octvalue'.
// 	var binvalue int = 0b1010                       // Declare an integer variable named 'binvalue' and assign 0b1010 to it.
// 	fmt.Println(binvalue)                           // Print the value of 'binvalue'.
// 	var abc = true                                  // Declare a boolean variable named 'abc' and assign true to it.
// 	var abcd bool = false                           // Declare a boolean variable named 'abcd' and assign false to it.
// 	fmt.Println(abc)                                // Print the value of 'abc'.
// 	fmt.Println(abcd)                               // Print the value of 'abcd'.
// 	var mystr string = "Hello"                      // Declare a string variable named 'mystr' and assign "Hello" to it.
// 	var mystr2 string = "\t "                       // Declare a string variable named 'mystr2' and assign "\t " to it.
// 	mystrSlice := []string{mystr}                   // Declare a string slice variable named 'mystrSlice' and assign "Hello" to it.
// 	mystr3 := strings.Join(mystrSlice, mystr2)      // Join mystrSlice with mystr2 and assign the result to 'mystr3'.
// 	var mystr4 string = "World\n"                   // Declare a string variable named 'mystr4' and assign "World\n" to it.
// 	var mystr5 string = mystr3 + mystr4             // Concatenate 'mystr3' and 'mystr4' and assign the result to 'mystr5'.
// 	fmt.Println(mystr5)                             // Print the value of 'mystr5'.
// 	mystr6, my := fmt.Println(mystr + " " + mystr4) // Print 'mystr' and 'mystr4', and assign the number of bytes written and any error to 'mystr6' and 'my'.
// 	fmt.Println(mystr6, my)                         // Print the values of 'mystr6' and 'my'.
// 	var num uint = 1                                // Declare an unsigned integer variable named 'num' and assign 1 to it.
// 	fmt.Println(num)                                // Print the value of 'num'.
// 	var num2 int64 = 2                              // Declare an integer variable named 'num2' and assign 2 to it.
// 	fmt.Println(num2)                               // Print the value of 'num2'.
// 	var num3 uint = 3                               // Declare an unsigned integer variable named 'num3' and assign 3 to it.
// 	fmt.Println(num3)                               // Print the value of 'num3'.
// 	var num4 int64 = 4                              // Declare an integer variable named 'num4' and assign 4 to it.
// 	fmt.Println(num4)                               // Print the value of 'num4'.
// 	var num5 uint64 = 5                             // Declare an unsigned integer variable named 'num5' and assign 5 to it.
// 	fmt.Println(num5)                               // Print the value of 'num5'.
// 	var num6 complex128 = 6                         // Declare a complex number variable named 'num6' and assign 6 to it.
// 	fmt.Println(num6)                               // Print the value of 'num6'.
// 	var num7 complex64 = 7                          // Declare a complex number variable named 'num7' and assign 7 to it.
// 	fmt.Println(num7)                               // Print the value of 'num7'.
// 	var num8 float64 = 8                            // Declare a float number variable named 'num8' and assign 8 to it.
// 	fmt.Println(num8)                               // Print the value of 'num8'.
// 	var num9 float32 = 9                            // Declare a float number variable named 'num9' and assign 9 to it.
// 	fmt.Println(num9)                               // Print the value of 'num9'.
// 	var num10 float64 = 10                          // Declare a float number variable named 'num10' and assign 10 to it.
// 	fmt.Println(num10)                              // Print the value of 'num10'.
// 	var myarray [3]int = [3]int{1, 2, 3}            // Declare an array variable named 'myarray' and assign [1, 2, 3] to it.
// 	fmt.Println(myarray)                            // Print the value of 'myarray'.
// 	var check = [3]float32{50.0, 7.0, 8.0}          // Declare an array variable named 'check' and assign [50.0, 7.0, 8.0] to it.
// 	fmt.Println(check)                              // Print the value of 'check'.
// 	var myarray2 = [...]int{1, 2, 3}                // Declare an array variable named 'myarray2' and assign [1, 2, 3] to it.
// 	fmt.Println(myarray2)                           // Print the value of 'myarray2'.
// 	var myarray3 = [...]int{1, 2, 3, 4, 5, 6, 7}    // Declare an array variable named 'myarray3' and assign [1, 2, 3, 4, 5, 6, 7] to it.
// 	fmt.Println(myarray3)                           // Print the value of 'myarray3'.
// 	// Two-dimensional array
// 	var myarray2d [3][3]int = [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
// 	fmt.Println(myarray2d)

// 	// Three-dimensional array
// 	var myarray3d [2][2][2]int = [2][2][2]int{{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}}
// 	fmt.Println(myarray3d)
// 	// Accessing the array elements
// 	checks := check[0]
// 	fmt.Println(checks)

// 	// Multidimensional array
// 	var myarray4 = [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
// 	fmt.Println(myarray4)
// 	var a2 = [2][3]int{{1, 2, 3}, {2, 3, 4}} // Declare an array variable named 'a2' and assign [1, 2, 3] to it.
// 	fmt.Println(a2)                          // Print the value of 'a2'.
// 	var sample int = 10                      // Declare an integer variable named 'sample' and assign 10 to it.
// 	fmt.Println("%", &sample)                // Print the value of 'sample'.
// 	var mypnt *int = &sample                 // Declare a pointer variable named 'mypnt' and assign the address of 'sample' to it.
// 	fmt.Println("%", mypnt)                  // Print the value of 'mypnt'.
// 	mypnt2 := sample                         // Assign the value of 'sample' to 'mypnt2'.
// 	fmt.Println("%", mypnt2)                 // Print the value of 'mypnt2'.
// 	// Structures
// 	type Person struct {
// 		name string
// 		age  int
// 	}

// 	var p1 Person
// 	p1.name = "John"
// 	p1.age = 30
// 	fmt.Println(p1.name, p1.age)
// 	var Employee struct {
// 		firstname string
// 		lastname  string
// 		fulltime  bool
// 	}
// 	Employee.firstname = "Ross"
// 	Employee.lastname = "Bing"
// 	Employee.fulltime = true
// 	fmt.Printf("The employee %s %s is %t\n", Employee.firstname, Employee.lastname, Employee.fulltime)

// 	var Employee2 struct {
// 		firstname string
// 		lastname  string
// 		salary    int
// 		fulltime  bool
// 	}

// 	Employee2.firstname = "Ross"
// 	Employee2.lastname = "Bing"
// 	Employee2.salary = 1200
// 	Employee2.fulltime = true
// 	fmt.Printf("The employee %s %s is %d and is %t\n", Employee2.firstname, Employee2.lastname, Employee2.salary, Employee2.fulltime)
// 	fmt.Println(Employee2)

// 	type Employee3 struct {
// 		firstname string
// 		lastname  string
// 		salary    int
// 		fulltime  bool
// 	}

// 	var ross Employee3 = Employee3{
// 		firstname: "Ross",
// 		lastname:  "Bing",
// 		salary:    1200,
// 		fulltime:  true,
// 	}

// 	fmt.Printf("The employee %s %s is %d and is %t\n", ross.firstname, ross.lastname, ross.salary, ross.fulltime)

// 	type Employee4 struct {
// 		firstname string
// 		lastname  string
// 		salary    int
// 		fulltime  bool
// 	}
// 	Panos := Employee4{"Panos", "Biazis", 1500, false}

// 	fmt.Printf("The employee %s %s is %d and is %t\n", Panos.firstname, Panos.lastname, Panos.salary, Panos.fulltime)

// 	// Maps data structure
// 	var mymap map[string]string = make(map[string]string)
// 	mymap["key1"] = "value1"
// 	mymap["key2"] = "value2"
// 	mymap["key3"] = "value3"
// 	fmt.Println(mymap)

// 	// Accessing elements from the map
// 	fmt.Println(mymap["key1"])
// 	fmt.Println(mymap["key2"])
// 	fmt.Println(mymap["key3"])
// 	fmt.Println(mymap["key4"])

// 	// Delete element from the map
// 	delete(mymap, "key1")
// 	fmt.Println(mymap)

// 	// Iterate over all items in the map
// 	for key, value := range mymap {
// 		fmt.Println(key, value)
// 	}

// 	// Create nested maps (or dictionaries)
// 	var mymap2 map[string]map[string]string = make(map[string]map[string]string)
// 	mymap2["key1"] = make(map[string]string)
// 	mymap2["key1"]["key1.1"] = "value1.1"
// 	mymap2["key1"]["key1.2"] = "value1.2"
// 	mymap2["key2"] = make(map[string]string)
// 	mymap2["key2"]["key2.1"] = "value2.1"
// 	mymap2["key2"]["key2.2"] = "value2.2"
// 	fmt.Println(mymap2)

// 	// Accessing inner items
// 	fmt.Println(mymap2["key1"]["key1.1"])
// 	fmt.Println(mymap2["key1"]["key1.2"])
// 	fmt.Println(mymap2["key2"]["key2.1"])
// 	fmt.Println(mymap2["key2"]["key2.2"])

// 	// Check if a key exists in the map
// 	if _, ok := mymap2["key1"]; ok {
// 		fmt.Println("key1 exists")
// 	} else {
// 		fmt.Println("key1 does not exist")
// 	}

// 	// Check if an item exists in the inner map
// 	if _, ok := mymap2["key1"]["key1.1"]; ok {
// 		fmt.Println("key1.1 exists")
// 	} else {
// 		fmt.Println("key1.1 does not exist")
// 	}

// 	var mmap = make(map[string]int)
// 	mmap["a"] = 2

// 	fmt.Println(mmap)

// 	var mmap2 = map[string]int{
// 		"a": 1,
// 		"b": 2,
// 		"c": 3,
// 	}
// 	fmt.Println(mmap2)
// 	mmap["b2"] = 22

// 	fmt.Println(mmap)

// 	mmap2["d"] = 4
// 	fmt.Println(mmap2)

// 	// Check if a key exists in the map
// 	if _, ok := mmap["b2"]; ok {
// 		fmt.Println("key b2 exists")
// 	} else {
// 		fmt.Println("key b2 does not exist")
// 	}
// 	var z3 int = 20

// 	x2 := z3 + 10
// 	fmt.Println(x2)
// 	s2 := int(s) // Casting the float constant 's' to an int.
// 	y2 := x2 + z3*s2
// 	fmt.Println(y2)

// 	// Decision Making

// 	if z3 > 10 {
// 		fmt.Println("z3 is greater than 10")
// 	} else {
// 		fmt.Println("z3 is less than or equal to 10")
// 	}

// 	var value = 2

// 	switch value {

// 	case 1:
// 		fmt.Println("value is 1")

// 	case 2:
// 		fmt.Println("value is 2")

// 	case 3:
// 		fmt.Println("value is 3")

// 	case 4:
// 		fmt.Println("value is 4")

// 	case 5:
// 		fmt.Println("value is 5")

// 	default:
// 		fmt.Println("value is not 1, 2, or 3")

// 	}
// }

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

// func swap(x, y string) string {
// 	return x, y
// }

func hello() {
	fmt.Println("Hello Goroutine")
}

const pi = 3.14

//const s = 9.27

func main() {
	fmt.Println("Start")
	var s float64 = 3 * pi
	fmt.Println("Hello World")
	fmt.Println("Hello World 2")

	var a int
	a = 20
	fmt.Println(a)
	fmt.Println(a + 10)
	fmt.Println(pi * 2)

	var hexvalue int
	hexvalue = 0xFF
	fmt.Println(hexvalue)

	var octvalue int = 034
	fmt.Println(octvalue)

	var binvalue int = 0b1010
	fmt.Println(binvalue)

	var abc = true
	var abcd bool = false
	fmt.Println(abc)
	fmt.Println(abcd)

	var mystr string = "Hello"
	var mystr2 string = "\t "
	mystrSlice := []string{mystr}
	mystr3 := strings.Join(mystrSlice, mystr2)
	var mystr4 string = "World\n"
	var mystr5 string = mystr3 + mystr4
	fmt.Println(mystr5)

	mystr6, my := fmt.Println(mystr + " " + mystr4)
	fmt.Println(mystr6, my)

	var num uint = 1
	fmt.Println(num)

	var num2 int64 = 2
	fmt.Println(num2)

	var num3 uint = 3
	fmt.Println(num3)

	var num4 int64 = 4
	fmt.Println(num4)

	var num5 uint64 = 5
	fmt.Println(num5)

	var num6 complex128 = 6
	fmt.Println(num6)

	var num7 complex64 = 7
	fmt.Println(num7)

	var num8 float64 = 8
	fmt.Println(num8)

	var num9 float32 = 9
	fmt.Println(num9)

	var num10 float64 = 10
	fmt.Println(num10)

	var myarray [3]int = [3]int{1, 2, 3}
	fmt.Println(myarray)

	var check = [3]float32{50.0, 7.0, 8.0}
	fmt.Println(check)

	var myarray2 = [...]int{1, 2, 3}
	fmt.Println(myarray2)

	var myarray3 = [...]int{1, 2, 3, 4, 5, 6, 7}
	fmt.Println(myarray3)

	var myarray2d [3][3]int = [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(myarray2d)

	var myarray3d [2][2][2]int = [2][2][2]int{{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}}
	fmt.Println(myarray3d)

	checks := check[0]
	fmt.Println(checks)

	var myarray4 = [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(myarray4)

	var a2 = [2][3]int{{1, 2, 3}, {2, 3, 4}}
	fmt.Println(a2)

	var sample int = 10
	fmt.Println("%", &sample)

	var mypnt *int = &sample
	fmt.Println("%", mypnt)

	mypnt2 := sample
	fmt.Println("%", mypnt2)

	type Person struct {
		name string
		age  int
	}

	var p1 Person
	p1.name = "John"
	p1.age = 30
	fmt.Println(p1.name, p1.age)

	var Employee struct {
		firstname string
		lastname  string
		fulltime  bool
	}
	Employee.firstname = "Ross"
	Employee.lastname = "Bing"
	Employee.fulltime = true
	fmt.Printf("The employee %s %s is %t\n", Employee.firstname, Employee.lastname, Employee.fulltime)

	var Employee2 struct {
		firstname string
		lastname  string
		salary    int
		fulltime  bool
	}
	Employee2.firstname = "Ross"
	Employee2.lastname = "Bing"
	Employee2.salary = 1200
	Employee2.fulltime = true
	fmt.Printf("The employee %s %s is %d and is %t\n", Employee2.firstname, Employee2.lastname, Employee2.salary, Employee2.fulltime)
	fmt.Println(Employee2)

	type Employee3 struct {
		firstname string
		lastname  string
		salary    int
		fulltime  bool
	}

	var ross Employee3 = Employee3{
		firstname: "Ross",
		lastname:  "Bing",
		salary:    1200,
		fulltime:  true,
	}
	fmt.Printf("The employee %s %s is %d and is %t\n", ross.firstname, ross.lastname, ross.salary, ross.fulltime)

	type Employee4 struct {
		firstname string
		lastname  string
		salary    int
		fulltime  bool
	}
	Panos := Employee4{"Panos", "Biazis", 1500, false}
	fmt.Printf("The employee %s %s is %d and is %t\n", Panos.firstname, Panos.lastname, Panos.salary, Panos.fulltime)

	var mymap map[string]string = make(map[string]string)
	mymap["key1"] = "value1"
	mymap["key2"] = "value2"
	mymap["key3"] = "value3"
	fmt.Println(mymap)

	fmt.Println(mymap["key1"])
	fmt.Println(mymap["key2"])
	fmt.Println(mymap["key3"])
	fmt.Println(mymap["key4"])

	delete(mymap, "key1")
	fmt.Println(mymap)

	for key, value := range mymap {
		fmt.Println(key, value)
	}

	var mymap2 map[string]map[string]string = make(map[string]map[string]string)
	mymap2["key1"] = make(map[string]string)
	mymap2["key1"]["key1.1"] = "value1.1"
	mymap2["key1"]["key1.2"] = "value1.2"
	mymap2["key2"] = make(map[string]string)
	mymap2["key2"]["key2.1"] = "value2.1"
	mymap2["key2"]["key2.2"] = "value2.2"
	fmt.Println(mymap2)

	fmt.Println(mymap2["key1"]["key1.1"])
	fmt.Println(mymap2["key1"]["key1.2"])
	fmt.Println(mymap2["key2"]["key2.1"])
	fmt.Println(mymap2["key2"]["key2.2"])

	if _, ok := mymap2["key1"]; ok {
		fmt.Println("key1 exists")
	} else {
		fmt.Println("key1 does not exist")
	}

	if _, ok := mymap2["key1"]["key1.1"]; ok {
		fmt.Println("key1.1 exists")
	} else {
		fmt.Println("key1.1 does not exist")
	}

	var mmap = make(map[string]int)
	mmap["a"] = 2
	fmt.Println(mmap)

	var mmap2 = map[string]int{
		"a": 1,
		"b": 2,
		"c": 3,
	}
	fmt.Println(mmap2)

	mmap["b2"] = 22
	fmt.Println(mmap)

	mmap2["d"] = 4
	fmt.Println(mmap2)

	if _, ok := mmap["b2"]; ok {
		fmt.Println("key b2 exists")
	} else {
		fmt.Println("key b2 does not exist")
	}

	var z3 int = 20
	x2 := z3 + 10
	fmt.Println(x2)

	s2 := int(s) // Corrected type conversion
	y2 := x2 + z3*s2
	fmt.Println(y2)

	if z3 > 10 {
		fmt.Println("z3 is greater than 10")
	} else {
		fmt.Println("z3 is less than or equal to 10")
	}

	var value = 2
	switch value {
	case 1:
		fmt.Println("value is 1")
	case 2:
		fmt.Println("value is 2")
	case 3:
		fmt.Println("value is 3")
	case 4:
		fmt.Println("value is 4")
	case 5:
		fmt.Println("value is 5")
	default:
		fmt.Println("value is not 1, 2, 3, 4, or 5")
	}

	//Loops

	for i := 0; i < 5; i++ { //For loops
		fmt.Println(i)
	}

	//Nested Loops
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			fmt.Println(i, j)
		}
	}

	sum := 0
	for i := 0; i < 5; i++ {
		sum += i
	}
	fmt.Println(sum)

	//Infinite Loop
	/*for {
		fmt.Println("Hello World")
	}
	*/

	// for true {
	// 	fmt.Println("Hello World")
	// }
	fmt.Println(1)
	goto End
	fmt.Println(2)
End:
	fmt.Println(3)

	strings := []string{"hello", "all", "of", "you"}
	for index, value := range strings {
		fmt.Println(index, value)
	}
	for value := range strings {
		fmt.Println(value)
	}

	for _, value := range strings {
		fmt.Println(value)
	}

	for index, _ := range strings {
		fmt.Println(index)
	}

	for index := 0; index < len(strings); index++ {
		fmt.Println(strings[index])
	}

	/*
																													Functions are a significant aspect of a Golang program.
																												Want to develop an application with multiple unique
																												functionalities, use ‘functions’ effectively

																												So, what do functions refer to?

																												A function represents a block of code which takes few
																												inputs, does some processing over them and provide some
																												outputs.

																												Basically, you can consider a function as an independent
																												section of code which usually performs a single or correlated
																												functions.

																													Remember, functions are also commonly known as
																												procedures or subroutines. You can easily divide your Golang
																												code into unique separate functions.

																												Functions are allowed to take nil, one or more input
																												parameters! Similarly, the functions can be intended to
																												provide nil, one more output.

																												A well-designed function is a group of statements which
																												together perform a specific task

																												In Golang, there will be at least one function which is the
																												main() function.


																												How can you divide the code to form different functions? Are
																												there any specific ways to perform the division?

																												There are no fixed rules to divide your Golang code. Logically
																												it is best to divide the code in such a way that every function
																												performs some specific task.

																												When you define a function efficiently, it often helps you
																												track your code easily, helps you find errors and rectify them
																												easily.


																												What are the major purposes of having functions in your
																										Golang code?

																										The major purpose of dividing your Golang code into
																										functions is to have some small reusable pieces of code.

																										Functions, to a great extent, would help in reducing the
																										redundant lines of code

																										In case, you need to perform the same functionality again at
																										a different place in your Golang code, all you need is to just
																										call the function again.



																										There are two terms associated with writing functions in
																								Golang:

																								¢ function declaration

																								¢ function definition

																								The function declaration is the first step to write a function.

																								By declaring a function, you tell the compiler about function
																								name, parameters and the return type!

																								What do parameters refer to?

																								Parameters are the values that are provided as inputs to the
																								functions. These input values get used within the function.



																								What is a ‘return type’?. Remember, A function can either
																						return some value or need not return anything!

																						You need to declare the return type of the function when you
																						declare the function. The return type would tell the compiler
																						the type of the data that would be returned.

																						For example, if a function is to return a value belonging to
																						‘int’ type, then you will have to mention the return type when
																						you declare the function.




																							The second step is to define your function once you
																						successfully declared the function with an appropriate
																						name, parameters and the return type.

																						Before you start using functions, make sure you know the
																						purpose of the function, the input parameters required along
																						with the expected output.

																						With these details, you can declare the function perfectly
																						telling the compiler all the details pertaining to the existence
																						of a function.




																						In Golang, you should define a function using the ‘func’
																				keyword.

																				Can we have more than one input parameters to the
																				function? Of course yes, you can have any number of input
																				parameters separated by commas.

																				The input parameters must be provided along with their
																				data type to the function as an argument.

																				In addition, Golang provides some built-in functions which
																				you can call. One of the commonly used built-in functions is
																				len()





																				What does the len() function return?

																		This built-in functions takes the arguments belonging to
																		different data types and returns the length of the type.

																		For example, if an array is passed to the len() function, it
																		would return the length of the array.

																		Once the function is declared, you need to provide a function
																		definition which comprises of the function header and the
																		function body.

																		Till now, you must have noticed only one function in the Go
																		language. It is the func main(){}.

																		This is the function that marks the mandatory main function
																		of your Golang program.






																		The general syntactical form of a function Golang is as
																follows:

																func function_name ( [list of parameters] ) [return_types]

																{
																The body of the function

																i

																Here, the word ‘func’ is the Golang keyword that is used in
																declaring your functions. This keyword starts the function's
																declaration.

																The next you notice in the syntax is the function_name.

																This is the actual function name. Remember, the function
																name along with the parameter list is referred to as function
																signature.



																func function_name ( [list of parameters] ) [return_types]

														{
														The body of the function

														}

														What happens to the parameters of the function when the
														function gets invoked?

														Think a parameter like a placeholder. When you invoke a
														function, a value gets passed to the parameter.

														The value that gets passed to the parameters provided in
														the function definition is known as the actual parameters. It
														is also Known as arguments.

														Remember, function parameters are totally optional!

														The order, number and type of parameters do matter a lot
														when you pass the values to the defined parameters.




														func function_name ( [list of parameters] ) [return_types]

												{
												The body of the function

												What are ‘return types’?

												As we know a specific function may return a single value, a
												list of values or may not return any value.

												Generally, return_types in the function definition is the data
												types of the values that get returned after the successful
												execution of the function.

												When a function is intended not to return any value, you
												need not provide any return-type to your function definition.


												func function_name ( [list of parameters] ) [return_types]

										{
										The body of the function

										}

										Once you successfully declared and defined the Golang
										function, you can create the body of the function.

										The function body is basically a set of statements that are
										intended to define what that specific function is to do in your
										Golang program.

										The body of the function can have any loop statement,
										control statements or nested conditional statements for
										execution.



										Do you have multiple consecutive parameters belonging to
								the same data type? You have a simpler way to handle this
								case.

								In Golang, It is enough to mention the data type only once for
								the last parameter belonging to that data type.

								Consider the code snippet below:
								func avg (x, y int) int {}

								The above definition of the parameters is allowed in Golang.

								Here, x and y are the two parameters belonging to the same
								data type ‘int.

								Instead of mentioning it for each parameter, you can
								mention the data type of the last parameter.


								Once you have successfully finished with the function
						declaration, definition and the body of the function is
						written, the function is all set to be called.

						Whenever you need to use the function defined, you need to
						call the function!

						The function can be called from any part of your Golang
						program.

						When the control reaches a ‘function call’ statement, the
						control gets instantly transferred to the called function.




						The called function then perform the task that it has been
				defined with.

				When the return statement of the function gets executed
				the control then returns back to the place from where the
				function was called.

				How to call a function that has been defined? And how do
				you store the returned value you get from the execution of
				the function.

				Sometimes, your function can just perform some tasks like
				printing values or statements. In that case, your function will
				not return any value.



				Just pass the required parameters in the same order along
		with the function name.

		Make sure the order of the parameters and the function
		name used in the function call statement matches with the
		function signature.

		If the intended function returns the value, you can store it.
		Never mess up with the order of parameters.

		If the order of the parameter values doesn’t match with the
		order or the data type of the parameters mentioned in the
		function signature, you will encounter a compile-time error.




	*/

	// a, b := swap("Mahesh", "Kumar")
	// fmt.Println(a, b)

	/*

											There is no fixed rule that Golang can return only value. You
										can have multiple values returned from the function.

										Consider the below code snippet:

										import “fmt”

										func swap(x, y string) (string, string) {
										i100 ldap

										i

										func main() {
										a, b := swap("Mahesh", "Kumar")
										fmt.PrintIn(a, b)

										i

										Here, ‘swap’ is the function name with two input parameters
										‘x’ and ‘y’ belonging to the string data type.

										The function ‘swap’ is intended to return “2” values, both
										belonging to the string data type.

										The purpose of the ‘swap’ function is to swap the sent string
										values and return them to the function call statement.




										Consider the below code snippet:

								import “fmt”

								func swap(x, y string) (string, string) {
								return y, X

								i

								func main() {
								a, b := swap("Mahesh", "Kumar")
								fmt.PrintIn(a, b)

								i

								In the main function, the ‘swap’ function is called. The first
								and the second parameter sent to the ‘swap’ function is
								‘Mahesh’ and ‘Kumar’ respectively.


								Consider the below code snippet:

						import “fmt”

						func swap(x, y string) (string, string) {
						return y, X

						i

						func main() {
						a, b := swap("Mahesh", "Kumar")
						fmt.PrintIn(a, b)

						i

						When the control reaches the function, the data type of
						the parameters sent is checked with the data type of the
						parameters that are sent.



						Consider the below code snippet again:

				import “fmt”

				func swap(x, y string) (string, string) {
				return y, X

				i

				func main() {
				a, b := swap("Mahesh", "Kumar")
				fmt.PrintIn(a, b)

				i

				The returned starings ‘Kumar’ and ‘Mahesh’ in order gets
				stored in the variables ‘a’ and ‘b’ respectively.

				You will notice a printIn statement [fmt.Println(a, b) ]. Here
				the print statement would print the values of a and b in that
				order.

				The final output of the above Golang program will be Kumar
				Mahesh. You must be clear of how the function is called and
				how the values are returned.


				When you want to write your own application in the Go
		language, you need to know the significance of the ‘variadic
		functions’.

		Just as the name indicated, variadic functions are those
		functions which have a varying number of arguments.

		In simple words, users can pass zero or more arguments to
		the variadic function.

		There is no restriction of the number of arguments to be
		passed to the ‘variadic functions’

	*/

	value1, value2 := someFunctionThatReturnsTwoValues()
	fmt.Println(value1, value2)

	// Example fix for swap function
	swap("Mahesh", "Kumar")

	/*

																									‘fmt.Printf’ is the best example of the variadic function in
																								Golang.

																								The ‘fmt.Printf function needs one fixed argument right
																								at the beginning. After that, it can accept any number of
																								arguments.

																								Variadic functions become extremely useful when you are
																								not sure of the incoming number of parameters.

																								Once, you use make the last parameter of your function
																								variadic, you can add any number of parameters to that
																								function



																								When should a variadic function be used?

																						Use a variadic function when you want to pass a ‘slice’ in a
																						Golang function. Whenever you want to pass a ‘slice’, the
																						variadic function is the best choice.

																						You can also use a variadic function when you are not aware
																						of the number of parameters required. You will be facing
																						such scenarios while building a real-time application.

																						Using the variadic functions will increase the readability and
																						clarity of your Golang program.


																						You need to remember some points while you use the
																				variadic functions in your Golang program.

																				Remember when you declare your variadic function, the
																				data type of the last parameter must be preceded by an
																				ellipsis.

																				The ellipsis is denoted by (...). What does ellipsis mean?

																				Ellipsis denotes that the variadic function can be called at
																				any number of parameters belonging to the mentioned data

																				type.


																				The syntax of the variadic function is as follows:

																		func function_name (parameter1, parameterz2... type) type{
																		// code...

																		}

																		Here, the ellipsis symbol (...) indicate that any number of
																		parameters can be sent to the variadic function.

																		Remember that when no argument is passed in the variadic
																		function. The slice inside the function would be ‘nil’. Don’t
																		forget this.

																		Keep in mind that you can also multiple slices to the variadic
																		functions. Variadic functions are widely used in use cases
																		that require string formatting.

																		Consider the below code snippet:

																unc world (a int, b... int)

																{
																}

																Here, the parameter ‘b’ is said to be ‘variadic’. The variable
																‘b’ is prefixed by an ellipsis (...), meaning that it any number
																of arguments can be accepted.

																You can call this function using the syntax, world (10,20)
																or world (11,12,13,14) . This functional call to the variadic
																function is totally acceptable.

																Keep in mind, you can call the world() function without
																parameters. hello(2), in this function call, there are zero
																arguments for the variable ‘b’ This is acceptable.

																Consider the below code snippet:
														func world (b...int, a int) {}

														Here, in the above function, you can never pass arguments
														to the variable ‘a’. Why?

														Because whatever argument you try to pass will be
														assigned only to the variable 'b’ as it is variadic.

														Now, you will understand why the variadic parameters can
														be present only in the last during the function definition.

														If this rule is not followed, you will view the ‘ syntax error:
														cannot use ... with the non-final parameter” error

														Be smart while you use the variadic function by following
														the above-stated rule to avoid the errors.


														Let’s discuss recursion. You must have across the term in
												probably every coding language you know!

												Recursion is the method of repeating a specific function in a
												self-similar manner.

												If your program calls a function inside the very same
												function, it is termed as the recursive function call.

												Yes, Golang also supports Recursion. You can design
												functions that would call itself.




												In recursive programming, the answer to the base condition
										is provided.

										The solution of the entire problem is expressed in terms of
										smaller problems and their solution is determined.

										A problem can be expressed in terms of one or more than
										one smaller problem.

										Remember you can have or more base conditions to stop the
										recursion flow!

										For example, to calculate the factorial of a number, the base
										case would be n=0. In that case, 1 gets returned


										Have you heard about stack overflow? It is the condition,
								where the program crashes or freezes.

								This condition occurs due to the infinite loop in the program
								or sometimes even when the variables are too large for the
								call stack size.

								If the base condition is never reached or not defined at all,
								then the stack overflow problem occurs.

								The memory gets exhausts and you need to provide a base
								condition to stop the recursion flow.


								Recursive programming helps in writing clear and precise
						code. Some problems can be solved inherently like the Tower
						of Hanoi!

						Though both the iterative and recursive approach has the
						same problem-solving power, the recursive program is
						chosen when you want a more precise and clear code,

						Through recursive programs has greater space and time
						requirements, this approach is used while building a
						large-scale application

				You have to be very careful to define the exit condition
				correctly. Else, there is a high probability that it can result in
				an infinite loop.

				With recursion, you can reduce unnecessary function calls.
				While designing large-scale applications, you can reduce
				the redundant code lines.

				Infinite recursion can be avoided with the help of if-else
				statements.



				Consider the below code snippet:

		func factorial(i int)int {
		ifi<=1){
		auto Wil

		H

		return i * factorial(i - 1)
		}
		func main() {

		variint=15

		fmt.Printf("Factorial of %d is %d", i, factorial(i))
		}

		Here, factorial is the recursive function. The logic is
		implemented within the factorial function.

		The function ‘factorial’ gets called from the main function
		as factorial (i). Here a number is sent as a parameter to the
		“factorial’ function

		In the factorial function, you can pass any number of
		parameters and the condition gets checked for every count.

	*/

	var i int = 15

	fmt.Printf("Factirial of %d is %d\n", i, factorial(i))

	/*
							What are Goroutines? Why do we need them? What is so
						special about them? Let's find out the answers to these
						questions.

						Before discussing the Goroutines topics, let’s see what
						concurrency means?

						Concurrency is the ability to manage multiple things at once.
						Remember, it doesn't mean that all things are to be done at
						the same time.

						In all large-scale applications, concurrency is a must in order
						to achieve good efficiency.


				Concurrency is a very vital part of the Go programming
				language. You can achieve concurrency using the concept of
				Goroutines and channels.

				Goroutines is an easy way of performing the tasks
				concurrently in the Go language.

				Goroutines allows you to create and run multiple functions in
				a concurrent manner.

				Compared to the thread concepts in other programming
				languages, Goroutines stand way ahead when it comes to
				achieving excellent concurrency


		Goroutines have several advantages in comparison with the
		threads! Foremost, they are extremely cheap in comparison
		to the threads.

		In Goroutines, the stack can grow and shrink dynamically
		based on the requirements of the application to be built.

		This is a huge factor since the stack size is fixed in the case
		of threads.

		So, Goroutines are very cheap to be employed in achieving
		concurrency.


	*/

	// 	Goroutines communication happens using the Channels!
	// What is the purpose of a channel?

	// In simple words, a channel is considered as a pipe through
	// which the Goroutines communicate.

	// Channels are designed to prevent race conditions while the
	// Goroutines access the shared memory.

	// Race conditions tend to happen more in the case of threads
	// and the presence of channels ensure that race conditions do
	// not occur with Goroutines.

	// Goroutines are execution threads! These are lightweight
	// and you can have a lot of them! There will be no issues with
	// system performance.

	// Goroutines are reliable during any kind of unexpected
	// hardware malfunctioning. Since Goroutines is a primary part
	// of Golang, the Go language is so fast!

	// Unlike threads, With Goroutines, there is no need for
	// management or any sort of schedulers to perform
	// concurrent tasks.

	// The memory required to create Goroutines is much less in
	// comparison with the threads.

	// To create a Goroutine it would just require 2 KB of memory!

	// For the threads, it would require 1MB of memory which is

	// approximately 500 times of the memory required to create
	// Goroutines!

	// Memory consumption becomes a huge factor when you
	// build large-scale applications that have to perform several
	// concurrent tasks.

	// Goroutines get created and destroyed by the Go runtime.
	// Never forget this!

	// During the runtime, operations like scheduling, garbage
	// collection and the runtime environment for the Goroutines
	// get created.

	// All these operations are quite cheap since there is no need
	// to request for resources.

	// This is a huge advantage in Golang as one need not request
	// resources from OS and return it back to OS as in the case of
	// threads

	// In this way, Goroutines result in nominal setups and
	// teardown costs and are so much less compared to the
	// threads.

	// Goroutines are basically functions that run concurrency with
	// other functions.

	// In simple words, they are lightweight threads with unique
	// properties.

	// Since the cost to create a Goroutine is less in comparison
	// to the thread, Goroutines become the best way to achieve
	// concurrency.

	// Hence, Go applications usually have more than thousands of
	// Goroutines running in a concurrent fashion.

	// With the presence of Goroutines, concurrency can be
	// achieved with no compromise on system performance.

	// How do you start a Goroutine?

	// You need to use the keyword ‘go’ as a prefix to the function.
	// That function would become the Goroutine

	// There are two major properties of Goroutines to be
	// considered when you code your algorithm

	// One property is that whenever a new Goroutine is started,
	// the goroutine call gets returned immediately

	// Unlike the usual functions, the control never waits for
	// Goroutine to finish execution.

	// 	Remember that the control returns instantly to the next line
	// of code after the Goroutine calls.

	// The return values from the Goroutine get ignored!

	// Another property of Goroutines is that the main Goroutine
	// must be running for any other Goroutine to run successfully.

	// If the main Goroutine itself is terminated, then the program
	// will exit. No other Goroutine will run.

	go hello() //Goroutine

	fmt.Println("Hello main")

	// Consider the following code snippet:

	// package main
	// import (
	// mien ae
	// )
	// func hello() {
	// fmt.PrintIn("Hello Goroutine")

	// func main() {
	// go hello() /Goroutine
	// fmt.PrintIn("Hello main")

	// i

	// The line ‘go Hello()’ in the above code would start a new

	// Goroutine.

	// Now, immediately the hello() function would run concurrently
	// along with the main function of the program.

	// Remember, the main function will run its very own
	// Goroutine. This is commonly referred to as the ‘main

	// Goroutine’

	// What will happen when you run the above code?

	// We will find this out next!

	// 	package main
	// import (
	// tenia
	// )
	// func hello() {
	// fmt.Printin("Hello Goroutine")

	// func main() {
	// go hello() /Goroutine
	// fmt.PrintIn("Hello main")

	// i

	// When you run the above code, you will be surprised! You will
	// find only the output of ‘main function’

	// What happened to the Goroutine that was started!?
	// Recollect the two properties and you might know the
	// reason.

	// 	When the new Goroutine is started, the call will get returned
	// instantly!

	// Remember that control will not wait for the Goroutine to
	// finish its execution.

	// Instead, the control will move to the next line of code after
	// the Goroutine call.

	// The other point is the main Goroutine must be running
	// always to ensure that other Goroutines run.

	// 	Now you will know why the Goroutine never ran! After the
	// call to ‘go hello()’, control instantly returned to the next line
	// of code

	// It did not wait for the hello Goroutine to finish! Instead, prints
	// the main function.

	// Then the main Goroutine terminated as there is no more
	// code! How do we resolve them?

	go hello() //Goroutine

	time.Sleep(2 * time.Second)

	fmt.Println("Hello main")

	// 	The ‘Sleep’ method belonging to the ‘time’ package is called
	// immediately after the call to the Goroutine as shown in the
	// above code.

	// The ‘main’ Goroutine is made to sleep for 1 second. The call
	// to ‘go hello() will have sufficient time for the execution before
	// the termination of the program

	// Now the output of the above code would be ‘Hello
	// Goroutine’, then there is a wait of 1 second, then print “Hello
	// main”.

	// 	You must be familiar with the term ‘Scope’!. What is a scope
	// with regard to a programming language?

	// The scope is basically a specific portion of the program
	// where the defined variable is to exist and beyond the region,
	// the defined variable cannot be accessed.

	// It is important to know the scope of the variables that you
	// have defined in the different parts of the program.

	// 	The variable, in general, can be defined in a class, method or
	// a loop.

	// Based on your functionality of the code, you can define it
	// anywhere in your program.

	// Remember, in Golang, all the identifier are statically scoped!
	// What does it mean by statically scoped?

	// Statically scoped means that that scope of a variable can be
	// determined at compile time. Right at the compile time, the
	// scope of the variable can be determined

	// What exactly it means when it is said that the Go language
	// is a statically scoped language?

	// In simple words, it means that the variable can be called
	// only from within the code block in which the definition has
	// been made.

	// When you try to call or operate on the variables from
	// the place in code where the specific variable cannot be
	// accessed, your code will throw errors!

	// Be sure to understand the scope of a specific variable right
	// at the beginning when you declare them in the code.

	// 	Basically, there are three places where you can declare the
	// variables in the Go language. Make sure you know these
	// places before you declare a variable.

	// You can declare a variable inside a block or it can inside a
	// function. Such a variable is known as the local variable.

	// You can also declare a variable outside all the functions of
	// your Golang program. The variables declared in this manner
	// are known as the global variables.

	// 	You must have come across the concept of global and local
	// variables while coding in other programming languages.

	// When the variables are declared in the function'’s definition
	// of your Golang program, those variables are known as the
	// formal parameters.

	// The term formal parameters are very much associated with
	// the function call and its execution in your Golang program.

	// The scope also impacts the lifetime of a variable! What does
	// this mean exactly?

	// The scope of the variable indicates how long the specific
	// variable persists in the memory.

	// It also indicates when the variable’s storage gets allocated
	// and deallocated.

	// Sometimes you might want multiple functions to use a
	// specific variable which is common to both the functions,
	// in that case, you must declare the variable outside the
	// functions.

	// 	Before you decide where to declare the variable in the Go
	// language, make sure to remember the three scopes, local,
	// global and the formal parameters.

	// Decide whether the variable you define will be required
	// only by a specific function or it is required throughout the
	// program

	// Once you decide on the access regions of each of the
	// variables in your Golang program, you can declare them
	// with the appropriate scope.

	// Let’s see more about local and global scope in the upcoming
	// sub-topic.

	// 	A Golang program will be consisting of the local and
	// global variables in most of the cases. You need to know the
	// uniqueness of both these scopes.

	// Local variables are more common! A local variable is a
	// variable that is declared either inside a block or the function.

	// The block is often depicted with the help of curly brackets {}.
	// Any variables you declare inside a function is termed as the
	// local variable of your Golang code.

	// 	Remember, the local variables cannot be accessible by any
	// condition outside the function or the block.

	// Variables intended for the local scope can be declared inside
	// the for loop, while statement or any condition statement
	// within a function.

	// Never forget that these variables, however, can be accessed
	// by the nested code blocks that are present inside a function.

	// If the local variables are found to be declared twice, with
	// exactly the same name in the same scope, then a compile
	// error will be thrown.

	// When do these local variables fail to exist? Local variables
	// don't exist once the execution of the function is done.

	// Local variables will be completely not known to the
	// functions outside their own function where they have been
	// declared.

	// 	Remember, that the local variables will be accessible to any
	// loop statement that is present within the function.

	// Another point to note is a variable that is declared inside
	// the loop will not be visible to the region outside the loop
	// statement’s body.

	// If you want to declare a variable that is common to many
	// functions, never defined them within a specific function and
	// don't use the concept of local variables.

	// 	What are the global variables? How different are they from
	// the local variables?

	// Global variables are those that are defined outside the
	// function or block in your Go language code.

	// You need to make a variable global if that variable is to be
	// common to all the functions and might be required by more
	// than one function in your code.

	// Global variables are not specific to a certain function. These
	// variables are common to any number of functions or code
	// blocks within a program.

	// Global variables will be available throughout the lifetime of
	// the program.

	// One can access the global variables from any part of the
	// code any number of times until the program terminates.

	// Global variables have an extremely large scope providing
	// access to all the functional or the code blocks present in the
	// Go program to access them.

	// Make sure you don't’ provide a variable both global
	// and variable scope. The meaning of variable scope in
	// programming gets lost.

	// 	The global variables are declared right at the top of the
	// program. You can make as many variables you want as
	// global variables.

	// The global variables need to be declared outside all the
	// functions or blocks present in your Go language.

	// The glocal variables can be accessed from any region of
	// the code and can be used throughout the program after its
	// declaration.

	// 	‘variable is shadowed during return’ is a common error that
	// you might encounter during the execution of the Go lang
	// code.

	// To resolve this error, you need to know the meaning and
	// the exact working of what the curly brackets do inside a
	// function.

	// Remember, each and every set of curly brackets {} defines a
	// completely new level of scope.

	// 	Remember, Go is lexically scoped using the blocks. The curly
	// braces help in defining block scopes.

	// What exactly is variable shadowing and is it common?

	// Variable shadowing occurs when the specific variable is
	// declared with a certain scope has the same name as a
	// variable that has been declared in the outer scope!

	// In this way, the scope of the variable has been shadowed!
	// The outer variable (global)is said to be shadowed by the
	// inner variable (local)

	// In simple terms, we can also refer that the inner identifier is
	// masking the outer identifier!

	// This scenario often leads to a conclusion as there is no
	// clarity in the uses of the variables that are shadowed.

	// While declaring and providing scopes to the variables, you
	// must be aware of the major properties of the Go language.

	// Remember that when you re-declare a variable, a new
	// variable is not introduced! Instead, the new value is assigned
	// to the original with a small constraint

	// 	The small constraint in the redeclaration of variables is that
	// the new value is assigned to the original if they are in the
	// very same block.

	// Shadowing of your Golang variable is a simple type of error
	// and can be detected easily.

	// You can detect the presence of variable shadowing in your
	// Golang source file by using the below command.

	// go tool vet --shadow file.go is the command to detect the
	// presence of variable shadowing in your Golang file.

	// Once you, run the vet command to detect the variable
	// shadowing, you will find the errors stating the line number of
	// code where the variable shadowing is done.

	// main.go:14: declaration of "err" shadows declaration at
	// main.go:13

	// The above is a sample error statement when you run the
	// ‘vet’ command.

	// From the above line, you can conclude that at line number
	// 14 in the file main.go the variable err shadows the
	// declaration made at the line number 13 of your main.go file.

	// 	The idea of variable shadowing might be useful in some
	// cases, but you need to be aware of the scope ranges to
	// avoid some weird behaviors of the variables.

	// It is always best to use different names for the variable to
	// prevent confusion in providing scope to the variables.

	// Know the limitation of the global and local scope, before you
	// decide to mask the scopes of the variables with the same
	// name.

	// 	In simple scenarios like in the case of Goroutines, it is
	// comparatively more readable to shadow the variables.

	// Though the ‘vet’ command helps in detecting the use of
	// shadowed variables. This command will not report all the
	// variables that were shadowed.

	// It is advised to use the go -nyet command to detect the
	// shadowing of the variables in an aggressive manner.

	// 	You might have come across various types of error while
	// trying coding languages like C, C++, Java, Python, etc.

	// The common errors are syntax, runtime, and logic errors.
	// Syntax errors are the easiest to identify and fix.

	// Runtime errors occur when the problem asks the computer

	// system to perform the task which the system cannot reliably
	// do.

	// 	Some examples of Runtime errors include dividing by zero
	// and opening a non-existent file. These are difficult to be
	// identified when compared with syntax errors.

	// Logical errors include the error in the calculation or the logic
	// itself. These are the most difficult to be identified.

	// In languages like C, C++, Java, Python you can handle the
	// errors with the help of exceptions, try, catch and finally
	// block.

	// Remember Go language does not have exceptions! So, there
	// is no try, catch or anything with similar functionality,

	// So, how does Go handle the error? There must definitely be a
	// way to handle errors in Go.

	// The two very common ways of handling errors in Go lang is
	// Multiple Return Values and Panic!

	// We will discuss these in this topic.

	// 	Let’s see about error handling using the Multiple Return
	// Values. With this feature, you can add an error struct to the
	// returned values.

	// Remember, by default, the error value will always be on the
	// right side while the result value will remain on the left.

	// Go allows the multiple return values. Never forget that
	// by default, the function would return an error as the last
	// returned value.

	// Go programming language offers you a simple and precise
	// error handling framework!

	// This error framework will have the ‘inbuilt error interface
	// type’ with the below declaration.

	// type error interface {

	// Error () string

	// Remember that function returns an error as the very last
	// return value. Never get confused while handling the function
	// parameters.

	// Want to construct an error message of your own? Use errors.
	// New! Let’s see how to do that

	// Consider the below function snippet:

	// func Sqrt(value float64) (float64, error) {
	// if(value < O){
	// return 0, errors.New("Math: negative number passed
	// to Sqrt")
	// i

	// return math.Sqrt(value)

	// i

	// The above function is to calculate the square root of a
	// floating-point number.

	// If the entered floating-point number is less than zero, we
	// return the value O along with the error message stating
	// ‘negative number has been entered”
	/*

		result, err:= Sqrt(-1)

		if err != nil {
			fmt.Println(err)
		}
	*/

	// Consider the above code snippet. Here the return value is
	// used. If the error value is not nil, you might want to display
	// the constructed error message.

	// When the function to calculate the square root of the
	// number program is run with the above snippet, you will get
	// the error message if the value passed is a negative number

	// In other cases, the square root of the number will be
	// displayed.

	// ‘Multiple return values’ is one best way to handle the errors
	// in Go language.

	// 	Without stack traces, it becomes extremely difficult to debug
	// as you will not know where the error exactly occurs.

	// A very common problem is that the error might pass through
	// 8 functional calls before you it finally gets to the code that
	// prints the error statement!

	// Here you are stuck! You will not know which functional call
	// exactly caused this error! Stack Traces will help you!

	// The ‘errors’ package is very useful in Golang since its
	// compatible with the standard package.

	// Remember Golang does not have the Stack Trace by default!
	// This is very unlike other programming languages like Java.

	// A Stack trace is generally the set of functions that the
	// specific program was in the middle when the stack trace
	// was printed.
	// result, err:= Sqrt(-1)

	// 	if err != nil {
	// 		fmt.Println(err)
	// 	}

	// 	When and where are the stack traces printed?

	// Stack Traces are printed to the console whenever the
	// unexpected error is said to occur.

	// The best part of Stack traces is that they are extremely
	// useful for debugging purposes!

	// You can not only find where the error happened but also
	// how your program arrived in this particular situation.

	// 	How to print the stack trace for the current Goroutine
	// function?

	// You can print the stack trace with the help of debugging.
	// PrintStack from the package runtime/debug in the Go
	// language.

	// In Go, you can also determine the current stack trace in a
	// programmatic way by calling the ‘runtime.stack’ function.

	// This is often used in designing large-scale applications.

	// 	In the Go language, the ‘GOTRACEBACK ' variable is vital.
	// What is its purpose?

	// GOTRACEBACK variable is responsible for controlling the
	// amount of output generated when the Go program fails.

	// When the GOTRACEBACK variable is none, it denotes that
	// the Goroutine stack trace is omitted entirely.

	// When the GOTRACEBACK variable = all, it denotes that for
	// all the user-created goroutines the stack traces are added.

	// 	What does it mean when the GOTRACEBACK = single?
	// Remember by default, the value of GOTRACEBACK is single.

	// This denotes that stack trace is printed for the current
	// goroutine.

	// In case there is no current Goroutine or when the failure is
	// internal, the stack trace gets printed for all the Goroutines
	// present in the Go program.

	// 	Now, what does it mean when the value of GOTRACEBACK=
	// system

	// This is very much similar to the case when the value of
	// GOTRACEBACK= all! There is only one difference

	// When the GOTRACEBACK= system, the stack frames are
	// added for the run-time functions.

	// Knowing about stack traces is essential to ensure that you
	// know when the program has thrown an error and helps you
	// in determining the exact location of the error.

	// 	Some of the less common Go control flow statements
	// include defer, panic and recover! These are very specific to
	// the Go language.

	// What is a defer statement? This statement is helpful in
	// pushing a specific call onto the list!

	// Then, the list of the saved call gets executed once the value
	// is returned from the surrounding functions

	// Defer is generally used in order to simplify the functions
	// which perform several clean-up operations of the code.

	// 	While using the Defer Statement, you need to be aware of
	// the three basic properties of it.

	// When your defer statement gets evaluated, the deferred
	// function’s parameters get evaluated!

	// Remember this, you must know when the specific deferred
	// function's parameter is evaluated completely.

	// This behavior of the defer statements makes it quite
	// straightforward and predictable. Keep this property while
	// you use the defer statement

	// 	The second property of ‘defer’ is that the ‘Deferred functions
	// get executed in the Last In First Out (LIFO)’ fashion once the
	// surrounding function returns the value.

	// Never forget this second property as it plays a vital role in
	// printing the output value from the functions.

	// The third property of ‘defer’ is that the ‘Deferred functions
	// may read as well as assign to the return value of the
	// returning function’

	// This third rule is quite useful for altering the error return
	// value of a function.

	// 	What does ‘panic’ mean in the Go language? It is a
	// significant built-in function of Golang.

	// This built-in function, Panic is responsible for stopping the
	// normal flow of control and begins to panic.

	// How can ‘Panic’ be invoked? Can it be done purposefully?
	// Yes, you can do it if you desire to

	// ‘Panics’ can be initiated by two major ways. One way is to
	// initiate ‘Panics’ by invoking it in a direct fashion.

	// Panics are also sometimes caused due to the runtime errors
	// like the out-of-bound arrays.

	// 	Let's see a simple example to under the ‘Panic’ built-in
	// function!

	// When a specific function ‘F’ calls the ‘Panic’ option, the
	// execution of that functions gets stopped!

	// The deferred functions present in the function ‘F’ get
	// executed in an absolutely normal manner. The function F
	// then returns to its caller.

	// Then the function F reacts and behaves like a call to the
	// ‘Panic’ to the caller itself.

	// This goes on up the stack until all functions present in
	// the current Goroutines have returned at Which point the
	// program crashes.

	// 	What is a ‘Recover’ function in the Go language? What is its
	// functionality?

	// Recover is a built-in function which is only useful inside
	// deferred functions.

	// This built-in function helps in regaining the control of a
	// Goroutine that is panicking.

	// You definitely need to recover the control of a Goroutine from
	// the panicking phase to continue the execution process.

	// 	Remember, during the normal execution, the call to recover
	// will return nil. It will have no other effect.

	// And if your current Goruitne is under the ‘Panic; phase, the
	// call to recover will completely capture the value provided to
	// the ‘Panic'.

	// Once the value offered to panic is captured, the normal
	// executed is continued from the stop point.

	// Defer, Panic, Recover functionality are vital while handling
	// the errors in the Go Language.

	fmt.Print("Ending the program")
	for i := 0; i < 3; i++ {
		time.Sleep(2 * time.Second) // Pauses the program for 2 seconds
		fmt.Print(".")
	}
	fmt.Println()
	fmt.Print("Press any key to continue...>> ")

	// Create a new reader from standard input (os.Stdin)
	reader := bufio.NewReader(os.Stdin)

	// Read a single byte from the reader
	_, _ = reader.ReadByte()

	fmt.Print("Continuing")
	for i := 0; i < 3; i++ {
		time.Sleep(1 * time.Second) // Pauses the program for 1 seconds
		fmt.Print(".")
	}

}

// Example function that returns two values
func someFunctionThatReturnsTwoValues() (string, string) {
	return "value1", "value2"
}

// Example swap function that returns one value
func swap(a, b string) {
	fmt.Println(a + " " + b)
}
func factorial(i int) int {
	if i <= 1 {
		return 1
	}
	return i * factorial(i-1)
}

// func Sqrt(value float64) (float64, error) {
// 	 if(value < O){
// 	 return 0, errors.New("Math: negative number passed
// 	 to Sqrt")
// 	 }

// 	 return math.Sqrt(value)

// }
