const promoteButtons = document.querySelectorAll('.promote-btn');

promoteButtons.forEach(function(button) {
  button.addEventListener('click', function(event) {
    event.preventDefault(); // Impedisce l'azione predefinita del bottone

    const stripeProductId = button.getAttribute('data-stripe-product-id'); // Ottieni l'ID del prodotto Stripe

    // Richiesta al server per creare una promozione per questo prodotto
    fetch(`${window.location.origin}/create-promotion/?stripeProductId=${stripeProductId}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Errore nella creazione del link promozionale.");
      }
      return response.json();
    })
    .then((data) => {
      if (data.promotionLink) {
        const promotionUrl = `${window.location.origin}/create-checkout-session/?promotionLink=${data.promotionLink}`;
        alert(`Il tuo link promozionale è: ${promotionUrl}`);
      } else {
        alert("Errore: Impossibile creare il link promozionale.");
      }
    })
    .catch((error) => {
      console.error("Errore nella creazione del link promozionale:", error);
      alert("Si è verificato un errore.");
    });
  
  });
});
