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
/*let pecaXadrez = "bishop";

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
}*/

//ex7.
/*const nota = 500;

if (nota <= 100 && nota >= 90){
   console.log("A");
}else if (nota < 90 && nota >= 80 ) {
  console.log("B");
}else if (nota < 80 && nota >= 70 ) {
  console.log("C");
}else if (nota < 70 && nota >= 60 ) {
  console.log("D");
}else if (nota < 60 && nota >= 50 ) {
  console.log("E");
}else if (nota < 50 && nota >= 0) {
  console.log("F");
}else {
    console.log("ERRO!! A nota deve ser um valor entre 0% e 100%.");
}*/

//ex8.
/*const num1 = 1;
const num2 = 5;
const num3 = 6;

if (num1 % 2 === 0 || num2 % 2 === 0 || num3 % 2 === 0){
  console.log("true");
}else{
  console.log("false");
}*/

//ex9.
/*const num1 = 1;
const num2 = 4;
const num3 = 6;

if (num1 % 2 === 1 || num2 % 2 === 1 || num3 % 2 === 1){
  console.log("true");
}else{
  console.log("false");
}*/

//ex10.
/*const vCustoProd = 10;
const vVendaProd = 100;
const vCustoTotal = 10 * (20/100) + 10;
const vLucroProd = vVendaProd - vCustoTotal;
const nVendaProd = 10000;
const lucro = vLucroProd * nVendaProd;

console.log("A empresa terá um lucro de", lucro ,"ao vender dez mil desses produtos");
*/

//ex11.
const salBruto = 3000;
let INSS = 0;
let IR = 0;
let salLiquido = 0;
let salBase = 0;

if (salBruto <= 1556.94){
  INSS = salBruto * (8/100);
}else if (salBruto >= 1556.95 && salBruto <= 2594.92){
  INSS = salBruto * (9/100);
}else if (salBruto >= 2594.93 && salBruto <= 5189.82){
  INSS = salBruto * (11/100);
}else if(salBruto > 5189.82){
  INSS = 570.88;
}
salBase = salBruto - INSS;
console.log(salBase);

if (salBase <= 1903.98){
  IR = 0;
}else if (salBase >= 1903.99 && salBase <= 2826.65){
  IR = salBase * (7.5/100) - 142,80;
}else if (salBase >= 2826.66 && salBase <= 3751.05){
  IR = salBase * (15/100) - 354.80;
}else if (salBase >= 3751.06 && salBase <= 4664.68){
  IR = salBase * (22.5/100) - 636.13;
}else if(salBase > 4664.68){
  IR = salBase * (27.5/100) - 869.36;
}

salLiquido = salBruto - INSS - IR;
console.log("Olá, seu salário líquido será:", salLiquido);
