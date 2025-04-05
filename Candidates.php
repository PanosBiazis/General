<?php 
include 'Connector.php';//include the connection file
$result=$conn->query("SELECT * FROM contestants");//query anything you want

$all=$result->fetch_all();//fetch everything from the query result
$col=$all[0];//get the first row
$columns=array();//create an empty array to hold column names
echo "<pre>";//display the data in a table format
foreach($col as $key => $value){//loop through the column names
    if(is_string($key)){//if the column name is a string, add it to the columns array
    $columns[]=$key;//add the column name to the columns array
    }
}
echo "<table boarder='1'>";//display the data in a table format
foreach($columns as $value){//loop through the column names and display them as table headers
    echo "<th>$value</th>";
}

for($x=0;$x<count($all);$x++){//loop through the rows
    echo "<tr>";//display the data in a table format
    foreach($all[$x] as $key => $value){//loop through the columns
       for($y=0;$y<count($columns);$y++){//loop through the column names
        echo "<td>".$all[$x][$y]."</td>";//display each value in its respective cell
       }
    }
    echo "</tr>";
}
echo "</table>";

?>