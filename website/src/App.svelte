<script>
  import { writable } from 'svelte/store';
  import { BeaconWallet } from "@taquito/beacon-wallet";
  import { NetworkType } from "@airgap/beacon-types";
  import { TezosToolkit } from "@taquito/taquito";

  const rpcUrl = "https://ghostnet.ecadinfra.com";
  const Tezos = new TezosToolkit(rpcUrl);
  const contractAddress = "KT1GoCja6hoW5dEJuXWhVD94o1kKhrDvKQ69";
  

  let wallet;
  let address;

  const currentView = writable('home'); // Gère la vue actuelle

  let create_car_address;
  let add_verified_address;
  let change_owner_address;
  let add_data_address;
  let add_data_text;


  let showChangeOwnerPopup = false;
  const notification = writable('');


  // Fonction pour se connecter au portefeuille
    const connectWallet = async (userType) => {
    const newWallet = new BeaconWallet({
      name: "Simple dApp tutorial",
      network: {
        type: NetworkType.GHOSTNET,
      },
    });

    try {
      await newWallet.requestPermissions();
      address = await newWallet.getPKH();
      wallet = newWallet;
      currentView.set(userType); // Définir la vue en fonction du type d'utilisateur
    } catch (error) {
      console.error('Error during wallet connection:', error);
    }
  };

// Fonction pour se déconnecter
const disconnectWallet = () => {
    if(wallet) {
      wallet.client.clearActiveAccount();
      wallet = undefined;
      address = "";
      currentView.set('home'); // Retourner à la vue "home" après déconnexion
    }
  };
      

const create_car = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .create_car(create_car_address)
    .send();
  create_car_address = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};

const add_verified = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .add_verified(add_verified_address)
    .send();
  add_verified_address = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};

const change_owner = async () => {
    showChangeOwnerPopup = false; // Fermez le popup avant de commencer le processus
    Tezos.setWalletProvider(wallet);
    try {
      const contract = await Tezos.wallet.at(contractAddress);
      const operation = await contract.methods
        .change_owner(change_owner_address)
        .send();
      change_owner_address = "";
      console.log(`Waiting for ${operation.opHash} to be confirmed...`);
      await operation.confirmation(2);
      console.log(`Operation injected: https://ghost.tzstats.com/${operation.opHash}`);
      notification.set('Le propriétaire a été changé avec succès.');
      
      // Faire disparaître la notification après 10 secondes
      setTimeout(() => {
        notification.set('');
      }, 10000);
    } catch (error) {
      console.error('Error during owner change:', error);
      notification.set('Erreur lors du changement de propriétaire.');
      // Gérer également l'affichage de cette erreur à l'utilisateur
    }
  };

const add_data = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .add_data(add_data_address, add_data_text)
    .send();
    add_data_address = "";
    add_data_text = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};

</script>

