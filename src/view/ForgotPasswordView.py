import flet as ft

def ForgotPasswordView(page: ft.Page, auth_controller):
    
    txt_email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=400,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    mensaje = ft.Text("", color="red", size=12)
    mensaje_exito = ft.Text("", color="green", size=12)
    
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=3000,
        )
        page.snack_bar.open = True
        page.update()
    
    def enviar_correo(e):
        if not txt_email.value:
            mensaje.value = "Ingresa tu correo electrónico"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
            return
        
        exito, msg = auth_controller.solicitar_recuperacion(txt_email.value)
        
        if exito:
            mensaje.value = ""
            mensaje_exito.value = msg
            txt_email.value = ""
            page.update()
            
            # Regresar al login después de 3 segundos
            import time
            def volver():
                time.sleep(3)
                page.go("/")
            import threading
            threading.Thread(target=volver, daemon=True).start()
        else:
            mensaje.value = msg
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
    
    def volver_login(e):
        page.go("/")
    
    return ft.View(
        route="/forgot-password",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("CoinControl - Recuperar Contraseña"),
            bgcolor=ft.Colors.GREEN_700,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK, 
                on_click=volver_login
            )
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK_RESET, size=60, color=ft.Colors.GREEN_700),
                    ft.Text("¿Olvidaste tu contraseña?", size=24, weight="bold"),
                    ft.Text("Ingresa tu correo y te enviaremos un enlace para restablecerla", 
                        size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    txt_email,
                    mensaje,
                    mensaje_exito,
                    ft.Container(height=10),
                    ft.ElevatedButton(
                        "Enviar enlace",
                        width=250,
                        on_click=enviar_correo,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREEN_500,
                            color=ft.Colors.WHITE,
                            padding=20,
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                    ),
                    ft.TextButton(
                        "Volver al inicio de sesión",
                        on_click=volver_login
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=10
            )
        ]
    )