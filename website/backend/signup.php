<?php
include "./connect.php";

$name = $_POST["name"];
$surname = $_POST["surname"];
$DNI = $_POST["DNI"];
$phone = $_POST["phone"];
$email = $_POST["email"];
$password = $_POST["password"];

$link = KonektatuDatuBasera();
$emaitza = mysqli_query(
	$link,
	"SELECT E_mail FROM client WHERE E_mail = '$email'"
);

if (mysqli_num_rows($emaitza) == 0) {
	mysqli_query(
		$link,
		"INSERT into client values ('$name', '$surname', '$phone', '$email', '$DNI', '$password')"
	);
	header("Location:../signup.php?signup=true");
} else {
	header("Location:../signup.php?signup=false");
}

?>
