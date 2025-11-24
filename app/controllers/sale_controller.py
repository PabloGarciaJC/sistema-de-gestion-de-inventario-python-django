from app.models.user import User
from app.models.sale import Sale
from app.views.sale_view import SaleView
from django.shortcuts import redirect
from django.http import HttpResponse

class SaleController:
    @staticmethod
    def index(request):
        """Muestra el listado de ventas"""
        # Verificar si el usuario está autenticado
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')
        
        # Obtener el usuario
        user = User.get_by_id(user_id)
        if not user:
            return redirect('/login/')
        
        # Obtener todas las ventas
        sales = Sale.get_all()
        
        # Renderizar la vista
        return HttpResponse(SaleView.index(user, sales))
