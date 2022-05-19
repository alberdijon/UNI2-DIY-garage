<?php
    include("connect.php");

    $email=$_POST["email"];
    $password=$_POST["password"];

    $link=KonektatuDatuBasera();
    $emaitza=mysqli_query($link,"SELECT E_mail, Password
                                FROM client
                                WHERE E_mail = '$email' AND Password = '$password'
                        ");

    if(mysqli_num_rows($emaitza)==0){
        header("Location:../login.php?credentials=false");
    }
    else{
        $name = mysqli_query($link,"SELECT Name FROM client WHERE E_mail = '$email'");
        $name = mysqli_fetch_array($name);
        $name = $name[0];

        $email = mysqli_query($link,"SELECT e_mail FROM client WHERE E_mail = '$email'");
        $email = mysqli_fetch_array($email);
        $email = $email[0];

        $userID = mysqli_query($link,"SELECT DNI from client WHERE E_mail = '$email'");
        $userID = mysqli_fetch_array($userID);
        $userID = $userID[0];
        
        session_start();

        $_SESSION['name'] = $name;
        $_SESSION['email'] = $email;
        $_SESSION['userID'] = $userID;

        header("Location:../dashboard.php");
    }
?>