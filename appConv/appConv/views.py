from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse

 
def error_404_view(request, exception):  
    return render(request, 'errors/404.html', status=404)

def error_403_view(request, exception):  
    return render(request, 'errors/403.html', status=403)


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "",
        "Disallow: /admin/",
        "",
        "Sitemap: https://www.convictionic.cl/sitemap.xml"
        
        
    ]
    
    return HttpResponse("\n".join(lines), content_type="text/plain")

