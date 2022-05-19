<?php
    include "./connect.php";
    session_start();

    $date = $_POST["date"];
    $time = $_POST["time"];
    $duration = $_POST["duration"];
    $reservedcabin = $_POST["reservedcabin"];
    $bin = $_POST["bin"];
    $link = KonektatuDatuBasera();
    $price = mysqli_query($link, "SELECT exh FROM cabins WHERE ID = '$reservedcabin'");
    $price = mysqli_fetch_array($price);
    $price = $price["exh"];
    $totalprice = (int)$price * (int)$duration;
    header("Location: ../reserve.php?bin=$bin&pr=$price&cb=$reservedcabin");
?>
