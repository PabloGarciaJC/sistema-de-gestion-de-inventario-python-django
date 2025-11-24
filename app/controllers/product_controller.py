from django.http import HttpResponse, HttpResponseRedirect
from app.models.user import User
from app.models.product import Product
from app.views.product_view import ProductView

class ProductController:
    """Controlador de Productos"""
    
    @staticmethod
    def index(request):
        """Lista de productos"""
        # Verificar autenticación
        user_id = request.session.get('user_id')
        
        if not user_id:
            return HttpResponseRedirect('/login/')
        
        user = User.get_by_id(user_id)
        if not user:
            request.session.flush()
            return HttpResponseRedirect('/login/')
        
        # Obtener productos
        products = Product.get_all()
        
        return HttpResponse(ProductView.index(user, request.path, products))
