<?php
    include "./connect.php";
    session_start();

    $date = $_POST["date"];
    $time = $_POST["time"];
    $duration = $_POST["duration"];
    $link = KonektatuDatuBasera();
    $bin = 0;
    for ($cabin = 1; $cabin <= 6; $cabin++) {
        $sql = "SELECT * FROM reservation WHERE Date = '$date' AND Hour = '$time' AND Cabin_ID = '$cabin'";
        $result = $link->query($sql);
        if ($result->num_rows > 0) {
            $bin = $bin + ($cabin * $cabin);
        }
    }
    header("Location: ../reserve.php?bin=$bin");
?>
