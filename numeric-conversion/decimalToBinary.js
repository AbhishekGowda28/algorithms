// @ts-check

/**
 * @param {number} decimal
 * @param {number} base
 */
function decimalToBinary(decimal, base) {
    const binaryArray = [];
    while (decimal > 1) {
        const reminder = decimal % base;
        decimal = Math.floor(decimal / base);
        binaryArray.unshift(reminder);
    }
    binaryArray.unshift(decimal);
    return binaryArray;

}

console.log(10, decimalToBinary(10, 2));
console.log(12, decimalToBinary(12, 2));
