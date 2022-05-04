<html lang="en">
	<head>
		<title>Sign up - uni2</title>
		<?php include "./elements/bs4.html"; ?>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<?php
				if(isset($_GET["signup"])){
					if($_GET["signup"]=="false"){
						?>
						<div class="alert alert-danger" role="alert">
							Can't create account.
						</div>
						<?php
					} elseif ($_GET["signup"]=="true") {
						?>
						<div class="alert alert-success" role="alert">
							Account created.
						</div>
						<?php
					}
				}
				?>
	<body class="signupbody flexv">
		<div class="loginmain">
			<img src="./logow.png" class="loginlogo" />
			<div class="signupsquare">
				<a href="./index.php">&#8592; Back to home</a>
				<h2>Introduce yourself.</h2>
				<form action="./backend/signup.php" method="post">
                    <div class="form-group">
                        <label for="DNI">DNI</label>
                        <input type="text" class="form-control" name="DNI" aria-describedby="DNIHelp" placeholder="Enter DNI" require>
                    </div>
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" class="form-control" name="name" aria-describedby="emailHelp" placeholder="Enter name" require>
                    </div>
                    <div class="form-group">
                        <label for="surname">Surname</label>
                        <input type="text" class="form-control" name="surname" aria-describedby="emailHelp" placeholder="Enter surname" require>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone number</label>
                        <input type="text" class="form-control" name="phone" aria-describedby="emailHelp" placeholder="Enter phone number" require>
                    </div>
					<div class="form-group">
						<label for="email">Email address</label>
						<input type="email" class="form-control" name="email" aria-describedby="emailHelp" placeholder="Enter email" require>
					</div>
					<div class="form-group">
						<label for="password">Password</label>
						<input type="password" class="form-control" name="password" placeholder="Enter password" require>
					</div>
					<button type="submit" class="btn lcbutton">Create account</button>
					&nbsp;
                    <a href="login.php">Log in</a>
				</form>
			</div>
		</div>
	</body>
</html>
