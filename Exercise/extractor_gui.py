import FreeSimpleGUI as sg

layout = [[sg.Text("Select Archive:"), sg.InputText(), sg.FileBrowse("Choose", key="files")],
          [sg.Text("Select Directory:"), sg.InputText(), sg.FileBrowse("Choose", key="Folder")],
          [sg.Button("Extract"), sg.Button("Exit")]]

window = sg.Window("Archive Extractor", layout)

while True:
    event, values = window.read()
    
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
window.close()
