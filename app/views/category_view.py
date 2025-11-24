from django.http import HttpResponse
from app.views.layout import Layout

class CategoryView:
    """Vista de Categorías"""
    
    @staticmethod
    def index(user, categories):
        """Renderiza la página de listado de categorías"""
        
        # Generar las filas de la tabla
        if categories:
            rows = ""
            for idx, category in enumerate(categories, 1):
                rows += f"""
                <tr>
                    <td>{idx}</td>
                    <td>{category['nombre']}</td>
                    <td>{category['descripcion'] or 'Sin descripción'}</td>
                    <td>
                        <button class="btn btn-warning">Editar</button>
                        <button class="btn btn-danger">Eliminar</button>
                    </td>
                </tr>
                """
            
            table_content = f"""
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Nombre</th>
                        <th>Descripción</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
            """
        else:
            table_content = """
            <div class="empty-state">
                <div style="font-size: 4rem; margin-bottom: 20px;">📑</div>
                <h3>No hay categorías registradas</h3>
                <p>Comienza agregando tu primera categoría</p>
            </div>
            """
        
        content = f"""
        <div class="card">
            <div class="card-header">
                <span>Gestión de Categorías</span>
                <button class="btn btn-primary">+ Nueva Categoría</button>
            </div>
            {table_content}
        </div>
        """
        
        return HttpResponse(Layout.render('Categorías', user, 'categorias', content))
