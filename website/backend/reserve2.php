<?php
    include "./connect.php";
    session_start();

    $date = $_POST["date"];
    $time = $_POST["time"];
    $duration = $_POST["duration"];
    $cabin = $_POST["cabin"];
    $bin = $_POST["bin"];
    $link = KonektatuDatuBasera();
    $price = mysqli_query($link, "SELECT exh FROM cabins WHERE ID = '$cabin'");
    $price = mysqli_fetch_array($price);
    $price = $price["exh"];
    $totalprice = (int)$price * (int)$duration;
    header("Location: ../reserve.php?bin=$bin&pr=$price");
?>
