//let age = 20;
//age = 30;
//let Name = "Hulk";
//const peso = 90;


//console.log(age);
//console.log(Name);
//console.log(peso);

// ------------------------------------------------------------------------- fim aula variáveis

//let movie = "avengers"; //string literal
//let score = 10.89; //number literal
//let isValid = true; //boolean
//let name; //underfined
//let color = null; //variável nula à espera de definição 

//+, -, *, /, **
//let salary = 3500;
//salary++;
//salary--;

//console.log(salary+salary);
//console.log(salary-salary);
//console.log(salary*salary);
//console.log(salary/salary);
//console.log(2**2);

//---------------------------- fim aula tipos primitivos, tipagem dinâmica, operadores aritméticos

// if - se
// else - senão

//let trybe = 14;

//if (trybe >= 14 && trybe < 14.40) {
  //  console.log("Esquenta");
//} else if (trybe >= 16.30 && trybe < 17.50) {
 //   console.log("Aula ao vivo");
//} else if (trybe >= 19.40 && trybe < 20) {
 //   console.log("Fechamento");
//}else{
 //   console.log("Fora dos momentos síncronos");
//}

//------------------------------------------------------ fim aula condições if e else

// OPERADOR AND
//ex1.
const comida = 'pão na chapa';
const bebida = 'cafézinho';

if (bebida === 'cafézinho' && comida === 'pão na chapa') {
  console.log('Muito obrigado pela refeição :)');
} else {
  console.log('Acho que houve um engano com meu pedido');
}

//ex2.
const conditionOne = true;
const conditionTwo = false;

console.log(conditionOne && conditionTwo);

//ex3.
const cenouras = true;
const leite = true;
const arroz = true;
const feijao = true;

const listaDeCompras = cenouras && leite && arroz && feijao;

//ex4.
console.log(true && true); // true
console.log(true && false); // false
console.log(false && true); // false
console.log(false && false); // false

//ex.Final
const currentHour = 15;
let msg = " ";

if (currentHour >= 22) {
    msg = "Não deveríamos comer nada, é hora de dormir";
    console.log(msg);
} else if (currentHour >= 18 && currentHour < 22) {
    msg = "Rango da noite, vamos jantar :D";
    console.log(msg);
} else if (currentHour >= 14 && currentHour < 18) {
    msg = "Vamos fazer um bolo para o café da tarde?";
    console.log(msg);
}else if (currentHour >= 11 && currentHour < 14) {
    msg = "Hora do almoço!!";
    console.log(msg);
}else if (currentHour >= 4 && currentHour < 11){
    console.log("Hmmm, cheiro de café recém passando");
}else {
    console.log(msg);
}

// OPERADOR OR
// ex1.
const bebidaPrincipal =  'cafezinho';
const bebidaAlternativa = 'suco de laranja';

if (bebidaPrincipal === 'cafezinho' || bebidaAlternativa === 'suco de laranja') {
  console.log("Obrigado por me atender :D")
} else {
  console.log("Ei, eu não pedi isso!");
}

//ex2.
console.log(true || true); // true
console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false

//ex.Final
let weekDay = "quarta-feira";

if (weekDay === "segunda-feira" || weekDay === "terca-feira" || weekDay === "quarta-feira" || weekDay === "quinta-feira" || weekDay === "sexta-feira") {
    console.log("Oba, mais um dia de aprendizado na TRYBE!! :D")
  } else {
    console.log("FINALMENTE!! Descanso merecido uuuhuull");
  }

  // OPERADOR NOT
  //ex1.
  console.log((2 + 2) === 4);

  //ex2.
  console.log(!(2 + 2) === 4);

  //ex3.(strings)
  const squirtle = "melhor pokemon inicial";

  console.log(!squirtle); // false

  //ex4.(numeros)
  console.log(!42); // false

  console.log(!0); // true
  // O número 0 tem o valor "falsy" no javascript. Logo, seu oposto é true.

  //ex5.(valores nulos)
  console.log(!null); // true

  //ex6.(valores indefinidos)
  console.log(!undefined); // true

  //------------------------------------------------------ fim aula operadores lógicos
  