document.querySelector('.reject').addEventListener

// Fonction pour ouvrir l'onglet sélectionné
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Ouvre le premier onglet par défaut
document.getElementById("Tab1").style.display = "block";

// Attache un gestionnaire d'événement à chaque bouton d'onglet pour appeler la fonction openTab lorsque le bouton est cliqué
var tabButtons = document.querySelectorAll(".tab button");
tabButtons.forEach(function(button) {
    button.addEventListener("click", function(event) {
        openTab(event, this.getAttribute("data-tab")); // Appelle la fonction openTab avec le nom de l'onglet correspondant
    });
});
[23:18]
