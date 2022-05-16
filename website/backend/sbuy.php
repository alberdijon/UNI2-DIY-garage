<?php
    include "./connect.php";
    session_start();

    $link = KonektatuDatuBasera();
    $Product_ID = $_POST["ID"];
    $Client_DNI = $_SESSION["userID"];
    $Date = date("Y-m-d");
    $Hour = date("H:i:s");
    $Amount = $_POST["amount"];
    $Price = $_POST["price"];

    $Total_price = (int)$Amount * (int)$Price;

    mysqli_query(
        $link,
        "INSERT INTO shop (Product_ID, Client_DNI, Date, Hour, Amount, Total_price) VALUES ('$Product_ID', '$Client_DNI', '$Date', '$Hour', '$Amount', '$Total_price')"
    );
    mysqli_query(
        $link,
        "UPDATE product SET Stock = Stock - '$Amount' WHERE ID = '$Product_ID'"
    );
    header("Location:../shop.php?purchased=true");

?>
