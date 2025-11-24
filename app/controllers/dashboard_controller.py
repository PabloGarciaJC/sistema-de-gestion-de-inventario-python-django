from django.http import HttpResponse, HttpResponseRedirect
from app.models.user import User
from app.models.product import Product
from app.models.category import Category
from app.models.sale import Sale
from app.views.dashboard_view import DashboardView

class DashboardController:
    """Controlador del Dashboard"""
    
    @staticmethod
    def index(request):
        """Muestra el dashboard"""
        # Verificar autenticación
        user_id = request.session.get('user_id')
        
        if not user_id:
            return HttpResponseRedirect('/login/')
        
        # Obtener datos del usuario
        user = User.get_by_id(user_id)
        
        if not user:
            request.session.flush()
            return HttpResponseRedirect('/login/')
        
        # Obtener estadísticas
        stats = {
            'total_productos': Product.count(),
            'total_categorias': Category.count(),
            'ventas_mes': Sale.total_ventas_mes()
        }
        
        # Renderizar dashboard
        return HttpResponse(DashboardView.index(user, request.path, stats))
