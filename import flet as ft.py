import flet as ft
from flet import (AlertDialog, Column, Container, MainAxisAlignment, Page, Row,
                  ScrollMode, Text, TextButton, TextField, TextThemeStyle,
                  ThemeMode, UserControl , ElevatedButton, )


class LoginPage(UserControl):
    def __init__(self):
        super().__init__()
        self.text_ini = Text(
            value="Wissen App",
            style=TextThemeStyle.TITLE_LARGE,
            color=ft.colors.BLACK,
        )
        self.textfild_user = TextField(
            label="Login",
            bgcolor="grey900",
            width= 250
        )
        self.textfild_password = TextField(
            label="Senha",
            password=True,
            bgcolor="grey900",
            width= 250
        )
        self.button_login = ElevatedButton(
            text="Login",
            color="grey900",
            bgcolor="grey200",
            width=250
        )
        self.button_register = TextButton(
            text="Cadastre-se",
            width=250,
            
        )  
        self.button_googleaccount = ElevatedButton(
            text="Use a Conta Google",
            color="grey900",
            bgcolor= "white",
            width= 250
        
        )

    def build(self):
        return Container(
            alignment=ft.alignment.center,
            margin=ft.margin.all(100),
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.text_ini,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfild_user,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfild_password,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.button_login,
                            
                        ]
                    ),
                        Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                        self.button_register,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                        self.button_googleaccount,
                        ]
                    ),
                ]
            )
        )


class RegisterPage(UserControl):
    def __init__(self):
        super().__init__()
        self.text_ini = Text(
            value="Cadastro Cliente",
            style=TextThemeStyle.TITLE_LARGE,
            color=ft.colors.BLACK,
        )
        self.textfield_name = TextField(
            label="Nome Completo",
            bgcolor="grey900",
        )
        self.textfield_password = TextField(
            label="Criar Senha",
            password=True,
            bgcolor="grey900",
        )
        self.textfield_password_confirm = TextField(
            label="Confirmar a Senha",
            password=True,
            bgcolor="grey900",
        )
        self.textfield_address = TextField(
            label="Endereço",
            bgcolor="grey900",
        )
        self.textfield_email = TextField(
            label="EMAIL",
            bgcolor="grey900",
        )
        self.textfield_phone = TextField(
            label="Telefone",
            bgcolor="grey900",
        )
        self.button_photo = TextButton(
            text="Foto",
        )
        self.button_register = ElevatedButton(
            text="Confirmar",
            bgcolor="grey900",
            color="white",
        )
        self.button_back = ElevatedButton(
            text="Voltar",
            bgcolor="grey900",
            color="white",
        )

    def build(self):
        return Container(
            alignment=ft.alignment.center,
            margin=ft.margin.all(40),
            content=Column(
                width= 500,
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.text_ini,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_name,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_password,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_password_confirm,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_address,
                        ]
                    ),
                    
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_email,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_phone,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.button_photo,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.button_register,
                            self.button_back,
                        ]
                    )
                ]
            )
        )


def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.title = "Wissen App"
    page.bgcolor = "orange"

    def clicked_reg_db(e):

        user = register_page.textfield_name.value
        password = register_page.textfield_password.value
        password_conf = register_page.textfield_password_confirm.value
        adress = register_page.textfield_email.value
        mail = register_page.textfield_email.value
        phone = register_page.textfield_phone.value
        if user == '' and password == '' and password_conf == '' and adress == ''  and mail == '' and phone == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Preencha todos os campos!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

        elif user == '' and password == password_conf:
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Por gentileza informe seu Nome Completo",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

        elif user and password != password_conf:
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="As senhas não conferem!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

        elif user and password == '' and password_conf == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Por favor preencha a senha",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

        elif user and password == password_conf and phone and mail and adress:
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value=f"olá {user} você foi cadastrado com sucesso!!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.GREEN,
                                
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                login_page
            )

    def clicked_reg_back(e):
        page.clean()
        page.add(
            login_page
        )

    register_page = RegisterPage()
    register_page.button_register.on_click = clicked_reg_db
    register_page.button_back.on_click = clicked_reg_back

    def clicked_login(e):

        user = login_page.textfild_user.value
        password = login_page.textfild_password.value

        if user == '' and password == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Preencha todos os Campos!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                login_page
            )

        elif user and password == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Preencha a Senha!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                login_page
            )

        elif password and user == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(5),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Preencha o Usuário!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                login_page
            )

        elif user and password:
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(30),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value=f"Seja Bem Vindo {user} !",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.GREEN
                            )
                        ]
                    )
                )
            )
            page.update()

    
            actions_alignment=MainAxisAlignment.END,

        page.dialog = dialog
        dialog.open = True
        page.update()

    def clicked_register(e):
        page.clean()
        page.add(
            register_page,
        )

    login_page = LoginPage()
    login_page.button_login.on_click = clicked_login
    login_page.button_register.on_click = clicked_register

    page.add(
        login_page,
    )


if __name__ == '__main__':
    ft.app(target=main, view= ft.WEB_BROWSER)
