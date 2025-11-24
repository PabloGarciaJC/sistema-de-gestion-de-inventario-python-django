from django.http import HttpResponse
from app.views.layout import Layout

class SaleView:
    """Vista de Ventas"""
    
    @staticmethod
    def index(user, sales):
        """Renderiza la página de listado de ventas"""
        
        # Mapeo de estados a badges
        estado_badges = {
            'pendiente': '<span class="badge badge-warning">Pendiente</span>',
            'completada': '<span class="badge badge-success">Completada</span>',
            'cancelada': '<span class="badge" style="background: #fee2e2; color: #991b1b;">Cancelada</span>'
        }
        
        # Generar las filas de la tabla
        if sales:
            rows = ""
            for sale in sales:
                badge = estado_badges.get(sale['estado'], sale['estado'])
                rows += f"""
                <tr>
                    <td>{sale['numero_factura']}</td>
                    <td>{sale['fecha']}</td>
                    <td>{sale['cliente_nombre']}</td>
                    <td>{sale['cliente_documento'] or 'N/A'}</td>
                    <td>${sale['total']:.2f}</td>
                    <td>{badge}</td>
                    <td>{sale['tipo_pago'].capitalize()}</td>
                    <td>
                        <button class="btn btn-success">Ver</button>
                        <button class="btn btn-warning">Editar</button>
                    </td>
                </tr>
                """
            
            table_content = f"""
            <table>
                <thead>
                    <tr>
                        <th>Factura</th>
                        <th>Fecha</th>
                        <th>Cliente</th>
                        <th>Documento</th>
                        <th>Total</th>
                        <th>Estado</th>
                        <th>Tipo Pago</th>
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
                <div style="font-size: 4rem; margin-bottom: 20px;">🛒</div>
                <h3>No hay ventas registradas</h3>
                <p>Comienza registrando tu primera venta</p>
            </div>
            """
        
        content = f"""
        <div class="card">
            <div class="card-header">
                <span>Gestión de Ventas</span>
                <button class="btn btn-primary">+ Nueva Venta</button>
            </div>
            {table_content}
        </div>
        """
        
        return HttpResponse(Layout.render('Ventas', user, 'ventas', content))
