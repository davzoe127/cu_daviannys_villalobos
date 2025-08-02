//1 
const nombre = "davi";
let edad = 19;
const es_estudiante = true

console.log(`mi nombre es ${nombre}, tengo ${edad} años, y ${es_estudiante}`)

//2
const nombre2 = prompt("ingrese su nombre: ");
let año_nacimiento = Number(prompt("ingrese su año de nacimiento: "));
let edad1 =  2025 - año_nacimiento

console.log(`hola! ${nombre2}, eres del año ${año_nacimiento}, y tienes aproximadamente ${edad1} años`);

//3

let num1 = Number(prompt("ingrese el primer numero:"));
let num2 = Number(prompt("ingrese el segundo numero: "));

let suma = num1 + num2;
let resta = num1 - num2;
let multiplicacion = num1 * num2;
let division = num1 / num2;

console.log(`suma: ${suma} \nresta ${resta} \nmultiplicacion ${multiplicacion} \ndivision ${division}`);

//4

let base_rec = Number(prompt("ingrese el valor de la base: "));
let altura_rec = Number(prompt("inrese el valor de la altura: "));

let area = base_rec * altura_rec;
let perimetro = 2 * (base_rec + altura_rec);

console.log(`el area del rectangulo es: ${area} \nel perimetro del rectangulo es: ${perimetro}`);

// 5

let usuarioedad = Number(prompt("ingrese su edad: "));
let rlaboral = usuarioedad >= 18 && usuarioedad <= 65;

console.log("esta en una edad laboral? (18-65) años", rlaboral);

