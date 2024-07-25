from django.shortcuts import redirect

def AuthMiddleware(get_response):
    def middleware(request):
        protected_paths = ['/', '/AddMovie/', '/Profile/', '/edit_movie/','/delete_movie/','/delete_profile/','/password']  

        if request.path in protected_paths and not request.user.is_authenticated:
            return redirect('login')
        
        response = get_response(request)
        return response
    
    return middleware
