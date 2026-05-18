import flet as ft
from controllers.UsuariosController import UsuariosController
from view.LoginView import LoginView
from view.RegisterView import RegisterView  
from view.PerfilView import UserView
from view.DashboardView import DashboardView

def start(page: ft.Page):
    page.title = "CoinControl"
    auth_ctrl = UsuariosController()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/register": 
            page.views.append(RegisterView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page))
        elif page.route == "/perfil":
            page.views.append(UserView(page, auth_ctrl))
        
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacía")])
            )

        page.update()
        
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
            
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    if page.route == "/":
        route_change(None)
    else:
        page.go("/")
    
def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()