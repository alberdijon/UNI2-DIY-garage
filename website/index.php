<html>
	<head>
		<title>Welcome - uni2</title>
		<link rel="stylesheet" href="styles.css" />
		<?php include ("./elements/bs4.html"); ?>
	</head>
	<body>
		<?php session_start();?>
		<div class="main">
			<?php include ("./elements/navbar.php"); ?>
		</div>
		<div class="hero-image">
			<div class="hero-text">
				<h1>Welcome to our garage</h1>
				Scroll down for more info
			</div>
		</div>
		<div class="main">
			<div class="spacel"></div>
			<h1 class="title">Do it yourself.</h1>
			<div class="maincontent"></div>
			<div class="maincontent"></div>
		<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>
