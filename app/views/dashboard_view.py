from django.http import HttpResponse
from app.views.layout import Layout

class DashboardView:
    """Vista del Dashboard"""
    
    @staticmethod
    def index(user, request_path, stats):
        """Vista principal del dashboard"""
        content = f"""
        <div class="card">
            <div class="card-header">Dashboard</div>
            <p>Bienvenido al sistema, {user['nombre_completo']}!</p>
            <p style="margin-top: 10px; color: #666;">Rol: {user['rol']}</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Productos</h3>
                <div class="value">{stats['total_productos']}</div>
            </div>
            <div class="stat-card">
                <h3>Categorías</h3>
                <div class="value">{stats['total_categorias']}</div>
            </div>
            <div class="stat-card">
                <h3>Ventas del Mes</h3>
                <div class="value">${stats['ventas_mes']}</div>
            </div>
        </div>
        """
        
        return HttpResponse(Layout.render('Dashboard', user, 'dashboard', content))
