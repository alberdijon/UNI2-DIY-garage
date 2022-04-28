<html lang="en">
    <head>
        <link rel="stylesheet" href="./elements/elementstyles.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-sm bg-light navbar-light sticky-top mainnav">
            <a class="navbar-brand" href="./index.php"><img class="navimg" src="./logob.png"></img></a>
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
                        <a class="nav-link" href="">
                            <span class="spanlink">Shop</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./about.php">
                            <span class="spanlink">About</span>
                        </a>
                    </li>
                </ul>
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
                   <?php
                         if(isset($_SESSION['name'])){
                            $user = $_SESSION['name'];
                    ?>

                    <ul class="navbar-nav navbar-right">
                        <li class="nav-item">
                            <a class="nav-link" href="#" id="navbardrop" data-toggle="dropdown">
                                <span class="spanlink">
                                   <?php echo "$user"; ?>
                                </span>
                            </a>
                        </li>
                    <div class="dropdown-menu">
                            <a class="dropdown-item" href="UserProfile.php">My profile</a>
                            <a class="dropdown-item" href="LogOut.php">Log Out</a>
                    </div>

                </li>
                <?php
                    }
                ?>
               
            </div>
        </nav>
    </body>
</html>