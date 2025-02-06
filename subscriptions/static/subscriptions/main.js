/*console.log("Sanity check!");

// Get Stripe publishable key
fetch(`${window.location.origin}/config/`)
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler
  let submitBtn = document.querySelector("#submitBtn");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch(`${window.location.origin}/create-checkout-session/`)
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});
*/


console.log("Sanity check!");

// Get the user's current language
const languageCode = document.documentElement.lang || 'en'; // Default to 'en' if no language is set

// Get Stripe publishable key
fetch(`${window.location.origin}/${languageCode}/config/`)
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler for the button click
  let submitBtn = document.querySelector("#submitBtn");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
      // Get Checkout Session ID from the backend
      fetch(`${window.location.origin}/${languageCode}/create-checkout-session/`)
      .then((result) => result.json())
      .then((data) => {
        console.log(data);

        // Verifica che il sessionId sia presente nella risposta
        if (data.sessionId) {
          // Reindirizza all'Checkout di Stripe usando sessionId
          stripe.redirectToCheckout({ sessionId: data.sessionId })
            .then((res) => {
              if (res.error) {
                console.error("Error during redirect: ", res.error.message);
              } else {
                console.log("Successfully redirected to Checkout");
              }
            });
        } else {
          console.error("Session ID non ricevuto dal backend");
        }
      })
      .catch((error) => {
        console.error("Errore durante la creazione della sessione:", error);
      });
    });
  }
});
