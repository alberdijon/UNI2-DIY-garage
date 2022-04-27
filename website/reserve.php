<html>
	<head>
		<title>uni2</title>
		<?php include ("./elements/bs4.html"); ?>
        <link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<div class="main">
		<?php include ("./elements/navbar.php"); ?>
        <div class="space"></div>
			<h1 class="title">Make a reservation</h1>
            <div class="reservemain">
                <div class="rdatetime">
                    <h3>Date and time</h3>
                    <form>
                        <div class="form-group">
                            <label for="date">Date</label>
                            <input type="date" class="form-control" id="date" require>
                        </div>
                        <div class="form-group">
                            <label for="time">Time</label>
                            <input type="time" class="form-control" id="time" require>
                        </div>
                        <button type="submit" class="btn rdtsubmit">Submit</button>
                    </form>
                </div>
                <div class="rgarage">
                    <h3>Select a cabin</h3>
                    <div class="rgraphic">
                        <div class="rgcabin cabin"><p>1</p></div>
                        <div class="rgcabin cabin"><p>2</p></div>
                        <div class="rgcabin cabin"><p>3</p></div>
                        <div class="rgvcabin">
                            <div class="rgmcabin cabin"><p>4</p></div>
                            <div class="rgmcabin cabin"><p>5</p></div>
                            <div class="rgmcabin cabin"><p>6</p></div>
                        </div>
                    </div>
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