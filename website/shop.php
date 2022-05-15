<html>
	<head>
		<title>Shop - uni2</title>
		<?php include ("./elements/bs4.html"); ?>
        <link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<?php session_start();?>
		<div class="main">
			<?php include ("./elements/navbar.php");
				include ("./backend/connect.php");
			?>
				<div class="space"></div>
				<div class="tadminoptions">
					<h1 class="title">Shop</h1>
					<?php
						if($_SESSION['userID'] == "admin"){
							echo '<a href="addproduct.php" class="tadminbutton">Add product</a>';
						}
					?>
				</div>
				<div class="sbanner">This shop works by <strong>reserving</strong> items you can later use at the garage. We do <strong>not</strong> ship them.</div>
				<div class="spacel"></div>
				<h3>Products</h3>
				<?php
					$link=KonektatuDatuBasera();
					$emaitza=mysqli_query($link,"SELECT * FROM product");
					if(mysqli_num_rows($emaitza)>0) {
						?>
						<table>
							<tr class="sttitle">
								<td>ID</td>
								<td>Brand</td>
								<td>Name</td>
								<td>Price</td>
								<td>Stock</td>
								<td>Image</td>
							</tr>
						<?php
						while($row = mysqli_fetch_array($emaitza)) {
							?>
							<tr class="stcontent">
								<td><?php echo $row['ID']; ?></td>
								<td><?php echo $row['Brand']; ?></td>
								<td><?php echo $row['Name']; ?></td>
								<td><?php echo $row['Price']; ?>€</td>
								<td><?php echo $row['Stock']; ?></td>
								<td>
									<?php
										if ($row['img'] != "") {
											echo "<img src='".$row['Image']."' width='100' height='100'/>";
										}
										else {
											echo "No image";
										}
									?>
								</td>
							</tr>
							<?php
						}
						?>
						</table>
					<?php
						} else {
							echo "No products found.";
						}
					?>
			<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>