console.log("Sanity check!");

// Get Stripe publishable key
fetch(`${window.location.origin}/config/`)
  .then((result) => { return result.json(); })
  .then((data) => {
    // Initialize Stripe.js with the public key
    const stripe = Stripe(data.publicKey);

    // Event handler for subscribe button
    const subscribeButtons = document.querySelectorAll('.subscribeBtn');
    
    // Loop through all subscribe buttons and add event listeners
    subscribeButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default button action

        const priceId = button.getAttribute('data-price-id'); // Get the price ID for this product
        
        if (priceId) {
          // Create a checkout session
          fetch(`${window.location.origin}/create-checkout-session/?priceId=${priceId}`)
            .then((result) => result.json())
            .then((data) => {
              console.log(data); // Log response data for debugging
              if (data.sessionId) {
                // Redirect to Stripe Checkout with the session ID
                return stripe.redirectToCheckout({ sessionId: data.sessionId });
              } else {
                alert("Error: Failed to create checkout session.");
              }
            })
            .catch((error) => {
              console.error("Error during checkout session creation:", error);
              alert("An error occurred while creating the checkout session.");
            });
        } else {
          alert("Error: No price ID found.");
        }
      });
    });
  })
  .catch((error) => {
    console.error("Error fetching Stripe public key:", error);
  });
