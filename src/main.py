import flet as ft


def main(page: ft.Page):
    page.title = "Destino Certo - Login"
    page.window_width = 1440
    page.window_height = 900
    page.window_min_width = 1100
    page.window_min_height = 700
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F4F8FB"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos
    email_field = ft.TextField(
        label="E-mail",
        hint_text="Digite seu e-mail",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border_radius=14,
        filled=True,
        bgcolor="#F8FAFC",
        border_color="#D6E4F0",
        focused_border_color="#1E88E5",
        text_size=14,
        cursor_color="#1E88E5",
        height=56,
    )

    password_field = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        border_radius=14,
        filled=True,
        bgcolor="#F8FAFC",
        border_color="#D6E4F0",
        focused_border_color="#1E88E5",
        text_size=14,
        cursor_color="#1E88E5",
        height=56,
    )

    feedback_text = ft.Text(
        "",
        size=13,
        color="#D32F2F",
        weight=ft.FontWeight.W_500,
    )

    def fazer_login(e):
        email = email_field.value.strip()
        senha = password_field.value.strip()

        if not email or not senha:
            feedback_text.value = "Preencha e-mail e senha para continuar."
            feedback_text.color = "#D32F2F"
        else:
            feedback_text.value = f"Login realizado com sucesso. Bem-vindo ao Destino Certo, {email}!"
            feedback_text.color = "#2E7D32"

        page.update()

    def ir_para_cadastro(e):
        feedback_text.value = "Redirecionando para a tela de cadastro..."
        feedback_text.color = "#1E88E5"
        page.update()

    # Lado esquerdo - apresentação do projeto
    left_panel = ft.Container(
        expand=True,
        padding=50,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    width=82,
                    height=82,
                    border_radius=20,
                    bgcolor="#FFFFFF",
                    alignment=ft.alignment.center,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=25,
                        color="#00000012",
                        offset=ft.Offset(0, 8),
                    ),
                    content=ft.Text(
                        "DC",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="#1E88E5",
                    ),
                ),
                ft.Container(height=18),
                ft.Text(
                    "Destino Certo",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color="#0F172A",
                ),
                ft.Text(
                    "Turismo acessível para todos.",
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color="#1E88E5",
                ),
                ft.Container(height=12),
                ft.Text(
                    "Encontre destinos, hotéis, restaurantes e pontos turísticos "
                    "com informações confiáveis sobre acessibilidade, mobilidade e inclusão.",
                    size=16,
                    color="#475569",
                    width=520,
                ),
                ft.Container(height=28),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            padding=18,
                            border_radius=18,
                            bgcolor="#FFFFFF",
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.ACCESSIBLE_FORWARD_ROUNDED, color="#1E88E5", size=30),
                                    ft.Column(
                                        spacing=4,
                                        controls=[
                                            ft.Text("Acessibilidade real", weight=ft.FontWeight.BOLD, size=15, color="#0F172A"),
                                            ft.Text("Informações verificadas por usuários e parceiros.", size=13, color="#64748B"),
                                        ],
                                    ),
                                ]
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            padding=18,
                            border_radius=18,
                            bgcolor="#FFFFFF",
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.MAP_ROUNDED, color="#00A86B", size=30),
                                    ft.Column(
                                        spacing=4,
                                        controls=[
                                            ft.Text("Descoberta de destinos", weight=ft.FontWeight.BOLD, size=15, color="#0F172A"),
                                            ft.Text("Planeje sua viagem com mais segurança.", size=13, color="#64748B"),
                                        ],
                                    ),
                                ]
                            ),
                        ),
                    ]
                ),
            ],
        ),
    )

    # Card de login
    login_card = ft.Container(
        width=430,
        padding=35,
        border_radius=28,
        bgcolor="#FFFFFF",
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=35,
            color="#00000018",
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            tight=True,
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Entrar",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#0F172A",
                ),
                ft.Text(
                    "Acesse sua conta para explorar destinos acessíveis.",
                    size=14,
                    color="#64748B",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=6),
                email_field,
                password_field,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=8,
                            controls=[
                                ft.Checkbox(value=True, active_color="#1E88E5"),
                                ft.Text("Lembrar-me", size=13, color="#475569"),
                            ],
                        ),
                        ft.TextButton(
                            "Esqueci minha senha",
                            style=ft.ButtonStyle(
                                color="#1E88E5",
                                overlay_color="#00000000",
                            ),
                        ),
                    ],
                ),
                feedback_text,
                ft.Container(height=4),
                ft.ElevatedButton(
                    text="Entrar",
                    width=360,
                    height=52,
                    on_click=fazer_login,
                    style=ft.ButtonStyle(
                        bgcolor="#1E88E5",
                        color="#FFFFFF",
                        shape=ft.RoundedRectangleBorder(radius=14),
                        elevation=4,
                    ),
                ),
                ft.OutlinedButton(
                    text="Criar conta",
                    width=360,
                    height=50,
                    on_click=ir_para_cadastro,
                    style=ft.ButtonStyle(
                        side=ft.BorderSide(1, "#1E88E5"),
                        color="#1E88E5",
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                ),
                ft.Container(height=6),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Ainda não tem cadastro?", size=13, color="#64748B"),
                        ft.TextButton(
                            "Cadastre-se",
                            on_click=ir_para_cadastro,
                            style=ft.ButtonStyle(color="#1E88E5"),
                        ),
                    ],
                ),
            ],
        ),
    )

    right_panel = ft.Container(
        width=500,
        padding=30,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[login_card],
        ),
    )

    main_layout = ft.Container(
        expand=True,
        padding=30,
        content=ft.Row(
            expand=True,
            controls=[
                left_panel,
                right_panel,
            ],
        ),
    )

    page.add(main_layout)


ft.app(target=main)