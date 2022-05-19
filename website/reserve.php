<html>
	<head>
		<title>Reserve - PitStop</title>
		<?php include ("./elements/bs4.html"); ?>
        <link rel="stylesheet" href="styles.css" />
        <link rel="stylesheet" type="text/css" media="screen" href="dynamicstyles.php">
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
            <?php
                if (isset ($_GET["reserve"]) && $_GET["reserve"] == "success") {
                        echo "<div class='alert alert-success' role='alert'>Reservation successful!</div>";
                }
            ?>
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
                        <div class="form-group duration">
                            <!-- <label for="duration">Duration (hours)</label> -->
                            <input type="hidden" class="form-control" name="duration" value="1" min="1" max="3" required>
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
                            <form class="rgraphic" action="./backend/reserve2.php" method="post">
                            <input type="hidden" name="date" value="<?php echo $date; ?>" />
                            <input type="hidden" name="time" value="<?php echo $time; ?>" />
                            <input type="hidden" name="duration" value="<?php echo $duration; ?>" />
                            <input type="hidden" name="bin" value="<?php echo $_GET['bin']; ?>" />
                                <?php 
                                    for($cabin = 1; $cabin <= 3; $cabin++) {
                                        if($cabarr[($cabin - 1)]) {
                                            ?>
                                            <div class="rgcabin cabin cabintrue"><p><?php echo "$cabin" ?></p></div>
                                            <?php
                                        } else {
                                            ?>
                                            <input type="submit" class="rgcabin cabin cabinfalse" name="reservedcabin" value="<?php echo "$cabin" ?>">
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
                                                <input type="submit" class="rgmcabin cabin cabinfalse" name="reservedcabin" value="<?php echo "$cabin" ?>">
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
                                    </form>
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
                        <?php
                            if (isset ($_GET['pr'])) {
                                $price = $_GET['pr'];
                                echo "€$price";
                            } else {
                                echo "€0";
                            }
                        ?>
                    </div>
                    <form action="./backend/reserveconfirm.php" method="post">
                        <?php
                            if (isset ($_GET['cb'])) {
                                $rrcabin = $_GET('cb');
                                echo "<input type='hidden' name='cabin' value='$rrcabin' />";
                            }
                        ?>
                        <input type="hidden" name="reserve_date" value="<?php echo $date; ?>" />
                        <input type="hidden" name="reserve_time" value="<?php echo $time; ?>" />
                        <input type="hidden" name="reserve_price" value="<?php echo $price; ?>" />
                        <input type="submit" class="greenbutton" value="Confirm">
                    </form>
                    
                </div>
            </div>
            <div class="spacel"></div>
            <h1 class="title">About the cabins</h1>
            <div class="maincontent">
                <p>
                    There are two types of cabins in the garage, there's the mini ones (cabins number 4, 5 and 6), designed for smaller cars or other types of smaller vehicles, and the jumbo ones (cabins 1, 2 and 3), fully equipped for the most advanced experts and the larger vehicles.
                </p>
                <!-- please change the image -->
                <img src="./images/kenny-eliason-tKvp2XBx4NE-unsplash.jpg" />
            </div>
            <div class="spacel"></div>
            <h1 class="title">The jumbo cabins</h1>
            <div class="maincontent">
                <p>
                    These cabins are 100% equipped to fulfill all your needs, from the most advanced cars to the smallest ones. These rooms are specifically made for bigger cars, but they can be used for smaller ones too if advanced tools are needed. Most cars will fit here, so we recommend these rooms to the average customer.
                </p>
                <!-- please don't ship these versions -->
                <img src="./images/artur-aldyrkhanov-_omYGHPwGEU-unsplash.jpg" />
            </div>
            <div class="spacel"></div>
            <h1 class="title">The mini cabins</h1>
            <div class="maincontent">
                <p>
                    These cabins are meant to be used for motorbikes, small cars, and other smaller vehicles. They are specially designed for them, and they are equipped with more specific tools for these. Most cars will not fit here, so we recommend checking the jumbo cabins first.
                </p>
                <!-- rezad para que ruben no mire el historial del github -->
                <img src="./images/damir-kopezhanov-w-bRrLmXODg-unsplash.jpg" />
            </div>
            <!-- if you wanna add more content go ahead, add a spacel div + a maincontent one -->
            <div class="spacel"></div>
		<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>