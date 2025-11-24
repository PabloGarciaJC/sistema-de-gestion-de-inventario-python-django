from config.database import Database

class Sale:
    """Modelo de Venta"""
    
    @staticmethod
    def get_all():
        """Obtiene todas las ventas con información del cliente"""
        query = """
            SELECT 
                v.id,
                v.numero_factura,
                v.fecha,
                v.total,
                v.estado,
                v.tipo_pago,
                c.nombre as cliente_nombre,
                c.documento as cliente_documento,
                u.username as vendedor
            FROM pablogarciajcbd.ventas v
            INNER JOIN pablogarciajcbd.clientes c ON v.cliente_id = c.id
            INNER JOIN pablogarciajcbd.usuarios u ON v.usuario_id = u.id
            ORDER BY v.fecha DESC, v.id DESC
        """
        return Database.execute_query(query)
    
    @staticmethod
    def get_by_id(sale_id):
        """Obtiene una venta por su ID"""
        query = """
            SELECT 
                v.*,
                c.nombre as cliente_nombre,
                c.documento as cliente_documento,
                c.telefono as cliente_telefono,
                u.username as vendedor
            FROM pablogarciajcbd.ventas v
            INNER JOIN pablogarciajcbd.clientes c ON v.cliente_id = c.id
            INNER JOIN pablogarciajcbd.usuarios u ON v.usuario_id = u.id
            WHERE v.id = %s
        """
        result = Database.execute_query(query, (sale_id,))
        return result[0] if result else None
    
    @staticmethod
    def count():
        """Cuenta el total de ventas"""
        query = "SELECT COUNT(*) as total FROM pablogarciajcbd.ventas"
        result = Database.execute_query(query)
        return result[0]['total'] if result else 0
    
    @staticmethod
    def total_ventas_mes():
        """Calcula el total de ventas del mes actual"""
        query = """
            SELECT COALESCE(SUM(total), 0) as total
            FROM pablogarciajcbd.ventas
            WHERE MONTH(fecha) = MONTH(CURRENT_DATE())
            AND YEAR(fecha) = YEAR(CURRENT_DATE())
            AND estado = 'completada'
        """
        result = Database.execute_query(query)
        return result[0]['total'] if result else 0
