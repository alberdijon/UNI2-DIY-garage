<?php
	function KonektatuDatuBasera() {
			if (!($konexioa=mysqli_connect("192.168.72.34","uni2","uni2"))) {	
				echo "There was an error connecting to the DB.";
				exit();
			} else {
				echo "connected";
			}

			if (!mysqli_select_db($konexioa,"diy_garage")) {	
			echo "There was an error selecting the DB.";
			exit();
			} else {
				echo "selected";
			}
			return $konexioa;
		}
	KonektatuDatuBasera();
?>