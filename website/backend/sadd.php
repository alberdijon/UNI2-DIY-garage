<?php
    include "./connect.php";
    session_start();

    $Brand = $_POST["brand"];
    $Name = $_POST["name"];
    $Price = $_POST["price"];
    $Stock = $_POST["stock"];
    if(isset($_FILES['image'])){
        $image = $_FILES['image']['name'];
        $tmp_name = $_FILES['image']['tmp_name'];
        $path = "./shoppics/".$image;
        move_uploaded_file($tmp_name, $path);
    }

    if ($_SESSION["userID"] == "admin") {
        try {
            $link = KonektatuDatuBasera();
            mysqli_query(
                $link,
                "INSERT INTO product (Brand, Name, Price, Stock) VALUES ('$Brand', '$Name', '$Price', '$Stock')"
            );
            header("Location:../shop.php?added=true");
        } catch (Exception $e) {
            header("Location:../shop.php?added=error");
        }
    } else {
        header("Location:../shop.php?added=false");
    }
?>
