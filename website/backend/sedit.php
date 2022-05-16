<?php
    include "./connect.php";
    session_start();

    $ID = $_POST["id"];
    $Brand = $_POST["brand"];
    $Name = $_POST["name"];
    $Price = $_POST["price"];
    $Stock = $_POST["stock"];

    if ($_SESSION["userID"] == "admin") {
        if (isset($_POST["edited"])) {
            try {
                $link = KonektatuDatuBasera();
                mysqli_query(
                    $link,
                    "UPDATE product SET Brand='$Brand', Name='$Name', Price='$Price', Stock='$Stock' WHERE ID='$ID'"
                );
                header("Location:../shop.php?edited=true");
            } catch (Exception $e) {
                header("Location:../shop.php?edited=error");
            }
        } else {
            ?>
                <form action="./sedit.php" method="post">
                    <input type="hidden" name="id" value="<?php echo $ID; ?>">
                    <input type="hidden" name="edited" value="true">
                    <input type="text" name="brand" value="<?php echo $Brand; ?>">
                    <input type="text" name="name" value="<?php echo $Name; ?>">
                    <input type="number" min=0 name="price" value="<?php echo $Price; ?>">
                    <input type="number" min=0 name="stock" value="<?php echo $Stock; ?>">
                    <input type="submit" value="Edit">
                </form>
            <?php
        }
    } else {
        header("Location:../shop.php?added=false");
    }
?>