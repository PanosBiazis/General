 <?php
 //This is my first PHP program.
 //myfirstphp.php 
 echo "Hello World"; // This is my first PHP program.
 //with echo, the output will be displayed on the browser as text: Hello World
 //Comments
/*
 * This is a comment. It's not part of the code, but will be read by the programmer when they are reading it.
 */
 //php stands for Hypertext Preprocessor
 //$ is a variable sign - used to store values in variables
 //$name = "John";
 //echo $name;
 echo "<br>";
 $text="Hey PHP Fan!";//text is a variable that stores string value
 echo "<br>";//new line
 $a=4;//a is a variable that stores integer value
 $b=5;//b is a variable that stores integer value
 echo $text;//text is a variable
 echo "<br>";//new line
 echo $a+$b;//a and b are variables added together
 $website="programminghub.io";//website is a variable inside a string which is printed using double quotes "" that stores website name
 echo "<br> I love to learn from $website";//print I love to learn from website which is stored in the variable website</span>
 echo "<br>";//new line
 /*
  *Datatypes in php has three categories:
  Scalar Types
  Compound Types
  Special Types
  Scalar Types
  *
  *Scalar Types:
  *String
  *Integer
  *Float
  *Boolean
  *
  *Compound Types:
  *Array
  *Object
  *
  *Special Types:
  *NULL
  *Resource
 */
