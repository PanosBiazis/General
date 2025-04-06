package main

import (
	"fmt"
	"time"
)

func main() {
	// Working with maps
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

	s := 2
	s2 := int(s)
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

	// Loops
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Nested loops
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

	// Goto statement
	fmt.Println(1)
	goto End
	fmt.Println(2)
End:
	fmt.Println(3)

	// Ranging over slices
	strings := []string{"hello", "all", "of", "you"}
	for index, value := range strings {
		fmt.Println(index, value)
	}
	for _, value := range strings {
		fmt.Println(value)
	}

	// Using time.Sleep
	for i := 0; i < 3; i++ {
		time.Sleep(1 * time.Second)
		fmt.Println(i)
	}
	fmt.Println("Ending the program")
}
