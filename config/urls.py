from django.urls import path
from app.controllers.auth_controller import AuthController
from app.controllers.dashboard_controller import DashboardController
from app.controllers.product_controller import ProductController
from app.controllers.category_controller import CategoryController
from app.controllers.sale_controller import SaleController
from app.controllers.report_controller import ReportController

urlpatterns = [
    path('', DashboardController.index, name='dashboard'),
    path('login/', AuthController.login, name='login'),
    path('register/', AuthController.register, name='register'),
    path('logout/', AuthController.logout, name='logout'),
    path('productos/', ProductController.index, name='products'),
    path('categorias/', CategoryController.index, name='categories'),
    path('ventas/', SaleController.index, name='sales'),
    path('reportes/', ReportController.index, name='reports'),
]
