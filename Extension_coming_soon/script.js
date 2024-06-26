// document.querySelector('.reject').addEventListener

// Fonction pour ouvrir l'onglet sélectionné
/*
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

function sendMessage() {
    var userMessage = document.getElementById('userMessage').value;
    if (userMessage.trim() === '') return; // Ne pas envoyer de messages vides

    // Affiche le conteneur de messages et cache la section transaction-info
    document.querySelector('.chatbot-container').style.display = 'block';
    document.querySelector('.transaction-info').style.display = 'none';

    displayMessage('user', userMessage);

    // Ici, vous devriez envoyer 'userMessage' à l'API OpenAI et attendre la réponse
    // Pour le moment, simulez une réponse après un court délai
    setTimeout(function() {
        var openAIResponse = "Ceci est une réponse simulée."; // Simule une réponse de l'API
        displayMessage('bot', openAIResponse);
    }, 1000); // Simule le temps de réponse de l'API

    // Vide le champ de saisie
    document.getElementById('userMessage').value = '';
}

function displayMessage(sender, message) {
    var chatMessages = document.getElementById('chatMessages');
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);

    // Fait défiler vers le bas pour la dernière bulle de message
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Faites apparaître la section 'transaction-info' et cachez 'chatbot-container' au chargement initial de la page
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.transaction-info').style.display = 'block';
    document.querySelector('.chatbot-container').style.display = 'none';
});

// Cette fonction bascule entre l'affichage de la section 'transaction-info' et 'chatbot-container'
function toggleChat(showChat) {
    document.querySelector('.chatbot-container').style.display = showChat ? 'block' : 'none';
    document.querySelector('.transaction-info').style.display = showChat ? 'none' : 'block';
}


function displayMessage(sender, message) {
    var chatMessages = document.getElementById('chatMessages');
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
}

*/

function addMessage(sender, message) {
    // Affiche le conteneur de messages et cache la section transaction-info
    var discussion = document.getElementById('discussion');
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    discussion.appendChild(messageDiv);
}

var texte0 = "";
function callServer(texte, question=true) {
    console.log(texte);
    const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    if (question) {
        var targetUrl = `https://impaktz.pythonanywhere.com/route2/?texte=${texte}&texte0=${texte0}`;
    } else {
        var targetUrl = `https://impaktz.pythonanywhere.com/route1/?texte=${texte}`;
    }
    
    console.log(targetUrl);
    fetch(proxyUrl + targetUrl)
        .then(response => response.text())
        .then(function(data) {
            texte0 = data;
            addMessage("bot", data);
        });
}


function sendMessage() {
    console.log("sendMessage");
    var userMessage = document.getElementById('userMessage').value;
    if (userMessage.trim() === '') return; // Ne pas envoyer de messages vides
    console.log("userMessage : ", userMessage);
    // Vide le champ de saisie
    document.getElementById('userMessage').value = '';
    addMessage("user", userMessage)
    // Ici, vous devriez envoyer 'userMessage' à l'API OpenAI et attendre la réponse
    callServer(userMessage);
}


document.addEventListener('DOMContentLoaded', function () {
    var button = document.getElementById('send-button');
    button.addEventListener('click', function() {
        sendMessage();
    });
    // if enter is pressed when in input userMessage
    var input = document.getElementById('userMessage');
    input.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});