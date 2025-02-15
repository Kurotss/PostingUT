def input_value(caption, is_required, is_multi_lines):
    input_string = None
    while True:
        if not is_multi_lines:
            input_string = input(caption + '\n')
        else:
            print(caption + " (введите последней пустую строку, чтобы закончить ввод)")
            input_string = "\n".join(iter(input, ''))
        
        if is_required and not input_string:
            print("Эта часть не может быть пустой")
        elif not is_required and not input_string:
            confirmation = input("Введите y, чтобы подтвердить пустое поле" + '\n')
            if confirmation == "y":
                break;
        else:
            break;
    return input_string

#make description of event            
def make_description():
    ## enter description
    event_name = input_value("Введите название ивента", is_required=True, is_multi_lines=False)
    event_number = input_value("Введите номер ивента", is_required=True, is_multi_lines=False)
    description = input_value("Введите описание ивента", is_required=True, is_multi_lines=False)
    ## timecodes = input_value("Введите таймкоды", is_required=True, is_multi_lines=True)
    translators = input_value("Перевод:", is_required=True, is_multi_lines=False)
    editors = input_value("Редактура:", is_required=True, is_multi_lines=False)
    video_makers = input_value("Монтаж:", is_required=True, is_multi_lines=False)
    subs = input_value("Субтитры:", is_required=True, is_multi_lines=False)
    logo = input_value("Логотип: (введите пустую строку, если блок должен быть пустым)", is_required=False, is_multi_lines=False)
    ## hashtags = input_value("Введите хэштеги", is_required=True, is_multi_lines=True)

    last_three = event_name[-3:] 
    if last_three != "..." and event_name[-1] == '.':
        event_name = event_name[:-1]
    
    message = f'Перевод {event_number}-{"его" if event_number[-1] == "3" and event_number[-2:] != "13" else "ого"} ивента «{event_name}».'
    if event_name[-1] == '!' or event_name[-1] == '?' or last_three == "...":
        message = message[:-1]
    ## message += f'\n\n{description}\n\nТаймкоды:\n\n{timecodes}\n\nПеревод: {translators}\nРедактура: {editors}\n'
    message += f'\n\n{description}\n\nПеревод: {translators}\nРедактура: {editors}\n'
    message += f'Монтаж: {video_makers}\nСубтитры: {subs}\n'
    if logo:
        message += f'Логотип: {logo}\n'
    return message

def enter_video_info():
    video_path = input_value("Введите путь к видео", is_required=True, is_multi_lines=False)
    thumb_path = input_value("Введите путь к обложке", is_required=True, is_multi_lines=False)
    schedule_date_string = input_value("Введите дату публикации в формате: yyyy-mm-dd HH:MM", is_required=True, is_multi_lines=False)  

    return video_path, thumb_path, schedule_date_string
