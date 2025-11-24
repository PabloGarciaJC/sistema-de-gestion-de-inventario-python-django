from django.http import HttpResponse
from app.views.layout import Layout

class ConfigView:
    """Vista de Configuración"""
    
    @staticmethod
    def index(user, data):
        """Renderiza la página de configuración del sistema"""
        
        user_info = data.get('user_info', {})
        system_stats = data.get('system_stats', {})
        all_users = data.get('all_users', [])
        database_info = data.get('database_info', [])
        
        # Sección de información del usuario
        user_section = f"""
        <div class="card">
            <div class="card-header">👤 Mi Perfil</div>
            <div style="padding: 20px;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <div>
                        <p style="color: #666; font-size: 0.9rem; margin-bottom: 5px;">Usuario</p>
                        <p style="font-weight: 600;">{user_info.get('username', 'N/A')}</p>
                    </div>
                    <div>
                        <p style="color: #666; font-size: 0.9rem; margin-bottom: 5px;">Nombre Completo</p>
                        <p style="font-weight: 600;">{user_info.get('nombre_completo', 'N/A')}</p>
                    </div>
                    <div>
                        <p style="color: #666; font-size: 0.9rem; margin-bottom: 5px;">Email</p>
                        <p style="font-weight: 600;">{user_info.get('email', 'N/A')}</p>
                    </div>
                    <div>
                        <p style="color: #666; font-size: 0.9rem; margin-bottom: 5px;">Rol</p>
                        <p style="font-weight: 600;">{user_info.get('rol', 'N/A')}</p>
                    </div>
                    <div>
                        <p style="color: #666; font-size: 0.9rem; margin-bottom: 5px;">Estado</p>
                        <p style="font-weight: 600;">
                            {'<span class="badge badge-success">Activo</span>' if user_info.get('activo') else '<span class="badge" style="background: #fee2e2; color: #991b1b;">Inactivo</span>'}
                        </p>
                    </div>
                    <div>
                        <p style="color: #666; font-size: 0.9rem; margin-bottom: 5px;">Miembro desde</p>
                        <p style="font-weight: 600;">{user_info.get('created_at', 'N/A')}</p>
                    </div>
                </div>
                <div style="margin-top: 20px;">
                    <button class="btn btn-primary">Editar Perfil</button>
                    <button class="btn btn-warning" style="margin-left: 10px;">Cambiar Contraseña</button>
                </div>
            </div>
        </div>
        """
        
        # Sección de estadísticas del sistema
        stats_section = f"""
        <div class="card">
            <div class="card-header">📊 Estadísticas del Sistema</div>
            <div class="stats-grid">
                <div class="stat-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                    <h3>Usuarios</h3>
                    <div class="value">{system_stats.get('total_usuarios', 0)}</div>
                </div>
                <div class="stat-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                    <h3>Productos</h3>
                    <div class="value">{system_stats.get('total_productos', 0)}</div>
                </div>
                <div class="stat-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                    <h3>Clientes</h3>
                    <div class="value">{system_stats.get('total_clientes', 0)}</div>
                </div>
                <div class="stat-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
                    <h3>Ventas</h3>
                    <div class="value">{system_stats.get('total_ventas', 0)}</div>
                </div>
            </div>
        </div>
        """
        
        # Sección de usuarios del sistema
        users_rows = ""
        if all_users:
            for usuario in all_users:
                estado_badge = '<span class="badge badge-success">Activo</span>' if usuario['activo'] else '<span class="badge" style="background: #fee2e2; color: #991b1b;">Inactivo</span>'
                users_rows += f"""
                <tr>
                    <td>{usuario['username']}</td>
                    <td>{usuario['nombre_completo']}</td>
                    <td>{usuario['email'] or 'N/A'}</td>
                    <td>{usuario['rol']}</td>
                    <td>{estado_badge}</td>
                    <td>
                        <button class="btn btn-warning">Editar</button>
                        <button class="btn btn-danger">Desactivar</button>
                    </td>
                </tr>
                """
        else:
            users_rows = '<tr><td colspan="6" class="empty-state">No hay usuarios</td></tr>'
        
        users_section = f"""
        <div class="card">
            <div class="card-header">
                <span>👥 Usuarios del Sistema</span>
                <button class="btn btn-primary">+ Nuevo Usuario</button>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Usuario</th>
                        <th>Nombre</th>
                        <th>Email</th>
                        <th>Rol</th>
                        <th>Estado</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {users_rows}
                </tbody>
            </table>
        </div>
        """
        
        # Sección de información de base de datos
        db_rows = ""
        if database_info:
            for table in database_info:
                db_rows += f"""
                <tr>
                    <td>{table['table_name']}</td>
                    <td>{table['table_rows']:,}</td>
                    <td>{table['size_mb']} MB</td>
                </tr>
                """
        else:
            db_rows = '<tr><td colspan="3" class="empty-state">No hay información disponible</td></tr>'
        
        db_section = f"""
        <div class="card">
            <div class="card-header">💾 Información de Base de Datos</div>
            <table>
                <thead>
                    <tr>
                        <th>Tabla</th>
                        <th>Registros</th>
                        <th>Tamaño</th>
                    </tr>
                </thead>
                <tbody>
                    {db_rows}
                </tbody>
            </table>
        </div>
        """
        
        content = f"""
        {user_section}
        {stats_section}
        {users_section}
        {db_section}
        """
        
        return HttpResponse(Layout.render('Configuración', user, 'configuracion', content))
