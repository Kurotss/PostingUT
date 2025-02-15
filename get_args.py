def get_video_info()
    bot_name = None
    video_path = None
    thumb_path = None
    message = None
    schedule_date_string = None

    parser = argparse.ArgumentParser()
    parser.add_argument('--bot', type=str, help='bot name to send video')
    parser.add_argument('--video', type=str, help='path to video file')
    parser.add_argument('--thumb', type=str, help='path to thumb file')
    ##parser.add_argument('--message', type=str, help='message to send')
    parser.add_argument('--schedule_date', type=str, help='date and time when the video should be posted, format: yyyy-mm-dd HH:MM')
    args = parser.parse_args()

    
    if dir(args).count("bot") == 0 or args.bot == None:
        print("error:1", flush=True)
        sys.exit()
    else:
        bot_name = args.bot
    if dir(args).count("video") == 0 or args.video == None:
        print("error:2", flush=True)
        sys.exit()
    else:
        video_path = args.video
    if dir(args).count("thumb") == 0 or args.thumb == None:
        print("error:3", flush=True)
        sys.exit()
    else:
        thumb_path = args.thumb
    ##if dir(args).count("message") == 0 or args.message == None:
    ##    print("error:4", flush=True)
    ##    sys.exit()
    ##else:
    ##    message = args.message
    if dir(args).count("schedule_date") == 0 or args.schedule_date == None:
        print("error:5", flush=True)
        sys.exit()
    else:
        schedule_date_string = args.schedule_date
        
    return bot_name, video_path, thumb_path, schedule_date_string
