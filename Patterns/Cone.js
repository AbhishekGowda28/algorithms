function Cone(pattern, num) {
    const higherMid = Math.ceil(num / 2);
    let lowerMid = Math.floor(num / 2);
    for (let row = 1; row <= higherMid; row++) {
        let space = "";
        let patterns = "";
        for (let counter = lowerMid; counter > 0; counter--) {
            space += " ";
        }
        for (let count = space.length * 2; count < num; count++) {
            patterns += pattern;
        }
        lowerMid--;
        console.log(space, patterns);
    }
}

Cone("*", 15)

module.exports = Cone;