<main>
  <h1>ImpakTz</h1>

  <div class="card">
    {#if $currentView === 'home'}
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>ImpacTz</title>
    
      <!-- 
        - favicon
      -->
      <link rel="shortcut icon" href="/assets/svelte.svg" type="image/svg+xml">
  
    
      <!-- 
        - google font link
      -->
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link
        href="https://fonts.googleapis.com/css2?family=Mulish:wght@600;700;900&family=Quicksand:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    </head>
    
    <body>
    
      <!-- 
        - HEADER
      -->
    
      <header class="header" data-header>
        <div class="container">
    
          <h1>
            DigitalRoadPass
          </h1>
    
          <button class="menu-toggle-btn" data-nav-toggle-btn>
            <ion-icon name="menu-outline"></ion-icon>
          </button>
    
          <nav class="navbar">
            <ul class="navbar-list">
    
              <li>
                <a href="#hero" class="navbar-link"></a>
              </li>
    
    
              <li>
                <a href="#" class="navbar-link"></a>
              </li>
    
              <li>
                <a href="#contact" class="navbar-link"></a>
              </li>
    
            </ul>
    
            <div class="header-actions">
              <button class="header-action-link" on:click={() => connectWallet('concessionnaire')}>Connexion Concessionnaire</button>
              <a href="#" class="header-action-link" on:click={() => connectWallet('garagiste')}>Connexion Garagiste</a>
              <a href="#" class="header-action-link" on:click={() => connectWallet('proprietaire')}>Connexion Propriétaire</a>
            </div>
          </nav>
    
        </div>
      </header>
    
      <main>
        <article>
    
          <!-- 
            - HERO
          -->
          
    
          <section class="hero" id="hero">
            <div class="container">
    
              <div class="hero-content">
                <h1 class="h1 hero-title">Assurez la transparence et la confiance dans l'achat de votre véhicule d'occasions.</h1>
    
                <p class="hero-text">
                  DigitalRoadPass est un passeport numérique utilisant les NFT pour garantir l'authenticité et l'historique complet de chaque véhicule.
                </p>
    
              </div>
    
              <figure class="hero-banner">
                <img src="https://vusmag.com/wp-content/uploads/2014/05/Fotolia_50766746_Subscription_XXL.jpg" alt="Lolo">
              </figure>
    
            </div>
          </section>
    
    
    
    
    
          <!-- 
            - ABOUT
          -->
    
          <section class="about">
            <div class="container">
    
              <div class="about-content">
    
                <div class="about-icon">
                  <ion-icon name="cube"></ion-icon>
                </div>
    
                <h2 class="h2 about-title">Pourquoi nous ?</h2>
    
                <p class="about-text">
                  Notre équipe est composée d'experts en informatique et en technologie qui ont accumulé des années d'expérience dans l'industrie. Nous sommes passionnés par notre travail et nous nous efforçons de fournir à nos clients les solutions sûres les plus innovantes et les plus efficaces.                </p>
    
                <button class="btn btn-outline">Learn More</button>
    
              </div>
    
              <ul class="about-list">
    
                <li>
                  <div class="about-card">
    
                    <div class="card-icon">
                      <ion-icon name="thumbs-up"></ion-icon>
                    </div>
    
                    <h3 class="h3 card-title">Authenticité et sécurité</h3>
    
                    <p class="card-text">
                      Les NFTs sont uniques et non duplicables, ce qui garanti l'authenticité des informations historiques d'un véhicule et les protéger contre la falsification.                    </p>
    
                  </div>
                </li>
    
                <li>
                  <div class="about-card">
    
                    <div class="card-icon">
                      <ion-icon name="trending-up"></ion-icon>
                    </div>
    
                    <h3 class="h3 card-title">Transferabilité facile 

                    </h3>
    
                    <p class="card-text">
                      La propriété d'un NFT est facilement transférable entre les parties, facilitant le partage sécurisé des informations historiques d'un véhicule lors de la vente.                    </p>
    
                  </div>
                </li>
    
                <li>
                  <div class="about-card">
    
                    <div class="card-icon">
                      <ion-icon name="shield-checkmark"></ion-icon>
                    </div>
    
                    <h3 class="h3 card-title">Transparence accrue</h3>
    
                    <p class="card-text">
                      Les NFTs étant stockés sur une blockchain, toutes les transactions et modifications apportées à l'historique d'un véhicule seraient enregistrées et visibles de manière transparente, renforçant la confiance des acheteurs.
                    </p>
    
                  </div>
                </li>
    
                <li>
                  <div class="about-card">
    
                    <div class="card-icon">
                      <ion-icon name="server"></ion-icon>
                    </div>
    
                    <h3 class="h3 card-title">Partenaires aguérris</h3>
    
                    <p class="card-text">
                      Seuls les garagistes peuvent écrire sur votre NFT, ce qui renforce sa crédibilité
                    </p>
    
                  </div>
                </li>
    
              </ul>
    
            </div>
          </section>
    
    
    
    
    
          <!-- 
            - FEATURES
          -->
  
    
    
    
    
    
          <!-- 
            - CONTACT
          -->
    
          <section class="contact" id="contact">
            <div class="container">
    
              <h2 class="h2 section-title">Besoin d'information ? Contactez-nous</h2>
    
              <p class="section-text">
                Nous vous fournirons une réponse en 48h
              </p>
    
              <div class="contact-wrapper">
    
                <form action="" class="contact-form">
    
                  <div class="wrapper-flex">
    
                    <div class="input-wrapper">
                      <label for="name">Name*</label>
    
                      <input type="text" name="name" id="name" required placeholder="Saisissez votre nom" class="input-field">
                    </div>
    
                    <div class="input-wrapper">
                      <label for="emai">Email*</label>
    
                      <input type="text" name="email" id="email" required placeholder="Saisissez votre adresse email"
                        class="input-field">
                    </div>
    
                  </div>
    
                  <label for="message">Message*</label>
    
                  <textarea name="message" id="message" required placeholder="Votre message :"
                    class="input-field"></textarea>
    
                  <button type="submit" class="btn btn-primary">
                    <span>Envoyer le message</span>
    
                    <ion-icon name="paper-plane-outline"></ion-icon>
                  </button>
    
                </form>
    
                <ul class="contact-list">
    
                  <li>
                    <a href="mailto:support@website.com" class="contact-link">
                      <ion-icon name="mail-outline"></ion-icon>
    
                      <span>: support@website.com</span>
                    </a>
                  </li>
    
                  <li>
                    <a href="#" class="contact-link">
                      <ion-icon name="globe-outline"></ion-icon>
    
                      <span>: www.website.com</span>
                    </a>
                  </li>
    
                  <li>
                    <a href="tel:+0011234567890" class="contact-link">
                      <ion-icon name="call-outline"></ion-icon>
    
                      <span>: (+001) 123 456 7890</span>
                    </a>
                  </li>
    
                  <li>
                    <div class="contact-link">
                      <ion-icon name="time-outline"></ion-icon>
    
                      <span>: 9:00 AM - 6:00 PM</span>
                    </div>
                  </li>
    
                  <li>
                    <a href="#" class="contact-link">
                      <ion-icon name="location-outline"></ion-icon>
    
                      <address>: 1644 Deer Ridge Drive Rochelle Park, NJ 07662</address>
                    </a>
                  </li>
    
                </ul>
    
              </div>
    
            </div>
          </section>
    
        </article>
      </main>
    
    
    
    
    
      <!-- 
        - FOOTER
      -->
    
      <footer>
    
        <div class="footer-bottom">
          <div class="container">
            <p class="copyright">
              &copy; 2024 <a href="">DigitalRoadPass</a>. All Right Reserved
            </p>
          </div>
        </div>
    
      </footer>
    
    
    
    
    
      <!-- 
        - custom js link
      -->
      <script src="./assets/js/script.js"></script>
    
      <!-- 
        - ionicon link
      -->
      <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
      <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
    
    </body>
{/if}
{#if $currentView === 'concessionnaire'}

<header class="header" data-header>
  <div class="container">

    <h1>
      DigitalRoadPass
    </h1>

    <a href="#" class="logo">
      <img src="./assets/images/logo.svg" alt="Landio logo">
    </a>

    <button class="menu-toggle-btn" data-nav-toggle-btn>
      <ion-icon name="menu-outline"></ion-icon>
    </button>

    <nav class="navbar">
      <ul class="navbar-list">

        <li>
          <a href="#hero" class="navbar-link"></a>
        </li>


        <li>
          <a href="#" class="navbar-link"></a>
        </li>

        <li>
          <a href="#contact" class="navbar-link"></a>
        </li>

      </ul>

      <div class="header-actions">
      
        <button class="header-action-link" on:click={disconnectWallet}>Déconnexion</button>
      </div>
    </nav>
  </div>
</header>
<div>
  <div>
    
  
  </div>
</div>
<main class="dataforme flex items-center justify-center min-h-screen bg-ghost-white-1">
  <div class="form-container">
    <input type="text" class="form-input" bind:value={create_car_address}>
    <button class="form-button" on:click={create_car}>Create Car</button>

    <input type="text" class="form-input" bind:value={add_verified_address}>
    <button class="form-button"on:click={add_verified}>Add Verified Account</button>

  </div>
</main>

{/if}

{#if $currentView === 'garagiste'}

<header class="header" data-header>
  <div class="container">

    <h1>
      DigitalRoadPass
    </h1>

    <button class="menu-toggle-btn" data-nav-toggle-btn>
      <ion-icon name="menu-outline"></ion-icon>
    </button>

    <nav class="navbar">
      <ul class="navbar-list">

        <li>
          <a href="#hero" class="navbar-link"></a>
        </li>


        <li>
          <a href="#" class="navbar-link"></a>
        </li>

        <li>
          <a href="#contact" class="navbar-link"></a>
        </li>

      </ul>

      <div class="header-actions">
      
        <button class="header-action-link" on:click={disconnectWallet}>Déconnexion</button>
      </div>
    </nav>
  </div>
</header>
<div>
  <div>
    
  
  </div>
</div>
<main class="dataforme flex items-center justify-center min-h-screen bg-ghost-white-1">
  <div class="form-container">
    <label class="form-label" for="add_data_address">Adresse</label>
    <input class="form-input" type="text" id="add_data_address" bind:value={add_data_address} placeholder="Entrez l'adresse" />

    <label class="form-label" for="add_data_text">Exemple de donnée textuelle</label>
    <input class="form-input" type="text" id="add_data_text" bind:value={add_data_text} placeholder="Entrez les données" />

    <button class="form-button" on:click={add_data}>
      Ajouter des données
    </button>
  </div>
</main>

{/if}

<script>
  let change_owner_address = '';
  let showChangeOwnerPopup = false;
  let notification = '';

  function change_owner() {
    // Implémentez la logique de changement de propriétaire ici...
    // Par exemple, envoyez les données à une API ou mettez à jour les données localement

    notification = 'Le propriétaire a été changé avec succès.';
    showChangeOwnerPopup = false; // Fermer le pop-up après le changement

    // Faire disparaître la notification après 10 secondes
    setTimeout(() => {
      notification = '';
    }, 10000);
  }
</script>

{#if $currentView === 'proprietaire'}

// Place this script tag before your closing tag
<script>
  // Wait for the entire content to load
  document.addEventListener('DOMContentLoaded', (event) => {
    // Function to toggle accordion content
    function toggleAccordion(accordionHeader) {
      // Add 'active' class to header
      accordionHeader.classList.toggle('active');
      // Toggle visibility of the next sibling element
      const content = accordionHeader.nextElementSibling;
      content.classList.toggle('hidden');
      content.style.maxHeight = content.style.maxHeight ? null : content.scrollHeight + 'px';
    }

    // Attach click event listener to accordion headers
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(accordion => {
      accordion.onclick = () => toggleAccordion(accordion);
    });
  });
</script>


<header class="header" data-header>
  <div class="container">

    <h1>
      DigitalRoadPass
    </h1>

    <button class="menu-toggle-btn" data-nav-toggle-btn>
      <ion-icon name="menu-outline"></ion-icon>
    </button>

    <nav class="navbar">
      <ul class="navbar-list">

        <li>
          <a href="#hero" class="navbar-link"></a>
        </li>


        <li>
          <a href="#" class="navbar-link"></a>
        </li>

        <li>
          <a href="#contact" class="navbar-link"></a>
        </li>

      </ul>

      <div class="header-actions">
        <button class="header-action-link" on:click={() => showChangeOwnerPopup = true}>
          Changer de propriétaire du véhicule
        </button>
          <!-- Pop-up de changement de propriétaire -->
            <!-- Popup pour le changement de propriétaire -->
            {#if showChangeOwnerPopup}
            <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-10">
              <div class="bg-white p-4 rounded-lg shadow-lg">
                <input type="text" bind:value={change_owner_address} placeholder="Nouvelle adresse du propriétaire">
                <button on:click={change_owner}>Changer propriétaire</button>
              </div>
            </div>
            {/if}
        <button class="header-action-link" on:click={disconnectWallet}>Déconnexion</button>
      </div>
    </nav>
  </div>
</header>

<main class="flex items-center justify-center min-h-screen bg-ghost-white-1 mt-marge">
  <div class="container mx-auto px-4 sm:px-8 max-w-3xl">
    <header class="text-center mb-12">
      <h1 class="text-4xl font-bold text-independence">Historique de la voiture</h1>
    </header>
    
    <div class="accordion" id="history-accordion">
      <!-- Accordion item -->
      <div class="bg-white rounded-lg shadow-md mb-5">
        <div class="p-5 border-b">
          <h2 class="font-bold text-lg text-independence">
            <button class="accordion-header focus:outline-none w-full text-left">
              01/01/2021 - Garage Dupont
              <span class="float-right">
                <ion-icon name="chevron-down-outline"></ion-icon>
              </span>
            </button>
          </h2>
          <div class="accordion-content hidden">
            <div class="mt-4">
              <p>Changement des pneus</p>
            </div>
          </div>
        </div>
      </div>
      <br>
      <div class="bg-white rounded-lg shadow-md mb-5">
        <div class="p-5 border-b">
          <h2 class="font-bold text-lg text-independence">
            <button class="accordion-header focus:outline-none w-full text-left">
              01/01/2021 - Garage Dupont
              <span class="float-right">
                <ion-icon name="chevron-down-outline"></ion-icon>
              </span>
            </button>
          </h2>
          <div class="accordion-content hidden">
            <div class="mt-4">
              <p>Changement des pneus</p>
            </div>
          </div>
        </div>
      </div>
      <br>
      <div class="bg-white rounded-lg shadow-md mb-5">
        <div class="p-5 border-b">
          <h2 class="font-bold text-lg text-independence">
            <button class="accordion-header focus:outline-none w-full text-left">
              01/01/2021 - Garage Dupont
              <span class="float-right">
                <ion-icon name="chevron-down-outline"></ion-icon>
              </span>
            </button>
          </h2>
          <div class="accordion-content hidden">
            <div class="mt-4">
              <p>Changement des pneus</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Repeat for other accordion items -->
    </div>
  </div>
</main>

{/if}



  </div>
</main>




<style>

.main {
  display: flex;
  flex-direction: column; /* Stack children vertically */
  justify-content: center; /* Center vertically */
  align-items: center; /* Center horizontally */
  min-height: 100vh; /* Full height of the viewport */
  background: var(--ghost-white-1);
}

.container {
  max-width: 3xl; /* Or any specific width */
  margin: 0 auto; /* Center in the available horizontal space */
}


.hero-banner img {
  border-radius: 20px; /* Adjust the pixel value to the desired radius */
}


  /* Ajoutez ceci dans votre balise de style existante */
  .form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem; /* Plus de padding pour un bloc plus grand */
  max-width: 600px; /* Largeur maximale ajustée pour un bloc plus grand */
  width: 100%; /* Utilisez toute la largeur possible jusqu'à max-width */
  margin: auto; /* Centre horizontalement */
  box-sizing: border-box; /* S'assure que padding est inclus dans la largeur */
  background: var(--white);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: relative; /* Positionnement relatif pour z-index fonctionne */
  z-index: 10; /* S'assure que le formulaire est au-dessus du fond */
}

.dataforme{

  display: flex; /* Utilise flexbox pour le centrage */
  align-items: center; /* Centre verticalement */
  justify-content: center; /* Centre horizontalement */
  min-height: 100vh; /* Hauteur minimale de la fenêtre de visualisation */
  background: var(--ghost-white-1); /* Couleur de fond */
  padding: 0; /* Pas de padding */
  margin: 0; /* Pas de marges externes */
  box-sizing: border-box; /* S'assure que padding et border sont inclus dans la largeur et hauteur */

}
  .form-input {
    background: var(--ghost-white-2);
    border: 1px solid var(--cool-gray);
    border-radius: 0.25rem;
    margin-bottom: 1rem;
    padding: 0.5rem 1rem;
  }

  .form-input:focus {
    outline: none;
    border-color: var(--majorelle-blue);
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.5); /* Ajoutez un halo de focus */
  }

  .form-button {
  background-color: var(--majorelle-blue);
  color: var(--white);
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  font-weight: var(--fw-700);
  text-transform: uppercase; /* Optionnel */
  cursor: pointer;
  border: none;
  transition: background-color 0.3s; /* Transition pour un changement de couleur en douceur */
}

/* Si vous voulez conserver un effet au survol mais pas blanc, assurez-vous que la couleur est correctement définie */
.form-button:hover {
  background-color: var(--majorelle-blue); /* Gardez la même couleur au survol */
}

  .form-label {
    text-align: left;
    width: 100%;
    color: var(--independence);
    margin-bottom: 0.5rem;
  }

:root {

/**
 * colors
 */

--raisin-black-2: hsl(245, 16%, 16%);
--raisin-black-1: hsl(244, 17%, 19%);
--majorelle-blue: hsl(245, 67%, 59%);
--ghost-white-1: hsl(240, 100%, 99%);
--ghost-white-2: hsl(228, 50%, 96%);
--white-opacity: hsla(0, 0%, 100%, 0.5);
--independence: hsl(245, 17%, 27%);
--lavender-web: hsl(247, 69%, 95%);
--eerie-black: hsl(210, 11%, 15%);
--cool-gray: hsl(244, 17%, 61%);
--sapphire: hsl(211, 100%, 35%);
--white: hsl(0, 0%, 100%);

/**
 * typography
 */

--ff-quicksand: "Quicksand", sans-serif;
--ff-mulish: "Mulish", sans-serif;

--fs-1: 36px;
--fs-2: 28px;
--fs-3: 20px;
--fs-4: 17px;
--fs-5: 16px;
--fs-6: 15px;
--fs-7: 14px;

--fw-500: 500;
--fw-600: 600;
--fw-700: 700;

/**
 * transition
 */

--transition: 0.25s ease;

/**
 * spacing
 */

--section-padding: 80px;

}





/*-----------------------------------*\
#RESET
\*-----------------------------------*/

*, *::before, *::after {
margin: 0;
padding: 0;
box-sizing: border-box;
}

li { list-style: none; }

a { text-decoration: none; }

a,
img,
span,
input,
label,
button,
ion-icon,
textarea { display: block; }

button {
border: none;
background: none;
font: inherit;
cursor: pointer;
}

input,
textarea {
border: none;
font: inherit;
width: 100%;
}

html {
font-family: var(--ff-quicksand);
scroll-behavior: smooth;
}

body { background: var(--white); }





/*-----------------------------------*\
#REUSED STYLE
\*-----------------------------------*/


.container { padding-inline: 15px; }

.h1,
.h2,
.h3 {
color: var(--independence);
font-family: var(--ff-mulish);
line-height: 1.2;
}

.h1 { font-size: var(--fs-1); }

.h2 { font-size: var(--fs-2); }

.h3 { font-size: var(--fs-3); }

.btn {
font-size: var(--fs-6);
font-weight: var(--fw-700);
padding: 15px 30px;
border-radius: 4px;
transition: var(--transition);
}

.btn:is(:hover, :focus) { transform: translateY(-2px); }

.btn-primary {
background: var(--majorelle-blue);
color: var(--white);
}

.btn-primary:is(:hover, :focus) {
--majorelle-blue: hsl(245, 67%, 55%);
box-shadow: 0 3px 10px hsla(245, 67%, 59%, 0.5);
}

.btn-outline { 
border: 1px solid var(--majorelle-blue);
color: var(--majorelle-blue);
}

.btn-outline:is(:hover, :focus) {
background: var(--majorelle-blue);
color: var(--white);
box-shadow: 0 3px 10px hsla(245, 67%, 59%, 0.5);
}

.btn-secondary {
background: hsla(245, 67%, 59%, 0.15);
color: var(--majorelle-blue);
}

.section-title { text-align: center; }

.section-text {
color: var(--cool-gray);
font-size: var(--fs-6);
line-height: 1.7;
text-align: center;
}





/*-----------------------------------*\
#HEADER
\*-----------------------------------*/

.header {
position: fixed;
top: 0;
left: 0;
width: 100%;
background: var(--white);
padding-block: 20px;
box-shadow: 0 1px 2px hsla(0, 0%, 0%, 0.05);
height: 65px;
overflow: hidden;
transition: 0.5s ease-in-out;
z-index: 4;
}

.header.active { height: 330px; }

.header .container {
display: flex;
justify-content: space-between;
align-items: center;
}

.menu-toggle-btn { font-size: 25px; }

.navbar {
position: absolute;
width: 100%;
top: 64px;
left: 0;
padding-inline: 30px;
visibility: hidden;
opacity: 0;
transition: 0.5s ease-in-out;
}

.header.active .navbar {
visibility: visible;
opacity: 1;
}

.navbar-link,
.header-action-link {
color: var(--cool-gray);
font-size: var(--fs-6);
font-family: var(--ff-mulish);
padding-block: 8px;
}

:is(.navbar-link, .header-action-link):is(:hover, :focus) { color: var(--majorelle-blue); }





/*-----------------------------------*\
#HERO
\*-----------------------------------*/

.hero {
padding: 125px 0 var(--section-padding);
background: var(--ghost-white-1);
}

.hero-content { margin-bottom: 80px; }

.hero-title { margin-bottom: 25px; }

.hero-text {
color: var(--cool-gray);
font-size: var(--fs-4);
font-weight: var(--fw-500);
line-height: 1.8;
margin-bottom: 40px;
}

.form-text {
color: var(--independence);
font-weight: var(--fw-500);
line-height: 1.8;
margin-bottom: 20px;
}

.form-text span {
display: inline-block;
font-size: 20px;
}

.email-field {
background: var(--ghost-white-2);
padding: 17px 20px;
border-radius: 8px;
margin-bottom: 20px;
}

.email-field:focus { outline-color: var(--majorelle-blue); }

.hero .btn-primary { margin-inline: auto; }

.hero-banner img { width: 100%; }





/*-----------------------------------*\
#ABOUT
\*-----------------------------------*/

.about { padding-block: var(--section-padding); }

.about-content { margin-bottom: 30px; }

.about-icon {
width: 60px;
height: 60px;
background: var(--lavender-web);
display: grid;
place-items: center;
color: var(--majorelle-blue);
font-size: 40px;
border-radius: 4px;
margin-bottom: 20px;
}

.about-title { margin-bottom: 10px; }

.about-text {
color: var(--cool-gray);
font-weight: var(--fw-500);
line-height: 1.8;
margin-bottom: 20px;
}

.about-list {
display: grid;
gap: 20px;
}

.about-card {
padding: 20px;
text-align: center;
box-shadow: 0 3px 12px hsla(233, 77%, 10%, 0.06);
border-radius: 4px;
transition: var(--transition);
}

.about-card:hover {
background: var(--majorelle-blue);
transform: translateY(-5px);
box-shadow: 0 5px 18px hsla(245, 67%, 59%, 0.4);
}

.about-card .card-icon {
width: 60px;
height: 60px;
background: var(--lavender-web);
display: grid;
place-items: center;
color: var(--majorelle-blue);
font-size: 28px;
border-radius: 50%;
margin-inline: auto;
margin-bottom: 20px;
transition: var(--transition);
}

.about-card:hover .card-icon {
background: hsla(0, 0%, 100%, 0.15);
color: var(--white);
box-shadow: 0 0 0 8px hsla(0, 0%, 100%, 0.05);
}

.about-card .card-title {
margin-bottom: 10px;
transition: var(--transition);
}

.about-card:hover .card-title { color: var(--white); }

.about-card .card-text {
color: var(--cool-gray);
font-size: var(--fs-6);
font-weight: var(--fw-500);
line-height: 1.8;
transition: var(--transition);
}

.about-card:hover .card-text { color: hsla(0, 0%, 100%, 0.5); }





/*-----------------------------------*\
#FEATURES
\*-----------------------------------*/

.features {
padding-block: var(--section-padding);
background: var(--ghost-white-1);
}

.features .section-title { margin-bottom: 15px; }

.features .section-text { margin-bottom: 60px; }

.features-wrapper:not(:last-child) { margin-bottom: 80px; }

.features-banner { margin-bottom: 35px; }

.features-banner img { width: 100%; }

.features-content-subtitle {
display: flex;
align-items: center;
gap: 10px;
font-size: var(--fs-5);
color: var(--eerie-black);
margin-bottom: 20px;
}

.features-content-subtitle ion-icon {
color: var(--majorelle-blue);
font-size: 20px;
}

.features-content-title {
font-size: var(--fs-2);
font-family: var(--ff-mulish);
color: var(--independence);
font-weight: var(--fw-600);
margin-bottom: 25px;
}

.features-content-title strong { font-weight: var(--fw-700); }

.features-content-text {
font-size: var(--fs-6);
color: var(--cool-gray);
line-height: 1.7;
margin-bottom: 25px;
}

.features-list { margin-bottom: 40px; }

.features-list-item {
display: flex;
align-items: flex-start;
gap: 5px;
font-size: var(--fs-5);
color: var(--cool-gray);
margin-bottom: 10px;
}

.features-list-item ion-icon { font-size: 23px; }

.features-list-item p { width: calc(100% - 28px); }

.features-wrapper:last-child {
display: flex;
flex-direction: column-reverse;
}

.btn-group {
display: flex;
flex-wrap: wrap;
justify-content: flex-start;
align-items: flex-start;
gap: 10px;
}





/*-----------------------------------*\
#BLOG
\*-----------------------------------*/

.blog { padding-block: var(--section-padding); }

.blog .section-title { margin-bottom: 20px; }

.blog .section-text { margin-bottom: 40px; }

.blog-list {
display: grid;
gap: 30px;
}

.blog-banner { margin-bottom: 20px; }

.blog-banner img {
width: 100%;
height: 100%;
object-fit: cover;
border-radius: 4px;
}

.blog-meta {
display: flex;
justify-content: flex-start;
align-items: center;
gap: 20px;
font-size: var(--fs-6);
text-transform: uppercase;
color: var(--cool-gray);
margin-bottom: 10px;
}

.blog-meta span {
display: flex;
align-items: center;
gap: 5px;
}

.blog-title {
font-size: var(--fs-3);
color: var(--independence);
}

.blog-text {
color: var(--cool-gray);
font-size: var(--fs-6);
line-height: 1.7;
margin-bottom: 15px;
}

.blog-link-btn {
display: flex;
align-items: center;
gap: 5px;
color: var(--majorelle-blue);
font-weight: var(--fw-600);
}

.blog-link-btn:is(:hover, :focus) { color: var(--sapphire); }





/*-----------------------------------*\
#CONTACT
\*-----------------------------------*/

.contact {
padding-block: var(--section-padding);
background: var(--ghost-white-1);
}

.contact .section-title { margin-bottom: 15px; }

.contact .section-text { margin-bottom: 60px; }

.contact-form { margin-bottom: 50px; }

.input-wrapper { margin-bottom: 20px; }

.contact label {
color: var(--independence);
font-weight: var(--fw-500);
margin-bottom: 10px;
}

.contact .input-field {
background: transparent;
color: var(--independence);
font-size: var(--fs-7);
padding: 10px 15px;
border: 1px solid hsla(244, 17%, 67%, 0.3);
border-radius: 4px;
}

.contact .input-field:focus {
outline: none;
background: var(--ghost-white-2);
}

.contact .input-field::placeholder { color: var(--cool-gray); }

textarea.input-field {
margin-bottom: 20px;
resize: vertical;
min-height: 50px;
height: 100px;
max-height: 200px;
}

.contact .btn-primary {
display: flex;
justify-content: center;
align-items: center;
gap: 10px;
}

.contact .btn-primary ion-icon { --ionicon-stroke-width: 40px; }

.contact-list li:not(:last-child) { margin-bottom: 25px; }

.contact-link {
color: var(--cool-gray);
font-weight: var(--fw-500);
display: flex;
justify-content: flex-start;
align-items: flex-start;
gap: 5px;
}

.contact-link ion-icon {
font-size: 20px;
--ionicon-stroke-width: 30px;
}

.contact-link :is(span, address) { width: calc(100% - 25px); }

.contact-link address { font-style: normal; }





/*-----------------------------------*\
#FOOTER
\*-----------------------------------*/

footer {
background: var(--raisin-black-1);
color: var(--white-opacity);
font-weight: var(--fw-500);
}

.footer-top { padding-block: var(--section-padding); }

.footer-brand { margin-bottom: 60px; }

footer .logo { margin-bottom: 25px; }

.footer-text {
font-size: var(--fs-6);
line-height: 1.8;
margin-bottom: 25px;
}

.social-list {
display: flex;
justify-content: flex-start;
align-items: center;
gap: 20px;
}

.social-link {
color: var(--white-opacity);
font-size: 25px;
transition: var(--transition);
}

.social-link:is(:hover, :focus) { color: var(--white); }

.footer-link-box {
display: grid;
gap: 50px;
}

.footer-list li:first-child { margin-bottom: 20px; }

.footer-item-title {
color: var(--white);
font-family: var(--ff-mulish);
font-weight: var(--fw-700);
}

.footer-link {
color: var(--white-opacity);
font-size: var(--fs-6);
transition: var(--transition);
padding-block: 10px;
}

.footer-link:is(:hover, :focus) {
color: var(--white);
transform: translateX(5px);
}

.footer-bottom {
background: var(--raisin-black-2);
padding-block: 20px;
text-align: center;
}

.copyright a {
display: inline-block;
color: var(--white-opacity);
transition: var(--transition);
}

.copyright a:is(:hover, :focus) { color: var(--white); }





/*-----------------------------------*\
#MEDIA QUERIES
\*-----------------------------------*/

/**
* responsive for larger than 450px screen
*/

@media (min-width: 450px) {

/**
 * HERO
 */

.hero-form { position: relative; }

.email-field {
  margin-bottom: 0;
  padding-right: 155px;
}

.hero .btn-primary {
  position: absolute;
  top: 5px;
  right: 5px;
  padding-block: 12.5px;
}



/**
 * ABOUT
 */

.about-card .card-text {
  max-width: 300px;
  margin-inline: auto;
}

}





/**
* responsive for larger than 576px screen
*/

@media (min-width: 576px) {

/**
 * CUSTOM PROPERTY
 */

:root {

  /**
   * typography
   */

  --fs-1: 52px;

}



/**
 * REUSED STYLE
 */

.container {
  max-width: 525px;
  margin-inline: auto;
  width: auto; /* Adjust width as necessary */
  margin: 0 auto; /* Auto margins for horizontal centering */
}

.section-text {
  max-width: 460px;
  margin-inline: auto;
  margin-bottom: 80px;
}

}





/**
* responsive for larger than 768px screen
*/

@media (min-width: 768px) {

/**
 * REUSED STYLE
 */

.container { max-width: 720px; }

.section-text { max-width: 645px; }



/**
 * HERO
 */

.hero :is(.hero-text, .form-text, .hero-form) { max-width: 520px; }

.hero-banner {
  max-width: 600px;
  margin-inline: auto;
}



/**
 * ABOUT
 */

.about-list { grid-template-columns: 1fr 1fr; }



/**
 * CONTACT
 */

.contact-form .wrapper-flex {
  display: flex;
  gap: 30px;
}

.wrapper-flex .input-wrapper { width: 50%; }



/**
 * FOOTER
 */

.footer-link-box { grid-template-columns: repeat(3, 1fr); }

}





/**
* responsive for larger than 992px screen
*/

@media (min-width: 992px) {

/**
 * REUSED STYLE
 */

.container { max-width: 950px; }

.section-text { max-width: 450px; }



/**
 * HEADER
 */

.header {
  overflow: visible;
  padding-block: 0;
  height: unset;
}

.header.active { height: unset; }

.menu-toggle-btn { display: none; }

.navbar {
  position: static;
  visibility: visible;
  opacity: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-inline: 0;
}

.navbar-list {
  display: flex;
  justify-content: center;
  align-items: center;
  width: max-content;
  gap: 40px;
  margin-inline: auto;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 40px;
}

.navbar-link,
.header-action-link { padding-block: 25px; }



/**
 * HERO
 */

.hero .container {
  display: grid;
  grid-template-columns: 4fr 5fr;
  align-items: center;
  gap: 60px;
}

.hero-content { margin-bottom: 0; }



/**
 * ABOUT
 */

.about .container {
  display: flex;
  align-items: center;
  gap: 50px;
}

.about-content {
  margin-bottom: 0;
  width: 40%;
}

.about-list {
  gap: 30px;
  padding-bottom: 50px;
}

.about-list li:nth-child(odd) { transform: translateY(50px); }



/**
 * FEATURES
 */

.features-wrapper {
  display: grid !important;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: 90px;
}

.features-wrapper:not(:last-child) { margin-bottom: 100px; }

.features-wrapper:last-child .features-banner {
  grid-column: 2 / 3;
  grid-row: 1 / 2;
}



/**
 * BLOG
 */

.blog-list { grid-template-columns: repeat(3, 1fr); }

.blog .section-text { margin-bottom: 50px; }



/**
 * CONTACT
 */

.contact-wrapper {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 80px;
  align-items: center;
}

.contact-form { margin-bottom: 0; }



/**
 * FOOTER
 */

.footer-top .container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 50px;
}

.footer-brand {
  margin-bottom: 0;
  max-width: 300px;
}

.footer-list { width: 140px; }

}





/**
* responsive for larger than 1200px screen
*/

@media (min-width: 1200px) {

/**
 * REUSED STYLE
 */

.container { max-width: 1150px; }



/**
 * HERO
 */

.hero .container { gap: 150px; }



/**
 * FOOTER
 */

.footer-link-box { margin-right: 40px; }

.footer-list { width: 170px; }

}

.accordion-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: var(--ghost-white-2);
  border: none;
  width: 100%;
  text-align: left;
  border-radius: 0.25rem;
}


.accordion-header.active + .accordion-content {
  display: block;
}

.accordion-header:hover,
.accordion-header:focus {
  background: var(--lavender-web);
}

/* Ion-icons styling */
ion-icon {
  font-size: 1.5rem;
}

/* Afficher le contenu de l'accordéon lorsque l'en-tête est cliqué */
.accordion-header.active + .accordion-content {
  display: block;
}

/* Additional styles for layout */
.main-layout {
  display: flex;
  justify-content: space-evenly; /* Distribute space evenly between the children */
  align-items: center; /* Align children vertically */
  min-height: 100vh; /* Full viewport height */
}

.content-center {
  flex-grow: 2; /* Allow this element to grow and take up more space */
  /* Your existing styles for this content */
}

aside {
  flex-grow: 1; /* Take up less space than the central content */
  /* Style for the aside elements */
}

/* Make sure the accordion content has a transition */
.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
}

/* When accordion content is not hidden, we want to display it with a smooth transition */
.accordion-content:not(.hidden) {
  max-height: 500px; /* Adjust as necessary */
}

.mt-large {
  margin-top: 4rem; /* Ou la valeur que vous souhaitez pour 'grosse marge' */
}



</style>
