from django.http import HttpResponse
from app.views.layout import Layout

class ChatbotView:
    """Vista del Chatbot con IA"""
    
    @staticmethod
    def render(user, history):
        """Renderiza la interfaz del chatbot"""
        
        # Construir mensajes del historial
        history_html = ""
        if history:
            for msg in history:
                history_html += f"""
                <div class='message user-message'>
                    <div class='message-content'>
                        <i class='fas fa-user message-icon'></i>
                        <div class='message-text'>{msg['message']}</div>
                    </div>
                    <div class='message-time'>{msg['created_at']}</div>
                </div>
                <div class='message bot-message'>
                    <div class='message-content'>
                        <i class='fas fa-robot message-icon'></i>
                        <div class='message-text'>{msg['response'].replace('•', '').replace('-', '').replace('•', '')}</div>
                    </div>
                    <div class='message-time'>{msg['created_at']}</div>
                </div>
                """
        else:
            history_html = """
            <div class='welcome-message'>
                <i class='fas fa-robot welcome-icon'></i>
                <h3>¡Bienvenido al Asistente Virtual!</h3>
                <p>Soy tu asistente de inventario con inteligencia artificial.</p>
                <p>Puedes preguntarme sobre productos, ventas, compras, stock, proveedores, clientes y cualquier módulo del sistema.</p>
                <p>Ejemplo: <strong>¿Qué productos tienen stock bajo?</strong></p>
                <div class='welcome-commands'>
                    <h4 class='welcome-commands-title'>Comandos básicos</h4>
                    <ul class='welcome-commands-list'>
                        <li class='welcome-command-item'><strong>"ayuda"</strong> - Muestra qué puede hacer el chatbot</li>
                        <li class='welcome-command-item'><strong>"buscar producto [nombre]"</strong> - Busca productos específicos</li>
                        <li class='welcome-command-item'><strong>"resumen de ventas"</strong> - Muestra estadísticas de ventas</li>
                        <li class='welcome-command-item'><strong>"resumen de compras"</strong> - Muestra estadísticas de compras</li>
                        <li class='welcome-command-item'><strong>"productos con stock bajo"</strong> - Lista productos con poco inventario</li>
                    </ul>
                </div>
            </div>
        """
        content = f"""
        <div class='card'>
            <div class='card-header'>
                <span><i class='fas fa-robot'></i> Asistente Virtual con IA</span>
                <button class='btn btn-secondary' id='clear-history-btn'>
                    <i class='fas fa-trash'></i> Limpiar Historial
                </button>
            </div>
            <div class='card-body chatbot-container'>
                <div id='chat-messages' class='chat-messages'>
                    {history_html}
                </div>
                <div id='typing-indicator' style='display:none;align-items:center;gap:8px;margin:10px 0;'>
                    <span class='spinner-border spinner-border-sm text-primary'></span>
                    <span>El asistente está escribiendo...</span>
                </div>
                <div class='chat-input-container'>
                    <div class='chat-input-wrapper'>
                        <textarea id='message-input' class='chat-input' rows='1' placeholder='Escribe tu mensaje...'></textarea>
                        <button id='send-btn' class='send-btn'><i class='fas fa-paper-plane'></i></button>
                    </div>
                </div>
            </div>
        </div>
        <script src='/static/js/chatbot.js'></script>
        """
        html = Layout.render(
            title="Chatbot IA",
            user=user,
            active_page="chatbot",
            content=content
        )
        return HttpResponse(html)
