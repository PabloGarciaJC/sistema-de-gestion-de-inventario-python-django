from config.database import Database

class Product:
    """Modelo de Producto"""
    
    @staticmethod
    def get_all():
        """Obtiene todos los productos"""
        query = """
            SELECT p.*, c.nombre as categoria
            FROM productos p
            LEFT JOIN categorias c ON p.categoria_id = c.id
            ORDER BY p.id DESC
        """
        return Database.execute_query(query)
    
    @staticmethod
    def get_by_id(product_id):
        """Obtiene un producto por ID"""
        query = """
            SELECT p.*, c.nombre as categoria
            FROM productos p
            LEFT JOIN categorias c ON p.categoria_id = c.id
            WHERE p.id = %s
        """
        products = Database.execute_query(query, (product_id,))
        return products[0] if products else None
    
    @staticmethod
    def count():
        """Cuenta el total de productos"""
        result = Database.execute_query("SELECT COUNT(*) as count FROM productos")
        return result[0]['count'] if result else 0
