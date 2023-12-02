x = document.getElementById("pesquisaClima");
x.addEventListener("click", async function () {
  cidade = document.getElementById("cidade").value;
  const apiClimaURL = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&units=metric&appid=${apiKey}&lang=pt_br`;
  let respostaClima = await fetch(apiClimaURL);
  let objdados = await respostaClima.json();
  temperatura = objdados.main.temp;
  descricao = objdados.weather[0].description;
  document.getElementById(
    "resultado"
  ).innerText = `Hoje está ${temperatura} e ${descricao}`;
});
let elemento = document.getElementById("pesquisa");
elemento.addEventListener("click", async function () {
  document.getElementById("resultado").innerText = "";
  var valor = document.getElementById("cep").value;
  if (valor == "") alert("Informe o CEP");
  else {
    var cep = valor.replace(/\D/g, "");
    var validacep = /^[0-9]{8}$/;

    if (validacep.test(cep)) {
      var api = "https://viacep.com.br/ws/" + cep + "/json/";
      let resposta = await fetch(api);
      dados = await resposta.json();
      console.log(dados);
      if (dados.erro)
        document.getElementById("resultado").innerText = "CEP Não Existe";
      else {
      }
      document.getElementById("resultado").innerText =
        dados.logradouro + " " + dados.bairro;
      document.getElementById("cidade").value = dados.localidade;
    }
    //if (!(resposta.ok))
    else alert("cep inválido");
  }
});
let apiKey = "e34504cec993c54e1ebdfd6ee4142e6c";
let bandeira = "https://flagsapi.com";
