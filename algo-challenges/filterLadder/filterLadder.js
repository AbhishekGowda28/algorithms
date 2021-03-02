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

const data = [{
    name: "Abhi",
    class: "C",
    strength: "none"
},
{
    name: "Ripple",
    class: "A",
    strength: "A"
},
{
    name: "Wabe",
    class: "A",
    strength: "B"
}];

const filterProperties = {
    class: "A",
    strength: "C"
};

const result = filterLadder(data, filterProperties);

console.log({ result });
