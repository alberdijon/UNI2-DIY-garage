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
			<div class="maincontent">
				<p>
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed optio repudiandae natus sequi quo quos officia! Quis alias hic, tempore libero placeat quibusdam non asperiores. Sint vitae maxime neque distinctio!
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis fugiat cupiditate, quis modi nemo dolorem itaque magnam facere cum laborum nihil doloribus at minima officia deleniti nostrum eum reiciendis ut.
				</p>
				<!-- Change the image -->
				<img src="./images/sample.jpg" />
			</div>
			<!-- spacel adds a (L)ittle space -->
			<div class="spacel"></div>
			<h1 class="title">Sample title.</h1>
			<div class="maincontent">
				<p>
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed optio repudiandae natus sequi quo quos officia! Quis alias hic, tempore libero placeat quibusdam non asperiores. Sint vitae maxime neque distinctio!
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis fugiat cupiditate, quis modi nemo dolorem itaque magnam facere cum laborum nihil doloribus at minima officia deleniti nostrum eum reiciendis ut.
				</p>
				<!-- Change the image -->
				<img src="./images/sample.jpg" />
			</div>
			<div class="spacel"></div>
			<!-- if you wanna add more content go ahead, add a spacel div + a maincontent one -->
			<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>