echo $a,"<br>";//a is a variable and $a is a string
echo $b,"<br>";//b is a variable and $b is a string
$x=3.96;//x is a variable and $x is a float
echo $x,"<br>";//x is a variable and $x is a float
$y=true;//y is a variable and $y is a boolean
echo $y,"<br>";//y is a variable and $y is a boolean
$z=null;//z is a variable and $z is a null
echo $z,"<br>";//z is a variable and $z is a null
echo ($a+$b),"<br>";//a and b are variables added together
echo ($a-$b),"<br>";//a and b are variables subtracted
echo ($a*$b),"<br>";//a and b are variables multiplied
echo ($a/$b),"<br>";//a and b are variables divided
echo ($a%$b),"<br>";//a and b are variables modulus
$c=$a+$b;
echo $c,"<br>";//c is a variable and $c is a integer
$hip="You";
$hop="are";
$hooray="amazing";
$compliment=$hip.$hop.$hooray; //concatenation of strings using . operator 
echo $compliment."!<br>";//compliment is a variable and displays "You are amazing!"</span>
$x=$f="hello";
echo $x,"<br>";
echo $f,"<br>";
$mymovieRating=1;
$mymovieRating+=1;
echo $mymovieRating,"<br>";
var_dump($a==$b);//var_dump displays the type and value of a variable
echo "<br>";//new line
var_dump($a!=$b);//var_dump displays the type and value of a variable
echo "<br>";//new line
var_dump($a>$b);//var_dump displays the type and value of a variable
echo "<br>";
var_dump($a<$b);
echo "<br>";
var_dump($a>=$b);
echo "<br>";
var_dump($a<=$b);
echo "<br>";
var_dump($a<>$b);
echo "<br>";
var_dump($a===$b);
echo "<br>";
var_dump($a!==$b);
echo "<br>";
var_dump($a&&$b);
echo "<br>";
var_dump($a||$b);
echo "<br>";
var_dump($a xor $b);
echo "<br>";
var_dump(!$a);
echo "<br>";
var_dump($a??$b);
echo "<br>";
//Operator precedence
echo $a+$b*2,"<br>";
echo ($a+$b)*2,"<br>";
echo $a+($b*2),"<br>";
echo $a+$b*2+3,"<br>";
echo ($a+$b)*2+3,"<br>";
echo $a+($b*2)+3,"<br>";
echo ($a+$b)*2+3+4,"<br>";
echo $a+($b*2)+3+4,"<br>";
echo ($a+$b)*2+3+4+5,"<br>";
echo $a+($b*2)+3+4+5,"<br>";
echo ($a+$b)*2+3+4+5+6,"<br>";
echo $a+($b*2)+3+4+5+6,"<br>";
echo ($a+$b)*2+3+4+5+6+7,"<br>";
echo $a+($b*2)+3+4+5+6+7,"<br>";
echo ($a+$b)*2+3+4+5+6+7+8,"<br>";
echo $a+($b*2)+3+4+5+6+7+8,"<br>";
echo ($a+$b)*2+3+4+5+6+7+8+9,"<br>";
echo $a+($b*2)+3+4+5+6+7+8+9,"<br>";
echo ($a+$b)*2+3+4+5+6+7+8+9+10,"<br>";
echo $a+($b*2)+3+4+5+6+7+8+9+10,"<br>";
echo $x and $y || $z; //bitwise AND has higher priority than logical AND
echo "<br>";
echo $x and $y and $z; //bitwise AND has higher priority than logical AND
echo $x && ($y || $z); // logical AND has higher priority than bitwise or
$day="monday";
if ($day=="sunday"){
    echo "Today is Sunday";
}else if($day=="monday"){
    echo "Today is Monday <br>";
}else if($day=="tuesday"){
    echo "Today is Tuesday";
}else if($day=="wednesday"){
    echo "Today is Wednesday";
}else if($day=="thursday"){
    echo "Today is Thursday";
}else if($day=="friday"){
    echo "Today is Friday";
}else if($day=="saturday"){
    echo "Today is Saturday";
}else{
    echo "Invalid day";
}
$age=20;
switch($age){
    case '0-1': 
        echo "Baby";
        break;
    case '2-3':
        echo "Toddler";
        break;
    case '4-5':
        echo "Preschooler";
        break;
    case '6-7':
        echo "School Age <br>";
        break;
    case '8-12':
        echo "kid <br>";
        break;
    case '13-17':
        echo "Teenager";
        break;
    case '18-99999':
        echo "Adult";
        break;    
    default:
        echo "Invalid age";
        break;
}
for($i=0;$i<10;$i++){
    echo $i,"<br>";
}
for($i=0;$i<10;$i++){
    if($i==5){
        break;
    }
    echo $i,"<br>";
}
for($i=0;$i<10;$i++){
    if($i==5){
        continue;
    }
    echo $i,"<br>";
}
for($i=0;$i<10;$i++){
    if($i==5){
        return;
    }
    echo $i,"<br>";
}
$i=0;
while($i<10){
    echo $i,"<br>";
    $i++;
}
echo "Done! <br>";
do{
    echo $i,"<br>";
    $i++;
}while($i<10);
$array_cars=array("Volvo","BMW","Toyota","Mercedes","Hyundai","Kia","Volkswagen","Skoda","Jaguar","Fiat","Tesla","Audi");
echo $array_cars[0];
echo "<br>";
echo $array_cars[1];
echo "<br>";
echo $array_cars[2];
echo "<br>";
echo $array_cars[3];
echo "<br>";
echo $array_cars[4];
echo "<br>";
echo $array_cars[5];
echo "<br>";
echo $array_cars[6];
echo "<br>";
echo $array_cars[7];
echo "<br>";
echo $array_cars[8];
echo "<br>";
echo $array_cars[9];
echo "<br>";
echo $array_cars[10];
echo "<br>";
echo $array_cars[11];
echo "<br>";
echo $array_cars[12];
echo "<br>";
echo $array_cars[0],"<br>";
echo $array_cars[1],"<br>";
echo $array_cars[2],"<br>";
echo $array_cars[3],"<br>";
echo $array_cars[4],"<br>";
echo $array_cars[5],"<br>";
echo $array_cars[6],"<br>";
echo $array_cars[7],"<br>";
echo $array_cars[8],"<br>";
echo $array_cars[9],"<br>";
echo $array_cars[10],"<br>";
echo $array_cars[11],"<br>";
echo $array_cars[12],"<br>";
echo $array_cars[0],"<br>";
echo $array_cars[1],"<br>";
echo $array_cars[2],"<br>";
echo $array_cars[3],"<br>";
echo $array_cars[4],"<br>";
echo $array_cars[5],"<br>";
echo $array_cars[6],"<br>";
echo $array_cars[7],"<br>";
/*There are types of arrays:
1. Indexed Arrays
2. Associative Arrays
3. Multidimensional Arrays
*/
$name=array("John","Jane","Jack","Jill");//name is an array with 4 elements
echo $name[0];//name is an array with 4 elements so the first element in this array is John
echo "<br>";//line break
echo $name[1];
echo "<br>";
echo $name[2];
echo "<br>";
echo $name[3];
echo "<br>";
$name1=array("John","Jane","Jack","Jill");//name1 is an array with 4 elements but we have added one more element to it
echo $name1[0];
echo "<br>";
echo $name1[1];
echo "<br>";
echo $name1[2];
echo "<br>";
echo $name1[3];
echo "<br>";
echo $name[0]."<br>".$name1[1]."<br>".$name[2]."".$name1[3]; //Concatenation with indexed arrays
//Associative arrays
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");//age is an associative array with keys as names and values as ages
echo $age["Peter"];//age is an associative array with keys as names and values as ages so the value of Peter is 35
echo "<br>";
echo $age["Ben"];
echo "<br>";
echo $age["Joe"];
echo "<br>";
echo $age["Peter"].$age["Ben"].$age["Joe"];//Concatenation with associative arrays
$movie=array(//movie is an associative array with keys as titles, years and directors
    "title"=>"The Matrix",
    "year"=>"1999",
    "director"=>"Wachowski"
);
echo $movie["title"]."<br>";
echo $movie["year"]."<br>";
echo $movie["director"]."<br>";
echo $movie["title"].$movie["year"].$movie["director"];
echo "<br>";
echo $movie["title"]."<br>";
echo $movie["year"]."<br>";
echo $movie["director"]."<br>";
echo $movie["title"].$movie["year"].$movie["director"];
$movie2=array(//movie2 is an associative array with keys as titles, years and directors. It has only one key-value pair
    'comedy'=> array('Pink Panther'),
    'action'=> array('Die Hard'),
    'epic'=> array('The lord of the rings'),
    'romance'=> array('Romeo and Juliet')
);
//Multidimensional Array
echo $movie2["comedy"][0];
echo "<br>";
echo $movie2["action"][0];
echo "<br>";
echo $movie2["epic"][0];
echo "<br>";
echo $movie2["romance"][0];
$employee=[
    "name"=>"John",
    "sport"=>["football","cricket"],
    "social media"=>['Facebook'=>'@john','Twitter'=>'@john'],
    "age"=>25,
    "salary"=>50000
];
//Accessing Multidimensional Array
echo $employee["name"];
echo "<br>";
echo $employee["age"];
echo "<br>";
echo $employee["salary"];
echo "<br>";
echo $employee["sport"][0];
echo "<br>";
echo $employee["social media"]["Facebook"];
echo "<br>";
echo $employee["social media"]["Twitter"];
echo "<br>";
echo $employee["sport"][1];
echo "<br>";
echo $employee["social media"]["Facebook"];
echo "<br>";
echo $employee["social media"]["Twitter"];
echo "<br>";
foreach ($array_cars as $brand){//foreach loop for cars array
    echo $brand,"<br>";
}
function my_message(){//function
    echo "Welcome to ProgrammingHub! <br>";
}
my_message();//calling the function
function add($x,$y){//function
    return $x+$y;
}
echo add(5,10);//calling the function with parameters 5 and 10</span>
function myGreeting($firstName){
    echo "Hello there $firstName <br>";
}
myGreeting("John");
myGreeting("Jane");
myGreeting("Jack");
myGreeting("Jill");
function myGreeting1($regards="Birthday"){
    echo "Wish you a very Happy $regards <br>";
}
echo "Hello Joe! <br>";
myGreeting1();
echo "Hello Jane! <br>";
myGreeting1("Anniversary");
echo "Hello Jack! <br>";
myGreeting1("Wedding");
echo "Hello Jill! <br>";
myGreeting1("Christmas");
$myRank=add(50,50);
echo $myRank;
//pass by value
$myNumber=5;
function improve($value){
    $value+=1;
    echo $value,"<br>";
}
//increase the counter
improve($myNumber);
echo $myNumber,"<br>";
//pass by reference
function improve1(&$value){
    $value+=1;
    echo $value,"<br>";
}
//increase the counter
improve1($myNumber);
echo $myNumber,"<br>";
 ?>