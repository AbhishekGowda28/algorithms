// import { problem1 } from "./1";
const problem = require("./1");

test("Testing problem 1", () => {
    const result = problem.problem1();
    expect(result).toBe(14);
});