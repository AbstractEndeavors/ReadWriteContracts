import PySimpleGUI as sg
import functions as fun
import grabApi
import sys
def startCont(path):
    sys.path.insert(0, path)
    print(path)
    import dothefunx
    dothefunx.windowDesk = windowDesk
    dotheFunx.startIt()
    sys.path.insert(0, home)
def widowMain(window):
      while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        elif event == 'getABI':
              
              input(values['pathChooseLs'])
              startCont(values['pathChooseLs'])
        elif event == 'RUN':
              from rpcListNew import rpcs as rpcLs
              add = values['runAdd']
              for k in range(0,len(rpcLs)):
                  progress_bar = window['progressbar']
                  progress_bar.UpdateBar(k)
                  keys = fun.getKeys(rpcLs[k])
                  
                  window['progTitle'].update(value=rpcLs[k])
                  window['progTitle'].update(value=rpcLs[k])
                  grabApi.deriveAnyInfo(add,k)
        elif event == 'Edit Me':
              sg.execute_editor(__file__)
        elif event == 'Version':
              sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
        elif event == 'File Location':
              sg.popup_scrolled('This Python file is:', __file__)
        window.refresh()
        #window.close()
        
def windowChat(window):
  while True:
        event, value = window.read()
        if event == 'SEND':
            query = value['query'].rstrip()
            # EXECUTE YOUR COMMAND HERE
            print('The command you entered was {}'.format(query))
            command_history.append(query)
            history_offset = len(command_history)-1
            # manually clear input because keyboard events blocks clear
            window['query'].update('')
            window['history'].update('\n'.join(command_history[-3:]))
        elif event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit event or X
            break
        elif 'Up' in event and len(command_history):
            command = command_history[history_offset]
            # decrement is not zero
            history_offset -= 1 * (history_offset > 0)
            window['query'].update(command)
        elif 'Down' in event and len(command_history):
            # increment up to end of list
            history_offset += 1 * (history_offset < len(command_history)-1)
            command = command_history[history_offset]
            window['query'].update(command)
        elif 'Escape' in event:
            window['query'].update('')
def menuWindow(window):
  while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'About...':
        window.disappear()
        sg.popup('About this program', 'Version 1.0', 'PySimpleGUI Version', sg.get_versions())
        window.reappear()
    elif event == 'Open':
        filename = sg.popup_get_file('file to open', no_window=True)
    elif event == 'Properties':
        second_window()
  window.close()
def sloaderWindow(window):
  while True:
    event, values = window.read()
    if event in ('EXIT', None):
        break           # exit button clicked
    if event in ('Shortcut 1', 'Fav Program'):
        print('Quickly launch your favorite programs using these shortcuts')
        print('''
            Or  copy files to your github folder.
            Or anything else you type on the command line''')
        # copyfile(source, dest)
    elif event == 'Run':
        for index, file in enumerate(values['demolist']):
            print('Launching %s' % file)
            window.refresh()          # make the print appear immediately
            if values['wait']:
                execute_command_blocking(LOCATION_OF_YOUR_SCRIPTS + file)
            else:
                execute_command_nonblocking(
                    LOCATION_OF_YOUR_SCRIPTS + file)

  window.close()
global rpcLs
from rpcListNew import rpcs as rpcLs
