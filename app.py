import PySimpleGUI as sg
from time import sleep

sg.theme('reddit')

#layout

screen_login = [
    [sg.Text('User')],
    [sg.Input(key='user')],
    [sg.Text('Password')],
    [sg.Input(key='password', password_char='*')],
    [sg.Button('Login')],
    [sg.Output(size=(43, 10))]
]

#window

window = sg.Window('Login', layout=screen_login)

#events

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        user_value = values['user']
        password_value = values['password']
        print('First step')
        sleep(5)
        print('Second step')
        sleep(5)
        print('Third step')
        sleep(5)
        print('Fourth step')

window.close()