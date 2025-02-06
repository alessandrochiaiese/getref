 - - [06/Feb/2025:18:24:50 +0000] "GET /en/plans/ HTTP/1.0" 200 1071 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap>
 - - [06/Feb/2025:18:24:52 +0000] "GET /config/ HTTP/1.0" 200 124 "https://affiliate.mydomain.it/en/plans/" "Mozilla/5.>
 - - [06/Feb/2025:18:24:54 +0000] "GET /en/plans/ HTTP/1.0" 200 1071 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap>
 - - [06/Feb/2025:18:24:54 +0000] "GET /config/ HTTP/1.0" 200 124 "https://affiliate.mydomain.it/en/plans/" "Mozilla/5.>
 Internal Server Error: /create-checkout-session/
 Recupero dei prodotti e dei prezzi...
 Tentativo di recuperare i prodotti da Stripe...
 Prodotti recuperati: [{'product_name': 'test', 'product_id': 'prod_QFboJLEdXmstiU', 'price_id': 'price_1PP6aqLA6EOGRbb>
 Price ID selezionato: price_1PP6aqLA6EOGRbboQRdBlx27
 Errore Stripe: Request req_EbIZpCxyF6J7Xl: Not a valid URL
 - - [06/Feb/2025:18:25:00 +0000] "GET /create-checkout-session/ HTTP/1.0" 500 70 "https://affiliate.mydomain.it/en/pla>
 Not Found: /remote/login
 - - [06/Feb/2025:18:31:36 +0000] "GET /remote/login HTTP/1.0" 404 6331 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)>
 - - [06/Feb/2025:18:31:37 +0000] "GET /login HTTP/1.0" 302 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK>
 - - [06/Feb/2025:18:31:38 +0000] "GET /it/login/ HTTP/1.0" 200 6955 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap>
 Not Found: /config/.env
 - - [06/Feb/2025:18:32:08 +0000] "GET /config/.env HTTP/1.0" 404 6328 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; 