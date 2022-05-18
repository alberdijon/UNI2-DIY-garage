const cabins = [false, false, false, false, false, false];

setSelectable = function (cabin) {
	cabins[cabin - 1] = true;
};

selectCabin = function (cabin) {
	for (let i = 0; i < cabins.length; i++) {
		if (i == cabin - 1) {
			$("#" + cabin).addClass("selected");
		}
	}
};
