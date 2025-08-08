//1
const nombreProducto = "Tablet 10 pulgadas";
let precio = 450.99;
let stock = 25;
const envioGratis = true;

console.log("Nombre del producto:", nombreProducto);
console.log("Precio:", precio);
console.log("Cantidad en stock:", stock);
console.log("¿Envío gratis?:", envioGratis);

//2
let cantidadComprada = 2;
let subtotal = precio * cantidadComprada;
let impuesto = subtotal * 0.07;
let totalFinal = subtotal + impuesto;

console.log("Subtotal:", subtotal.toFixed(2));
console.log("Total con impuesto:", totalFinal.toFixed(2));

//3
let edadUsuario = 20;

if (edadUsuario >= 18) {
  console.log("Puedes obtener tu licencia de conducir.");  //profe no hicimos estos ya? me habre confundido?
} else {
  console.log("Aún no tienes la edad para obtener la licencia.");
}

//4

let colorSemaforo = "amarillo";

if (colorSemaforo === "verde") {
  console.log("Puede avanzar.");
} else if (colorSemaforo === "amarillo") {
  console.log("precaución.");
} else if (colorSemaforo === "rojo") {
  console.log("detenerse.");
} else {
  console.log("????.");
}

//claro que lo hicimos ya

//5
let diaSemana = 4;

switch (diaSemana) {
  case 1:
    console.log("Lentejas");
    break;
  case 2:
    console.log("Pollo al horno");
    break;
  case 3:
    console.log("Pescado a la plancha");
    break;
  case 4:
    console.log("Pasta");
    break;
  case 5:
    console.log("Paella");
    break;
  default:
    console.log("Día no válido para menú.");
}

//e otro era de ls estaciones xd

//6
for (let i = 2; i <= 20; i += 2) {
  console.log(i);
}
//7
let cuenta = 10;
while (cuenta >= 1) {
  console.log(cuenta);
  cuenta--;
}
console.log("¡Despegue!");

//xdddddddddddd

//8
for (let i = 1; i <= 50; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz"); //buslaiyir
  } else {
    console.log(i);
  }
}

//9

let sumaTotal = 0;
for (let i = 1; i <= 100; i++) {
  sumaTotal += i;
}
console.log("Suma total de 1 a 100:", sumaTotal);

//10

let edad = 19;
let tieneEntrada = false;

if (edad >= 18 && tieneEntrada) {
  console.log("Acceso concedido");
} else {
  console.log("Acceso denegado");
}

edad = 22;
tieneEntrada = true;

if (edad >= 18 && tieneEntrada) {
  console.log("Acceso concedido");
} else {
  console.log("Acceso denegado");
}

//profe de pana que yo loca no ando, esto lo hicimos ya