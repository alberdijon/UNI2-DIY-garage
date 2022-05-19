<html lang="en">
    <head>
        <link rel="stylesheet" href="./elements/elementstyles.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-sm bg-light navbar-light sticky-top mainnav">
            <a class="navbar-brand" href="./index.php"><img class="navimg" src="./logobmini.png"></img></a>
            <button
                class="navbar-toggler"
                type="button"
                data-toggle="collapse"
                data-target="#collapsibleNavbar"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsibleNavbar">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="./index.php"><span class="spanlink">Home</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./reserve.php">
                            <span class="spanlink">Reserve</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./shop.php">
                            <span class="spanlink">Shop</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./about.php">
                            <span class="spanlink">About</span>
                        </a>
                    </li>
                </ul>
                <!-- If the user does not exist, show login/signup -->
                <?php
                if(!isset($_SESSION['name'])){
                ?>
                     <ul class="navbar-nav navbar-right">
                    <li class="nav-item">
                        <a class="nav-link" href="signup.php">
                            <span class="spanlink">Sign up</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="login.php">
                            <span class="spanlink">Log in</span>
                        </a>
                    </li>
                </ul>

                    <?php
                }
                    ?>
                    <!-- If the user does exist, create $user -->
                   <?php
                         if(isset($_SESSION['name'])){
                            $user = $_SESSION['name'];
                    ?>
                    <!-- This should probably be a dropdown -->
                    <!-- However, I don't know how to make it work xd -->
                    <ul class="navbar-nav navbar-right">
                        <li class="nav-item">
                            <a class="nav-link" href="./dashboard.php">
                                <span class="spanlink">
                                    <!-- And display the user instead of the login buttons -->
                                   <?php echo "$user"; ?>
                                </span>
                            </a>
                        </li>
                    </li>
                <?php
                    }
                ?>

            </div>
        </nav>
    </body>
</html>