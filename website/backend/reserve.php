<?php
    include "./connect.php";
    session_start();

    $date = $_POST["date"];
    $time = $_POST["time"];
    $duration = $_POST["duration"];
    $cabin = $_POST["cabin"];

    $link = KonektatuDatuBasera();
    // tell me which cabins have registries in cabin-client at the selected date and time
    $sql = "SELECT * FROM cabins WHERE EXISTS (SELECT * FROM cabin-client WHERE cabins.ID = cabin-client.Cabin_ID AND (cabin-client.date = '$date' AND (cabin-client.Hour BETWEEN '$time' AND '$time' + INTERVAL $duration HOUR)))";
    $result = mysqli_query($link, $sql);
    $cabins = array();
    while($row = mysqli_fetch_assoc($result)) {
        array_push($cabins, $row['ID']);
    }
    $price = $row['€xh'];
    $total = $price * $duration;

    if (!isset($_POST[cabin])) {     
        header("Location: ../reserve.php");
    } else {
        echo("hello");
    }
?>
