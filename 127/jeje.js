let equalPressed = 0;
let buttonInput = document.querySelectorAll(".button");
let input = document.getElementById("input");
let equal= document.getElementById("equal");
let clear = document.getElementById("clear");
let erase = document.getElementById("erase");
let historyContent = document.getElementById("historyContent");

window.onload = () => {
    input.value = "";
}

buttonInput.forEach((buttonClass) => {
    buttonClass.addEventListener("click", (event) => {
        if (equalPressed === 1){
            equalPressed = 0;
        }
    let value = event.target.dataset.number;
    
    if (value === "AC"){
        input.value = "";
        return;
    }

    if (value === "DEL"){
        input.value = input.value.slice(0, -1);
        return;
    }

    input.value += value;


    });
});

equal.addEventListener("click", () => {
    equalPressed = 1;
    let inputValue = input.value;

    try {
        let expression = inputValue
        .replaceAll(/(\d+)\s*(?=cos|sin|tan|sqrt)/g, '$1*')
        .replaceAll("sin", "Math.sin")
        .replaceAll("cos", "Math.cos")
        .replaceAll("tan", "Math.tan")
        .replaceAll("^2", "**2")
        .replaceAll("^3", "**3")
        .replaceAll("√", "Math.sqrt")
        .replaceAll("%", "%")
        .replaceAll("^", "**")
       


        let result = eval(expression);

        if(Number.isNaN(result) || !Number.isFinite(result)){
            throw new Error("Expresión matemática inválida.");
            
        }

        input.value = Number.isInteger(result) ? result : result.toFixed(2);
        addToHistory(expression, input.value);

    } catch (error){
        alert("Error: " + error.message);
    
    }

    });
        function addToHistory(expression, result){
            let divItem = document.createElement("div");
            let span = document.createElement("span");
            let button = document.createElement("button");

            divItem.className = "historyItem";
            divItem.style.display ="flex";
            divItem.style.justifyContent ="space-between";

            span.textContent = `${expression} = ${result}`
            span.dataset.userInput = expression;
            span.style.cursor = "pointer";
            span.style.color = "white";

            button.textContent = "Delete";
            button.className = "btn-sm";
            button.style.backgroundColor = "pink";
            button.style.color = "white";

            button.addEventListener("click", () => divItem.remove());
            span.addEventListener("click", () => {
                input.value = span.dataset.userInput;
            });

            divItem.appendChild(span);
            divItem.appendChild(button);
            historyContent.appendChild(divItem);

}

clear.addEventListener("click", () => {
    input.value = "";

});

erase.addEventListener("click", () => {
    input.value = input.value.slice(0, -1);
});