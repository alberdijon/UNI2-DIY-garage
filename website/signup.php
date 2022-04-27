<html lang="en">
	<head>
		<title>Sign up - uni2</title>
		<?php include ("./elements/bs4.html"); ?>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body class="signupbody flexv">
		<div class="loginmain">
			<img src="./logo.png" class="loginlogo" />
			<div class="signupsquare">
				<a href="./index.php">&#8592; Back to home</a>
				<h2>Introduce yourself.</h2>
				<form>
                    <div class="form-group">
                        <label for="DNI">DNI</label>
                        <input type="text" class="form-control" id="DNI" aria-describedby="DNIHelp" placeholder="Enter DNI" require>
                    </div>
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Enter name" require>
                    </div>
                    <div class="form-group">
                        <label for="surname">Surname</label>
                        <input type="text" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Enter surname" require>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone number</label>
                        <input type="text" class="form-control" id="phone" aria-describedby="emailHelp" placeholder="Enter phone number" require>
                    </div>
					<div class="form-group">
						<label for="email">Email address</label>
						<input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email" require>
					</div>
					<div class="form-group">
						<label for="password">Password</label>
						<input type="password" class="form-control" id="password" placeholder="Enter password" require>
					</div>
					<button type="submit" class="btn lcbutton">Create account</button>
					&nbsp;
                    <a href="login.php">Log in</a>
				</form>
			</div>
		</div>
	</body>
</html>
