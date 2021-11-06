//ex1.
//const a = 1;
//const b = 2;

//console.log(a + b);
//console.log(a - b);
//console.log(a * b);
//console.log(a / b);
//console.log(a % b);

// ex2.
//const a = 1;
//const b = 2;

//if (a > b){
 //   console.log(a);
//}else {
  //  console.log(b);
//}

//ex3.
/*const a = 3;
const b = 23;
const c = 1;

if (a > b && a > c){
   console.log(a);
}else if (a < b && b > c ) {
  console.log(b);
}else {
    console.log(c);
}*/

//ex4.
/*const n = 5;

if (n % 2 === 0){
  console.log("positive");
} else {
  console.log("negative");
}*/

//ex5.
/*const l1 = 60;
const l2 = 50;
const l3 = 60;

if ((l1 + l2 + l3) === 180){
  console.log("triângulo equilatero");
} else {
  console.log("valores inválidos para o triangulo equilatero");
}*/

//ex6. referências para fazer o exercicio https://blog.megajogos.com.br/conheca-as-pecas-do-xadrez/ https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase
let pecaXadrez = "bishop";

if (pecaXadrez.toLowerCase() === "rei"){
  console.log("Pode ser movimentado em qualquer direção do tabuleiro, mas apenas de casa em casa.");
} else if (pecaXadrez.toLowerCase() === "rainha"){
  console.log("Sem restrições, a Rainha tem livre movimentação no jogo na horizontal, vertical e diagonais.");
}else if (pecaXadrez.toLowerCase() === "torre"){
  console.log("pode correr sem restrição de número de casas e em todas as direções (frente, trás, direita, esquerda).");
}else if (pecaXadrez.toLowerCase() === "bispo"){
  console.log("Sem restrição de número de casas, mas somente no sentido diagonal.");
}else if (pecaXadrez.toLowerCase() === "cavalo"){
  console.log("Realiza movimentos em “L”, ou seja, duas casas em um sentido e uma casa em sentido perpendicular àquele, em qualquer direção.");
}else if (pecaXadrez.toLowerCase() === "peao"){
  console.log("Pode apenas realizar movimentos frontais, de forma que o primeiro movimento de cada peão abranja até duas casas, e os demais se limitam a uma casa à frente. O ataque do peão sempre ocorre na diagonal.");
}else {
  console.log("Ops!!Essa peça não é de xadrez, favor escolher uma peça do xadrez válida.")
}