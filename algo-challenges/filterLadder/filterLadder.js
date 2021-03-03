function filterLadder(data, filterProperties) {
    const keys = Object.keys(filterProperties);
    let dataCollected = [...data];
    keys.forEach((key) => {
        dataCollected = dataCollected.filter(d => {
            return d[key] === filterProperties[key];
        });
    });
    return dataCollected;
}

module.exports = { filterLadder };
