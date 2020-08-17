const { getInteger } = require("./utils/Math/getInteger");

function candies(children, numberOfCandies) {
    if (numberOfCandies < children || children === 0) {
        return 0;
    }

    return getInteger(numberOfCandies / children);
}

module.exports = { candies };
