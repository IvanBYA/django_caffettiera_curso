from .models import Link

# Procesadores de contexto

def context_dict(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context