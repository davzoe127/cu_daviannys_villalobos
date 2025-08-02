//1
const edad = 19

if (edad >= 18){
    console.log("eres mayor de edad");
} else {
    console.log("eres menor de edad");
}

//2 
let num1 = 127
let num2 = 1

if(num1 > num2){
    console.log(`el numero ${num1} es mayor que el numero ${num2} `);    
 } else if (num2 > num1) {
    console.log(`el numero ${num2} es mayor que el nuemero ${num1}`);
 } else {
    console.log("son iguales");
 }

 //3
let colorsemaforo = "rojo";

if(colorsemaforo === "verde"){
    console.log("puede cruzar");
} else if (colorsemaforo === "amarillos"){
    console.log("cuidadito");
} else if (colorsemaforo === "rojo"){
    console.log("no puedes cruzar");
} else {
    console.log("color lo valido");
}

//4

let edad1 = 19;
let tieneticket = true;

if (edad1 >= 18 && tieneticket === true){
    console.log("acceso concedido");
} else{
    console.log("acceso denegado");
}

//5

let montocompra = 127
let preciofinal;

if(montocompra > 100){
    preciofinal = montocompra * 0.80;
    console.log("20% desc");
} else if (montocompra > 50){
    preciofinal = montocompra * 0.90;
    console.log("10% desc");
} else {
    preciofinal = montocompra;
    console.log("nada de desc");
}

console.log("el precio final a pagar es $" + preciofinal);