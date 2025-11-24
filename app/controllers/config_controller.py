from app.models.user import User
from app.models.config import Config
from app.views.config_view import ConfigView
from django.shortcuts import redirect
from django.http import HttpResponse

class ConfigController:
    @staticmethod
    def index(request):
        """Muestra la página de configuración"""
        # Verificar si el usuario está autenticado
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')
        
        # Obtener el usuario
        user = User.get_by_id(user_id)
        if not user:
            return redirect('/login/')
        
        # Obtener datos de configuración
        data = {
            'user_info': Config.get_user_info(user_id),
            'system_stats': Config.get_system_stats(),
            'all_users': Config.get_all_users(),
            'database_info': Config.get_database_info()
        }
        
        # Renderizar la vista
        return HttpResponse(ConfigView.index(user, data))
