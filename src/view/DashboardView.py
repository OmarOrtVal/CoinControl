import flet as ft

def DashboardView(page: ft.Page):
    user = getattr(page, "user_data", None)
    
    def mostrar_perfil(e):
        if not user:
            return
        dialogo = ft.AlertDialog(
            title=ft.Text("Mi Perfil"),
            content=ft.Column([
                ft.Text(f"Nombre: {user.get('nombre', '')} {user.get('apellido', '')}"),
                ft.Text(f"Email: {user.get('email', '')}"),
                ft.Text(f"Telefono: {user.get('telefono', 'No registrado')}"),
            ], tight=True),
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: close_dialog(dialogo))
            ],
        )
        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()
    
    def close_dialog(dialogo):
        dialogo.open = False
        page.update()
    
    def cerrar_sesion(e):
        page.user_data = None
        page.go("/")
    
    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text("Dashboard"),
                actions=[
                    ft.IconButton(
                        icon=ft.Icons.PERSON,
                        on_click=mostrar_perfil
                    ),
                    ft.IconButton(
                        icon=ft.Icons.LOGOUT,
                        on_click=cerrar_sesion
                    ),
                ],
            ),
        ]
    )