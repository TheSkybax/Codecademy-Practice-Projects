// The temperature in Kelvin
const kelvin = 0;

// The temperature in Celsius
const celsius = kelvin - 273;

// The temperature in Fahrenheit
let fahrenheit = celsius * (9 / 5) + 32;

// Making it an integer
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${celsius} degrees Celsius`);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit`);

// Extra credit
let newton = Math.floor(celsius * (33 / 100));
console.log(`The temperature is ${newton} degrees Newton`);
