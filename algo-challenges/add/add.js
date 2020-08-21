function add() {
	const arr = Array.from(arguments);
	return arr.reduce((prev, curr) => prev += Number(curr), 0);
}

function addWithSpreadOperator(...params) {
	let sum = 0;
	params.forEach(element => {
		sum += element;
	});

	return Number(sum);
}

module.exports = {
	add,
	addWithSpreadOperator
};
