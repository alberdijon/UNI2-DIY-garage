<?php
    include "./connect.php";
    session_start();

    $date = $_POST["date"];
    $time = $_POST["time"];
    $cabin = $_POST["cabin"];
    $price = $_POST["price"];
    $dni = $_SESSION["userID"];
    $link = KonektatuDatuBasera();
    echo $date;
    echo $time;
    echo $cabin;
    echo $price;
    echo $dni;
    
    $sql = "INSERT INTO reservation VALUES ('$cabin', '$dni', '$time', '$date', '$price')";
    mysqli_query($link, $sql);
    header("Location: ../reserve.php?reserve=success");
?>
