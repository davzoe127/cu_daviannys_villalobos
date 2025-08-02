//1

let numero = 7;
for (let i = 1; i <= 10; i++){
    console.log(`${numero} * ${i} = ${numero * i}`);
}

// 2
let contador = 10;
console.log("cuenta regresiva");
    while(contador >= 0){
        console.log(contador);
        contador--
    }
    console.log("despega");

// 3
const numeroSecreto = 4;
let intentoUsuario = 0;

console.log("adivina el número secreto");

while (intentoUsuario !== numeroSecreto) {
  intentoUsuario = Math.floor(Math.random() * 10) + 1;
  console.log(`es el ${intentoUsuario}?`);
}

console.log(`que pro, el número secreto era ${numeroSecreto}`);