/*let variavel = "valor";*/

/*let pizza1 = "4 queijos";
let pizza2 = "calabresa";
let pizza3 = "frango";

console.log(pizza1, pizza2, pizza3);*/

/*arrays
let pizzas = ["4 queijos", "calabresa", "frango"];

pizzas[4] = "marguerita";
pizzas.push("presunto");

console.log(pizzas.length);
console.log(pizzas);
console.log(pizzas.sort());
console.log(pizzas[0]);

for (let index = o; index < pizzas.length; index++){
    console.log(pizzas[index]);
}
----------------------------------------------------FIM AULA [ARRAYS] */

var numero = 7;
/*
console.log(numero*1);
console.log(numero*2);
console.log(numero*3);
console.log(numero*4);
console.log(numero*5);
console.log(numero*6);
console.log(numero*7);
console.log(numero*8);
console.log(numero*9);*/

for (var contador = 1; contador <= 9; contador++){
    console.log(numero * contador);
}

var listaDeNomes = ["Joana", "Maria", "Lucas"];

for (var indice = 0; indice < listaDeNomes.length; indice++){
    var msg = "boas vindas. " + listaDeNomes[indice] + "!";
    console.log(msg);
}