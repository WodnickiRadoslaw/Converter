import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['km to m', 'm to km', 'kg to g', 'g to kg',
                'sec to min', 'min to sec', 'hr to min', 'min to hr', "C to F", "F to C"], key='-UNITS-'),
        sg.Button('Convert!', key='-CONVERT-')
    ],
    [sg.Text('Output: ', key='-OUTPUT-')]
]
window = sg.Window('Basic Converter', layout, size=(485, 100))
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to m':
                    output = round(float(input_value) * 1000, 2)
                    output_string = f'{input_value} kilometer(s) are {output} meters.'
                case 'm to km':
                    output = round(float(input_value) / 1000, 2)
                    output_string = f'{input_value} meters are {output} kilometer(s).'
                case 'kg to g':
                    output = round(float(input_value) / 0.001, 2)
                    output_string = f'{input_value} kilogram(s) are {output} grams.'
                case 'g to kg':
                    output = round(float(input_value) / 1000, 2)
                    output_string = f'{input_value} grams are {output} kilogram(s).'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds are {output} minute(s).'
                case 'min to sec':
                    output = round(float(input_value) * 60, 2)
                    output_string = f'{input_value} minute(s) are {output} seconds.'
                case 'hr to min':
                    output = round(float(input_value) * 60, 2)
                    output_string = f'{input_value} hour(s) are {output} minutes.'
                case 'min to hr':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} minute(s) are {output} hours.'
                case 'C to F':
                    output = round(float(input_value) * 1.8 + 32, 2)
                    output_string = f'{input_value} Celcius is {output} Fahrenheit.'
                case 'F to C':
                    output = round(float((input_value) - 32)
                                   * 0.55555555555, 2)
                    output_string = f'{input_value} Fahrenheit is {output} Celcius.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please, enter a number:')
window.close()
