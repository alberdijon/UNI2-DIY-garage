<?php
    include "./connect.php";
    session_start();
    
    $reserve_cabin = $_POST['rrcabin'];
    $reserve_date = $_POST['rrdate'];
    $reserve_time = $_POST['rrtime'];
    $reserve_dni = $_SESSION["userID"];
    $reserve_price = $_POST['reserve_price'];
    $link = KonektatuDatuBasera();  

    $sql = "INSERT INTO reservation VALUES ('$reserve_cabin', '$reserve_dni', '$rrtime', '$rrdate', '$reserve_price')";
    mysqli_query($link, $sql);
    header("Location: ../reserve.php?reserve=success");
?>
