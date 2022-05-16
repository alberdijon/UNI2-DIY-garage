<html>
	<head>
		<title>Reserve - uni2</title>
		<?php include ("./elements/bs4.html"); ?>
        <link rel="stylesheet" href="styles.css" />
	</head>
	<body>
        <?php 
            session_start();
            if(!isset($_SESSION['name'])){
                header("Location: login.php");
            } else {
                $user = $_SESSION['name'];
            }
        ?>
		<div class="main">
		    <?php include ("./elements/navbar.php"); ?>
            <div class="space"></div>
			<h1 class="title">Make a reservation</h1>
            <div class="reservemain">
                <div class="rdatetime">
                    <h3>Date and time</h3>
                    <form action="./backend/reserve.php" method="post">
                        <div class="form-group">
                            <label for="date">Date</label>
                            <input type="date" class="form-control" id="date" require>
                        </div>
                        <div class="form-group">
                            <label for="time">Time</label>
                            <input type="time" step="3600" class="form-control" id="time" require>
                        </div>
                        <div class="form-group">
                            <label for="duration">Duration (hours)</label>
                            <input type="number" class="form-control" id="duration" value="1" min="1" max="3" require>
                        </div>
                        <input type="submit" class="btn rdtsubmit"/>
                    </form>
                </div>
                <div class="rgarage">
                    <h3>Select a cabin</h3>
                    <?php
                        if(isset($_POST['date'])) {
                            $date = $_POST['date'];
                            $time = $_POST['time'];
                            $duration = $_POST['duration'];
                            $link = KonektatuDatuBasera();
                            $sql = "SELECT * FROM cabins WHERE NOT EXISTS (SELECT * FROM cabin-client WHERE cabins.ID = cabin-client.Cabin_ID AND (cabin-client.date = '$date' AND (cabin-client.Hour BETWEEN '$time' AND '$time' + INTERVAL $duration HOUR)))";
                            $result = mysqli_query($link, $sql);
                            
                        }
                    ?>
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
                    <div class="rconfirmprice">
                        0€
                    </div>
                    <button class="greenbutton" type="submit">Confirm</button>
                </div>
            </div>
            <div class="spacel"></div>
            <h1 class="title">About the cabins</h1>
            <div class="maincontent">
                <p>
                    never gonna give you up never gonna let you down never gonna run around and desert you never gonna make you cry never gonna say goodbye never gonna tell a lie and hurt you
                </p>
                <!-- please change the image -->
                <img src="./images/sample.jpg" />
            </div>
            <div class="spacel"></div>
            <h1 class="title">The jumbo cabins</h1>
            <div class="maincontent">
                <p>
                    si necesitas reggaeton dale sigue bailando mami no pares acercate a mi pantalon dale
                </p>
                <!-- please don't ship these versions -->
                <img src="./images/sample.jpg" />
            </div>
            <div class="spacel"></div>
            <h1 class="title">The mini cabins</h1>
            <div class="maincontent">
                <p>
                    jon si lees esto recurda recoger la recompensa diaria del vip
                </p>
                <!-- rezad para que ruben no mire el historial del github -->
                <img src="./images/sample.jpg" />
            </div>
            <!-- if you wanna add more content go ahead, add a spacel div + a maincontent one -->
            <div class="spacel"></div>
		<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>