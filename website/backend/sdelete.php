<?php
    include "./connect.php";
    session_start();

    $link = KonektatuDatuBasera();
    $Product_ID = $_POST["id"];

    if ($_SESSION["userID"] == "admin") {
        try {
            mysqli_query(
                $link,
                "DELETE FROM product WHERE ID = '$Product_ID'"
            );
            header("Location:../shop.php?deleted=true");
        } catch (Exception $e) {
            header("Location:../shop.php?deleted=error");
        }
    } else {
        header("Location:../shop.php?deleted=false");
    }

?>
