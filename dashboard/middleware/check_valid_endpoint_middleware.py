from django.shortcuts import redirect, render
from django.urls import resolve, reverse
from django.http import Http404, HttpResponseRedirect
from django.http import JsonResponse

class CheckValidEndpointMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ottieni il percorso dell'URL dalla richiesta
        path = request.path_info
        
        try:
            # Controlla se l'URL esiste nel sistema di routing di Django
            resolve(path)
        except Exception:
            # Se l'utente è un admin, mostriamo la lista degli endpoint disponibili
            if request.user.is_authenticated and request.user.is_staff:
                # Mostra la lista degli URL disponibili in formato JSON (solo admin)
                available_urls = self.get_all_urls()
                return redirect(to='core_home')
                #return JsonResponse({'available_urls': available_urls}, status=200)

            # Se l'utente non è admin, mostra 404
            #raise Http404("Page not found")
            #return redirect(reverse('404'))
            return render(request, 'dashboard/pages/samples/error-404.html', status=404)

        # Altrimenti, procedi con la normale gestione della richiesta
        response = self.get_response(request)
        return response

    def get_all_urls(self):
        """
        Recupera tutte le URL del progetto Django (e delle app) configurate nei urls.py.
        """
        from django.urls import get_resolver
        resolver = get_resolver()

        # Otteniamo tutte le URL e le relative viste
        urls = []
        for pattern in resolver.url_patterns:
            if hasattr(pattern, 'pattern'):
                urls.append(str(pattern.pattern))
        return urls
