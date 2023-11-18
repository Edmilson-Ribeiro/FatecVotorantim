let total = 0;
let totalAdicionais;
let totalEntrega;

function calcular() { 
    let combo = Number(document.getElementById("combo").value);
    calcularAdicionais();
    calcularEntrega();
    totalPedido = combo + totalAdicionais + totalEntrega;
    document.getElementById("totalPagar").innerHTML=`R$${totalPedido}`
    document.getElementById("floatingTextarea2Disabled").innerHTML=`Seu combo custará ${combo} com ${totalAdicionais} de adicionais e ${totalEntrega} de taxa de entrega`

    console.log(combo);
    console.log(totalAdicionais);
    console.log(totalEntrega);
    console.log(totalPedido)
}
function calcularAdicionais(){
    totalAdicionais = 0;
    let adicionais = document.querySelectorAll("input[name='adicionais']");
    for (let i = 0; i < adicionais.length; i++){
        if (adicionais[i].checked){
            totalAdicionais = totalAdicionais + Number(adicionais[i].value);
        }
    }
}
function calcularEntrega() {
    let entrega = document.querySelectorAll("input[name='entrega']");
    for (var i = 0; i < entrega.length; i++) {
        if (entrega[i].checked) {
            totalEntrega = Number(entrega[i].value);
            break;
        }
    }
}



    
