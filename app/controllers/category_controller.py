from app.models.user import User
from app.models.category import Category
from app.views.category_view import CategoryView
from django.shortcuts import redirect

class CategoryController:
    @staticmethod
    def index(request):
        """Muestra el listado de categorías"""
        # Verificar si el usuario está autenticado
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')
        
        # Obtener el usuario
        user = User.get_by_id(user_id)
        if not user:
            return redirect('/login/')
        
        # Obtener todas las categorías
        categories = Category.get_all()
        
        # Renderizar la vista
        return CategoryView.index(user, categories)
