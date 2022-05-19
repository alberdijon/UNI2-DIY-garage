<html>
	<head>
		<title>Welcome - PitStop</title>
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
				<h1>Welcome to PitStop</h1>
				Scroll down for more info
			</div>
		</div>
		<div class="main">
			<div class="spacel"></div>
			<h1 class="title">Do it yourself.</h1>
			<div class="maincontent">
				<p>
					PitStop is all about fixing your own car. We have a wide range of tools and parts to choose from. You can rent a cabin for a few hours and use everything you need to make your car look like new.

				</p>
				<!-- Change the image -->
				<img src="./images/nina-mercado-e9YFrEBWit8-unsplash.jpg" />
			</div>
			<!-- spacel adds a (L)ittle space -->
			<div class="spacel"></div>
			<h1 class="title">You can do anything.</h1>
			<div class="maincontent">
				<p>
					From bikes to electric cars, from tire changes to engine repairs, you can have all the tools you need at a place where you can do it yourself. We probably have every tool you can think of. Rent a cabin now!
				</p>
				<!-- Change the image -->
				<img src="./images/obi-pixel6propix-05xv0tuIm6M-unsplash.jpg" />
			</div>
			<div class="spacel"></div>
			<!-- if you wanna add more content go ahead, add a spacel div + a maincontent one -->
			<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>
