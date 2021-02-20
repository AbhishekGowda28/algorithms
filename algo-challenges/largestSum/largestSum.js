function convertFlatArrayInto2DArray(rowCount, columnCount, elements) {
    let counter = 0; arr = [];
    for (let row = 0; row < rowCount; row++) {
        arr[row] = []
        for (let col = 0; col < columnCount; col++) {
            arr[row][col] = elements[counter];
            counter++;
        }
    }
    return arr;
}

function Sum(input1, input2, input3) {
    const array = convertFlatArrayInto2DArray(input1, input2, input3);
    let largestRowSum = 0;
    let largestColumnSum = 0;
    for (let row = 0; row < input1; row++) {
        let interRow = 0;
        for (let col = 0; col < input1; col++) {
            interRow += array[row][col]
        }
        if (interRow > largestRowSum) {
            largestRowSum = interRow;
        }
    }
    for (let col = 0; col < input1; col++) {
        let interCol = 0;
        for (let row = 0; row < input1; row++) {
            interCol += array[row][col]
        }
        if (interCol > largestColumnSum) {
            largestColumnSum = interCol;
        }
    }
    console.log({ largestColumnSum, largestRowSum });
    return largestRowSum + largestColumnSum;
}


const input1 = 2;
const input2 = 2;
const input3 = [1, 2, 5, 6];

const result = Sum(input1, input2, input3);
console.log(result)