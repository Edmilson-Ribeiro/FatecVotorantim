function calcular() {
  let salario = Number(document.getElementById(`salario`).value);
  let aumento = Number(document.getElementById(`aumento`).value);
  salario += (salario * aumento) / 100;
  console.log(salario);
  document.getElementById(
    `salarioNovo`
  ).innerHTML = `O novo salário é ${salario}.`;
}
function calcularArea(){
  let base = Number(document.getElementById(`base`).value);
  let altura = Number(document.getElementById(`altura`).value);
  let area = (base * altura) / 2;
  console.log(area);
  document.getElementById(
    `areaTriangulo`
  ).innerHTML = `A area do triângulo é ${area}.`;
}
