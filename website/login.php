<html lang="en">
	<head>
		<title>Log in - PitStop</title>
		<?php include ("./elements/bs4.html"); ?>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<?php
				if(isset($_GET["credentials"])){
					if($_GET["credentials"]=="false"){
						?>
						<div class="alert alert-danger" role="alert">
							Wrong credentials.
						</div>
						<?php
					}
				}
				?>
	<body class="loginbody flexv">
		<div class="loginmain">
			<img src="./logow.png" class="loginlogo" />
			<div class="loginsquare">
				<a href="./index.php">&#8592; Back to home</a>
				<h2>Welcome back.</h2>
				<form action="./backend/login.php" method="post">
					<div class="form-group">
						<label for="email">Email address</label>
						<input type="email" class="form-control" name="email" aria-describedby="emailHelp" placeholder="Enter email" require>
					</div>
					<div class="form-group">
						<label for="password">Password</label>
						<input type="password" class="form-control" name="password" placeholder="Enter password" require>
					</div>
					<button type="submit" class="btn llbutton">Log in</button>
					&nbsp;
					<a href="signup.php">Create an account</a>
				</form>
			</div>
		</div>
	</body>
</html>
