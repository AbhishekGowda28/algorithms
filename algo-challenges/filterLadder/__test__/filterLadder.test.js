import { filterLadder } from "../filterLadder";

describe("Filtering of object", () => {
    test("Test 1", () => {

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

        const expected = filterLadder(data, filterProperties);
        const actual = [];
        expect(actual).toStrictEqual(expected);
    });
    test("Test 2", () => {

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
        },
        {
            name: "Another Name",
            class: "A",
            strength: "B"
        }];

        const filterProperties = {
            class: "A",
            strength: "B"
        };

        const expected = filterLadder(data, filterProperties);
        const actual = [{
            name: "Wabe",
            class: "A",
            strength: "B"
        }, {
            name: "Another Name",
            class: "A",
            strength: "B"
        }];
        expect(actual).toStrictEqual(expected);
    });
});