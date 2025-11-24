from config.database import Database

class Category:
    @staticmethod
    def get_all():
        """Obtiene todas las categorías"""
        query = """
            SELECT id, nombre, descripcion 
            FROM pablogarciajcbd.categorias 
            WHERE activo = 1
            ORDER BY nombre
        """
        return Database.execute_query(query)
    
    @staticmethod
    def get_by_id(category_id):
        """Obtiene una categoría por su ID"""
        query = """
            SELECT id, nombre, descripcion 
            FROM pablogarciajcbd.categorias 
            WHERE id = %s AND activo = 1
        """
        result = Database.execute_query(query, (category_id,))
        return result[0] if result else None
    
    @staticmethod
    def count():
        """Cuenta el total de categorías"""
        query = "SELECT COUNT(*) as total FROM pablogarciajcbd.categorias WHERE activo = 1"
        result = Database.execute_query(query)
        return result[0]['total'] if result else 0
