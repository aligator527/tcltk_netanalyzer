import core
import PySimpleGUI as sg

Network = core.Network()

def main():

    monitor = Network.monitor_packages()

    addrs = Network.get_addrs()
    layout_addrs = [sg.Button('All')]
    handle_addr = ["All"]
    for addr in addrs:
        layout_addrs.append(sg.Button(addr))
        handle_addr.append(addr)
    print(layout_addrs, handle_addr)
    # Define the window's contents
    layout = [  [sg.Text("Host Name:"),     sg.Text(Network.get_name()), sg.Text("|"), sg.Text("Host IP:"), sg.Text(Network.get_addr())],
                [sg.Text("Bytes Sent:"),    sg.Text(monitor[0], key='-MONITOR1-')],
                [sg.Text("Bytes Recv:"),    sg.Text(monitor[1], key='-MONITOR2-')],
                [sg.Text("Packets Sent:"),  sg.Text(monitor[2], key='-MONITOR3-')],
                [sg.Text("Packets Recv:"),  sg.Text(monitor[3], key='-MONITOR4-')],
                [layout_addrs]
            ]

    # Create the window
    window = sg.Window('TCL/TK Network Analyzer', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'All':
            monitor = Network.monitor_packages()
            window['-MONITOR1-'].update(monitor[0])
            window['-MONITOR2-'].update(monitor[1])
            window['-MONITOR3-'].update(monitor[2])
            window['-MONITOR4-'].update(monitor[3])
        elif event in handle_addr:
            monitor = Network.monitor_packages(event)
            window['-MONITOR1-'].update(monitor[0])
            window['-MONITOR2-'].update(monitor[1])
            window['-MONITOR3-'].update(monitor[2])
            window['-MONITOR4-'].update(monitor[3])

    # Finish up by removing from the screen
    window.close()

if __name__ == "__main__":
    main()