//1
let diasemana = Number(prompt("ingrese un numero del 1 a 7:"));

switch (diasemana){
    case 1:
        console.log("es lunes"):
        break;
    case 2:
        console.log("es martes");
        break;
    case 3: 
        console.log("es miercoles");
        break;
    case 4: 
        console.log("es jueves");
        break;
    case 5:
        console.log("es vieernes")
        break;
    case 6:
        console.log("es sabado")
        break;
    case 7:
        console.log("es domingooooooooo");  // preguntar
        break;
}

//2

let opcionmenu = "salir";
    switch(opcionmenu.toUpperCase()) {
        case "INICIAR":
            console.log("comenzo");
            break;

        case "GUARDAR":
            console.log("guardado con exito!");
            break;
        case "SALIR":
            console.log("chau");
            break;
        default:
            console.log("??????");
            break; 
    }

    //3

let mes = prompt("Ingresa el nombre del mes:").toLowerCase();

switch (mes) {
  case "marzo":
  case "abril":
  case "mayo":
    console.log(`El mes ${mes} es de primavera`);
    break;

  case "diciembre":
  case "enero":
  case "febrero":
    console.log(`El mes ${mes} es de invierno`);
    break;

  case "junio":
  case "julio":
  case "agosto":
    console.log(`El mes ${mes} es de verano`);
    break;

  case "septiembre":
  case "octubre":
  case "noviembre":
    console.log(`El mes ${mes} es de otoño`);
    break;

  default:
    console.log("que mes es ese dios");
    break;
}
