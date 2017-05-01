<?php
// Create connection
$user = "bdudley3"; 
$con=mysqli_connect("localhost",$user,$user,$user);

// Check connection
if (mysqli_connect_errno()) {
  echo "<b>Failed to connect to MySQL: " . mysqli_connect_error() . "</b>";
}
else {
     echo "Connect established";
}

?> 

This is called testconnect.php