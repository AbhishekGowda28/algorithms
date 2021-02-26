function decimalToBinary(decimal, base) {
    const binaryArray = [];
    while (decimal > 1) {
        const reminder = decimal % base;
        decimal = Number(decimal / base).toFixed(0);
        binaryArray.unshift(reminder);
    }
    binaryArray.unshift(decimal);
    return binaryArray;
}

console.log(decimalToBinary(10, 2));
console.log(decimalToBinary(12, 2));
