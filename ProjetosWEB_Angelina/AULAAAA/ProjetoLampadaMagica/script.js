let lampada = document.getElementById("lampada");
function ligar()
{
    lampada.src = "luzLigada.gif";
}
function desligar()
{
    lampada.src = "luzDesligada.gif";
}

function aparecer()
{
    lampada.style.display = "inline";
}
function sumir()
{
    lampada.style.display = "none";
    document.getElementById("Titulo").style.color="red"
}
function alternar()
{
    if(lampada.getAttribute("src")=="luzLigada.gif")
    desligar();
    else if(lampada.getAttribute("src")=="luzDesligada.gif")
    ligar();
}
function piscar()
{
    alternar()
}
setInterval(piscar, 500);