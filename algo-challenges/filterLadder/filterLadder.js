function filterLadder(data, filterProperties) {
    Object.keys(filterProperties).filter(key => {
        return data.filter(d => d[key] === filterProperties[key]);
    });
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
    strength: "B"
};

const result = filterLadder(data, filterProperties);