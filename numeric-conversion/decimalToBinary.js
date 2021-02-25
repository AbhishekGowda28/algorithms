function decimalToBinary(decimal){
    const binaryArray = [];
    while(decimal > 0){
        binaryArray.push(decimal % 2);
        decimal = Number((decimal / 2).toFixedString(0));
    }
    return binaryArray;
} 
