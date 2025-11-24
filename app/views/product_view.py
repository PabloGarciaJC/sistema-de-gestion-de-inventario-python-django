from django.http import HttpResponse
from app.views.layout import Layout

class ProductView:
    """Vista de Productos"""
    
    @staticmethod
    def index(user, request_path, products):
        """Vista de lista de productos"""
        
        # Generar filas de la tabla
        if products:
            rows = ''
            for product in products:
                rows += f"""
                <tr>
                    <td>{product['id']}</td>
                    <td>{product['nombre']}</td>
                    <td>{product.get('categoria', 'Sin categoría')}</td>
                    <td>${product['precio_venta']}</td>
                    <td>{product['stock_actual']}</td>
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
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Categoría</th>
                        <th>Precio</th>
                        <th>Stock</th>
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
                <div style="font-size: 4rem; margin-bottom: 20px;">📦</div>
                <h3>No hay productos registrados</h3>
                <p>Comienza agregando tu primer producto</p>
            </div>
            """
        
        content = f"""
        <div class="card">
            <div class="card-header">
                <span>Productos</span>
                <button class="btn btn-primary">+ Nuevo Producto</button>
            </div>
            {table_content}
        </div>
        """
        
        return HttpResponse(Layout.render('Productos', user, 'productos', content))
