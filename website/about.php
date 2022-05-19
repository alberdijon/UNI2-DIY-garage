<html>
	<head>
		<title>About us - PitStop</title>
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
					<iframe class="map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d432.4814034307407!2d-2.4853375993070195!3d43.18061043650664!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd4e2af15dc66a27%3A0xb190c3a6d8b2ce32!2zQ2Fycm9jZXLDrWFzIEpvc8Op!5e0!3m2!1sen!2ses!4v1652890276645!5m2!1sen!2ses" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
					<div class="address">
						<h3>Address</h3>
						<p>
							<strong>PitStop</strong>
							<br>
							Otaola Avenue, 21
							<br>
							20600
							<br>
							Eibar, Gipuzkoa
							<br>
							943 00 11 22
						</p>
					</div>
				</div>
				<div class="spacel"></div>
				<h1 class="title">About us</h1>
				<div class="maincontent">
					<p>
						We're a small team with a garage to help you with all your car-related needs. We're located in Eibar, please feel free to visit us anytime. Contact us if you have any questions.
					</p>
					<!-- Put the garage's images or something here -->
					<img src="./images/alex-suprun-AHnhdjyTNGM-unsplash.jpg" />
				</div>
			<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>