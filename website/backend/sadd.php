<?php
    include "./connect.php";
    session_start();

    $Brand = $_POST["brand"];
    $Name = $_POST["name"];
    $Price = $_POST["price"];
    $Stock = $_POST["stock"];
    if(isset($_FILES['image'])){
        $errors= array();
        $file_name = $_FILES['image']['name'];
        $file_size = $_FILES['image']['size'];
        $file_tmp = $_FILES['image']['tmp_name'];
        $file_type = $_FILES['image']['type'];
        $file_ext=strtolower(end(explode('.',$_FILES['image']['name'])));
        
        $expensions= array("jpeg","jpg","png");
        
        if(in_array($file_ext,$expensions)=== false){
            $errors[]="extension not allowed, please choose a JPEG or PNG file.";
        }
        
        if($file_size > 2097152) {
            $errors[]='File size must be less than 2 MB';
        }
        
        if(empty($errors)==true) {
            move_uploaded_file($file_tmp,"../shoppics/".$file_name);
            echo "Success";
        }else{
            print_r($errors);
        }
    }

    if ($_SESSION["userID"] == "admin") {
        try {
            $link = KonektatuDatuBasera();
            if (isset($_FILES['image'])) {
                mysqli_query(
                    $link,
                    "INSERT INTO product (Brand, Name, Price, Stock, img) VALUES ('$Brand', '$Name', '$Price', '$Stock', '$file_name')"
                );
            } else {
                mysqli_query(
                    $link,
                    "INSERT INTO product (Brand, Name, Price, Stock) VALUES ('$Brand', '$Name', '$Price', '$Stock')"
                );
            }

            header("Location:../shop.php?added=true");
        } catch (Exception $e) {
            header("Location:../shop.php?added=error");
        }
    } else {
        header("Location:../shop.php?added=false");
    }
?>
