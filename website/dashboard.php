<html>
	<head>
		<title>Dashboard - PitStop</title>
		<?php include ("./elements/bs4.html"); ?>
        <link rel="stylesheet" href="styles.css" />
	</head>
	<body>
        <?php
            session_start();
            if(!isset($_SESSION['name'])){
                header("Location: login.php");
            } else {
                $user = $_SESSION['name'];
            }
        ?>
		<div class="main">
		    <?php include ("./elements/navbar.php"); ?>
            <div class="space"></div>
			<h1 class="title">Account dashboard</h1>
            <div class="drow drow1">
                <div class="dcardl duser">
                    <div class="duseru">
                        <h2>Welcome, <?php echo "$user"; ?></h2>
                        <span>Not <?php echo "$user"?>? <a href="./backend/logout.php">Log out</a></span>
                    </div>
                    <div class="duserimg">
                        <img src="./pfps/default.jpg" alt="user">
                    </div>
                </div>
                <div class="dcardl dsettings">
                    <h2>Settings</h2>
                    <span>
                        <a href="./settings.php">Change password</a>
                        <a href="./settings.php">Change email</a>
                        <a href="./settings.php">Change profile picture</a>
                    </span>
                </div>
            </div>
            <div class="drow drow2">
                <div class="dcardm dappointment">
                    <h2>Appointments</h2>
                </div>
                <div class="dcardm dvehicles">
                    <h2>Your vehicles</h2>
                </div>
            </div>
		    <?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>