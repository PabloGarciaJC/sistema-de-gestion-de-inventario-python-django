from config.database import Database

class Config:
    """Modelo para la configuración del sistema"""
    
    @staticmethod
    def get_user_info(user_id):
        """Obtiene información completa del usuario"""
        query = """
            SELECT 
                u.id,
                u.username,
                u.nombre_completo,
                u.email,
                u.activo,
                u.created_at,
                r.nombre as rol
            FROM pablogarciajcbd.usuarios u
            INNER JOIN pablogarciajcbd.roles r ON u.rol_id = r.id
            WHERE u.id = %s
        """
        result = Database.execute_query(query, (user_id,))
        return result[0] if result else None
    
    @staticmethod
    def get_system_stats():
        """Obtiene estadísticas generales del sistema"""
        query = """
            SELECT 
                (SELECT COUNT(*) FROM pablogarciajcbd.usuarios WHERE activo = 1) as total_usuarios,
                (SELECT COUNT(*) FROM pablogarciajcbd.productos WHERE activo = 1) as total_productos,
                (SELECT COUNT(*) FROM pablogarciajcbd.categorias WHERE activo = 1) as total_categorias,
                (SELECT COUNT(*) FROM pablogarciajcbd.clientes WHERE activo = 1) as total_clientes,
                (SELECT COUNT(*) FROM pablogarciajcbd.proveedores WHERE activo = 1) as total_proveedores,
                (SELECT COUNT(*) FROM pablogarciajcbd.ventas) as total_ventas,
                (SELECT COUNT(*) FROM pablogarciajcbd.compras) as total_compras
        """
        result = Database.execute_query(query)
        return result[0] if result else {}
    
    @staticmethod
    def get_all_users():
        """Obtiene todos los usuarios del sistema"""
        query = """
            SELECT 
                u.id,
                u.username,
                u.nombre_completo,
                u.email,
                u.activo,
                r.nombre as rol
            FROM pablogarciajcbd.usuarios u
            INNER JOIN pablogarciajcbd.roles r ON u.rol_id = r.id
            ORDER BY u.created_at DESC
        """
        return Database.execute_query(query)
    
    @staticmethod
    def get_database_info():
        """Obtiene información de la base de datos"""
        query = """
            SELECT 
                TABLE_NAME as table_name,
                TABLE_ROWS as table_rows,
                ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024, 2) AS size_mb
            FROM information_schema.tables
            WHERE table_schema = 'pablogarciajcbd'
            AND TABLE_NAME NOT LIKE 'django_%%'
            ORDER BY TABLE_ROWS DESC
        """
        return Database.execute_query(query)
        return Database.execute_query(query)
