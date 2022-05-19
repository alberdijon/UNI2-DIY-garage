<?php
    include "./connect.php";
    session_start();

    $date = $_POST["date"];
    $time = $_POST["time"];
    $duration = $_POST["duration"];
    $timewindow = date('H:i:s', strtotime("$time + $duration hours"));
    $link = KonektatuDatuBasera();
    $bin = 0;
    for ($cabin = 1; $cabin <= 6; $cabin++) {
        if($duration == "1") {
            $sql = "SELECT * FROM reservation WHERE Date = '$date' AND Hour = '$time' AND Cabin_ID = '$cabin'";
        } else {
            $sql = "SELECT * FROM reservation WHERE Date = '$date' AND (Hour BETWEEN '$time' AND '$timewindow') AND Cabin_ID = '$cabin'";
        }
        
        $result = $link->query($sql);
        if ($result->num_rows > 0) {
            $bin = $bin + (pow(2, ($cabin - 1)));
        }
    }
    header("Location: ../reserve.php?bin=$bin&dt=$date&tm=$time");
?>
