function Sum(input1, input2, input3) {
    let largestRowSum = 0;
    let largestColumnSum = 0;
    for (let row = 0; row < input1; row++) {
        let intermediateRowSum = 0;
        for (let column = row; column < input2; column++) {
            console.log(intermediateRowSum, row, column, input3[row + column]);
            intermediateRowSum += input3[row + column];
        }
        if (intermediateRowSum > largestRowSum) {
            largestRowSum = intermediateRowSum;
        }
    }
    return largestRowSum;
}


const input1 = 2;
const input2 = 2;
const input3 = [1, 2, 5, 6];

const result = Sum(input1, input2, input3);
console.log(result)