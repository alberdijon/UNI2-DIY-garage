<html>
	<head>
		<title>uni2</title>
		<link rel="stylesheet" href="styles.css" />
		<?php include ("./elements/bs4.html"); ?>
	</head>
	<body>
		<div class="main">
		<?php include ("./elements/navbar.php"); ?>
        <div class="space"></div>
			<h1 class="title">Make a reservation</h1>
            <div class="reservemain">
                <div class="rdatetime">
                    <h3>Date and time</h3>
                </div>
                <div class="rgarage">
                    <h3>Select a cabin</h3>
                </div>
                <div class="rconfirm">
                    <h3>Price</h3>
                    <button class="greenbutton" type="submit">Confirm</button>
                </div>
            </div>
		<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>