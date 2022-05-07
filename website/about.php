<html>
	<head>
		<title>About us - uni2</title>
		<?php include ("./elements/bs4.html"); ?>
        <link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<?php session_start();?>
		<div class="main">
			<?php include ("./elements/navbar.php"); ?>
				<div class="space"></div>
				<h1 class="title">Where we are</h1>
				<div class="location">
					<div class="map">
						<!-- THE IFRAME WILL GO HERE -->
					</div>
					<div class="address">
						<h3>Address</h3>
						<p>
							<strong>DIY garage name</strong>
							<br>
							street name,
							<br>
							postal code
							<br>
							city
							<br>
							phone number
						</p>
					</div>
				</div>
				<div class="spacel"></div>
				<h1 class="title">About us</h1>
				<div class="maincontent">
					<p>
						Lorem ipsum dolor sit amet, consectetur adipiscing elit.
						Sed euismod ipsum eget nunc tincidunt, eget euismod nunc lobortis.
						Sed euismod ipsum eget nunc tincidunt, eget euismod nunc lobortis.
					</p>
					<!-- Put the garage's images or something here -->
					<img src="./images/sample.jpg" />
				</div>
			<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>