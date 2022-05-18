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
                    <!-- FORM START -->
                    <form action="./backend/reserve.php" method="post">
                        <div class="form-group">
                            <label for="date">Date</label>
                            <input type="date" class="form-control" name="date" required>
                        </div>
                        <div class="form-group">
                            <label for="time">Time</label>
                            <input type="time" step="3600" class="form-control" name="time" required>
                        </div>
                        <div class="form-group">
                            <label for="duration">Duration (hours)</label>
                            <input type="number" class="form-control" name="duration" value="1" min="1" max="3" required>
                        </div>
                        <input type="submit" class="btn rdtsubmit"/>
                    </form>
                </div>
                <div class="rgarage">
                    <h3>Select a cabin</h3>
                    <?php
                        if(isset($_GET['bin'])) {
                            $bin = $_GET['bin'];
                            $cabarr = array(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);
                            for ($cabin = 6; $cabin >= 1; $cabin--) {
                                if ($bin >= (pow(2, ($cabin - 1)))) {
                                    $cabarr[($cabin - 1)] = TRUE;
                                    $bin = $bin - (pow(2, ($cabin - 1)));
                                } else {
                                    $cabarr[($cabin - 1)] = FALSE;
                                }
                            }
                            ?>
                            <div class="rgraphic">
                                <?php 
                                    for($cabin = 1; $cabin <= 3; $cabin++) {
                                        if($cabarr[($cabin - 1)]) {
                                            ?>
                                            <div class="rgcabin cabin cabintrue"><p><?php echo "$cabin" ?></p></div>
                                            <?php
                                        } else {
                                            ?>
                                            <div class="rgcabin cabin cabinfalse"><p><?php echo "$cabin" ?></p></div>
                                            <?php
                                        }
                                    }
                                ?>
                            <div class="rgvcabin">
                                <?php
                                    for ($cabin = 4; $cabin <= 6; $cabin++) {
                                        if($cabarr[($cabin - 1)]) {
                                            ?>
                                                <div class="rgmcabin cabin cabintrue"><p><?php echo "$cabin" ?></p></div>
                                            <?php
                                        } else {
                                            ?>
                                            <div class="rgmcabin cabin cabinfalse"><p><?php echo "$cabin" ?></p></div>
                                            <?php
                                        }
                                    }
                                ?>
                            <!-- Legacy (without a loop) -->
                            <!-- <div class="rgcabin cabin"><p>1</p></div>
                            <div class="rgcabin cabin"><p>2</p></div>
                            <div class="rgcabin cabin"><p>3</p></div>
                            <div class="rgvcabin">
                            <div class="rgmcabin cabin"><p>4</p></div>
                            <div class="rgmcabin cabin"><p>5</p></div>
                            <div class="rgmcabin cabin"><p>6</p></div> -->
                        </div>
                    </div>
                    <?php
                        } else {
                            ?>
                            <div class="rgraphic">
                                <h2 class="rgctext">Please select a date and time first.</h2>
                            </div>
                    <?php
                        }
                    ?> 
                    
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
        <script src="./js/reserve.js"></script>
	</body>
</html>