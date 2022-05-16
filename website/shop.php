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
				<?php
					if (isset($_GET["purchased"])) {
						if ($_GET["purchased"] == "true") {
							?>
							<div class="alert alert-success" role="alert">
								Purchase successful.
							</div>
							<?php
						} else {
							?>
							<div class="alert alert-danger" role="alert">
								Error adding product to cart.
							</div>
							<?php
						}
					}

					if (isset($_GET["added"])) {
						if ($_GET["added"] == "true") {
							?>
							<div class="alert alert-success" role="alert">
								Product added.
							</div>
							<?php
						} elseif ($_GET["added"] == "false") {
							?>
							<div class="alert alert-danger" role="alert">
								Nice try bro.
							</div>
							<?php
						} else {
							?>
							<div class="alert alert-danger" role="alert">
								Error adding product.
							</div>
							<?php
						}
					}

					if (isset($_GET["deleted"])) {
						if ($_GET["deleted"] == "true") {
							?>
							<div class="alert alert-success" role="alert">
								Product deleted.
							</div>
							<?php
						} else if ($_GET["deleted"] == "false") {
							?>
							<div class="alert alert-danger" role="alert">
								You are not authorized to delete this product.
							</div>
							<?php
						} else {
							?>
							<div class="alert alert-danger" role="alert">
								Error deleting product. Make sure there aren't any orders associated with it.
							</div>
							<?php
						}
					}
				?>
				<div class="tadminoptions">
					<h1 class="title">Shop</h1>
					<?php
					if (isset($_SESSION["userID"])) {
						if($_SESSION['userID'] == "admin"){
							echo '<button onclick="openAddFormS()" class="tadminbutton">Add product</button>';
						}
					}
					?>
				</div>
				<div id="addproduct">
					<div class="admintop">
						<h2 class="admintitle">Add product</h2>
						<button onclick="closeAddFormS()" class="adminclose">Close</button>
					</div>
					<div class="afstructure">
						<form action="backend/sadd.php" method="post" enctype="multipart/form-data">
							<div class="adminform">
								<label for="brand">Brand:</label>
								<input type="text" name="brand" id="brand" required />
							</div>
							<div class="adminform">
								<label for="name">Name:</label>
								<input type="text" name="name" id="name" required />
							</div>
							<div class="adminform">
								<label for="price">Price:</label>
								<input type="number" min="0" name="price" id="price" required />
							</div>
							<div class="adminform">
								<label for="stock">Stock:</label>
								<input type="number" min="0" name="stock" id="stock" required></input>
							</div>
							<div class="adminform">
								<label for="image">Image:</label>
								<input type="file" name="image" id="image" />
							</div>
							<input type="submit" value="Add product" class="adminbutton" />
						</form>
					</div>
					
				</div>
				<div class="sbanner">This shop works by <strong>reserving</strong> items you can later use at the garage. We do <strong>not</strong> ship them.</div>
				<div class="spacel"></div>
				<div class="s2title">
					<h2>Products</h2>
				</div>
				
				<?php
					$link=KonektatuDatuBasera();
					$emaitza=mysqli_query($link,"SELECT * FROM product");
					if(mysqli_num_rows($emaitza)>0) {
						?>
						<div class="products">
							<?php
							while($row = mysqli_fetch_array($emaitza)) {
								?>
								<div class="stcontent">
									<span class="sttext">
										<span class="stbrand"><?php echo $row['Brand']; ?></span>
										<span class="stname"><?php echo $row['Name']; ?></span>
										<?php
										if (isset($_SESSION["userID"])) {
											if($_SESSION['userID'] == "admin"){
												?>
												<div class="staoptions">
													<form action="./backend/sedit.php" method="post">
														<input type="hidden" name="id" value="<?php echo $row['ID']; ?>" />
														<input type="hidden" name="brand" value="<?php echo $row['Brand']; ?>" />
														<input type="hidden" name="name" value="<?php echo $row['Name']; ?>" />
														<input type="hidden" name="price" value="<?php echo $row['Price']; ?>" />
														<input type="hidden" name="stock" value="<?php echo $row['Stock']; ?>" />
														<input type="submit" name="edit" class="material-symbols-outlined staoptionsbutton" value="edit">
													</form>
													<form action="./backend/sdelete.php" method="post">
														<input type="hidden" name="id" value="<?php echo $row['ID']; ?>" />
														<input type="submit" name="delete" class="material-symbols-outlined staoptionsbutton" value="delete" />
													</form>	
												</div>
												<?php
											}
										}
										?>
									</span>
									<span class="stright">
										<span class="stprice"><?php echo $row['Price']; ?>€</span>
										<?php
										if (isset($_SESSION["userID"])) {
											// Buy button
											if ($row['Stock'] != 0) {
												?>
												<form action="./backend/sbuy.php" method="post" class="shopform">
													<input type="number" class="sfamount" min="1" max="<?php echo $row['Stock']; ?>" name="amount" value="1" id="amount" required />
													<input type="hidden" name="ID" value="<?php echo $row['ID']; ?>" />
													<input type="hidden" name="price" value="<?php echo $row['Price']; ?>" />
													<button type="submit" class='stbutton'>Reserve</button>
												</form>
												<?php
											}
											else {
												echo "<a class='stoos'>Out of stock</a>";
											}
										}
											
										// Image
										if ($row['img'] != "") {
											echo "<img src='".$row['Image']."'/>";
										}
										else {
											echo "<img src='./resources/nomedia.png'/>";
										}
										?>
									</span>
								</div>
								<?php
							}
							?>
						</div>
					<?php
						} else {
							?>
							<div class="snoproducts">
								No products found.
							</div>
							<?php
						}
					?>
			<?php include ("./elements/footer.html"); ?>
		</div>
	</body>
</html>