#!/data/data/com.termux/files/usr/bin/python
import os, time, threading, sys, platform
import subprocess, argparse
from pytube import YouTube
from colorama import Fore



#Dibuat oleh mas Dx4, dengan suka rela loh, gratis lagiii
#Harusnya berterima kasihh bukan me recode


#This is main version
version = "1.0"







line1 = " __     __      _______    _            _                         ____  "
line2 = " \\ \\   / /     |__   __|  | |          | |                       |___ \\ "
line3 = "  \\ \\_/ /__  _   _| |_   _| |__   ___  | |_ ___    _ __ ___  _ __  __) |"
line4 = "   \\   / _ \\| | | | | | | | '_ \\ / _ \\ | __/ _ \\  | '_ ` _ \\| '_ \\|__ < "
line5 = "    | | (_) | |_| | | |_| | |_) |  __/ | || (_) | | | | | | | |_) |__) |"
line6 = "    |_|\\___/ \\__,_|_|\\__,_|_.__/ \\___|  \\__\\___/  |_| |_| |_| .__/____/ "
line7 = f"    Created by {Fore.RED}D{Fore.YELLOW}x{Fore.GREEN}4{Fore.RESET}                                          | |         "
line8 = f"    GitHub : {Fore.BLUE}https://github.com/{Fore.CYAN}DX4GREY{Fore.RESET}                     |_|  v{version}  "

title_script = f"""
{Fore.RED}{line1}
{Fore.RED}{line2}
{Fore.RED}{line3}
{Fore.RED}{line4}
{Fore.RESET}{line5}
{Fore.RESET}{line6}
{Fore.RESET}{line7}
{Fore.RESET}{line8}
"""
def set_terminal_title(title):
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")

class LoadingThread(threading.Thread):
    def __init__(self, message, loading_type='default'):
        super().__init__()
        self.message = message
        self.loading_type = loading_type
        self.progress = 0
        self.stop_flag = threading.Event()

    def stop(self):
        self.stop_flag.set()
    
    def is_run(self):
        return self.is_alive()

    
    def update_progress(self, progress):
        self.progress = progress

    def loading_default(self):
        animation = "|/-\\"
        idx = 0
        while not self.stop_flag.is_set():
            print(f"{self.message} {animation[idx % len(animation)]}", end="\r")
            idx += 1
            time.sleep(0.1)
        self.clear_line()

    def loading_horizontal(self):
        bar_length = 20
        while not self.stop_flag.is_set():
            filled_length = int(bar_length * self.progress)
            bar = '#' * filled_length + '-' * (bar_length - filled_length)
            print(f"{self.message} [{bar}] {self.progress * 100:.1f}%", end="\r")
            time.sleep(0.1)
        self.clear_line()

    def clear_line(self):
        sys.stdout.write("\033[K")
        sys.stdout.flush()

    def run(self):
        if self.loading_type == 'default':
            self.loading_default()
        elif self.loading_type == 'horizontal':
            self.loading_horizontal()

def print_error(message):
    text = (f"{Fore.RED} [!] {Fore.RESET}{message}")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def print_output(message):
    text = (f"{Fore.MAGENTA} [*] {Fore.RESET}{message}")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
def print_success(message):
    text = (f"{Fore.GREEN} [√] {Fore.RESET}{message}")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
def prog(message):
    return f"{Fore.MAGENTA} [*] {Fore.RESET}{message}"

def custom_title(tit, message):
    return f"{Fore.BLUE} [{tit}] {Fore.RESET}{message}"

def print_input(message):
    text = f"{Fore.YELLOW} [?] {Fore.RESET}{message}"
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    return input()
def type_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    print()

def printc(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def youtube_downloader(url, typec):
    print_output("Url : "+url)
    aud = "audio"
    vid = "video"
    typex = "Audio" if typec in aud else "Video"
    try:
        loading = LoadingThread(prog(f'Fetching {typex} information...'), 'default')
        loading.start()
        video = YouTube(url)
        if typec in aud:
            stream = video.streams.get_audio_only()
        elif typec in vid:
            stream = video.streams.get_highest_resolution()
        else:
            loading.stop()
            loading.join() 
            print_error(f"Unexpected value : {typec}")
            sys.exit() 
            
        current_dir = os.path.dirname(os.path.abspath(__file__))
         
        if typec in aud:
            output_dir = os.path.join(current_dir, "Audio")
            output_path = os.path.join(output_dir, f"{sanitize_filename(video.title)}.mp3")
        elif typec in vid:
            output_dir = os.path.join(current_dir, "Video")
            output_path = os.path.join(output_dir, f"{sanitize_filename(video.title)}.mp4")
        os.makedirs(output_dir, exist_ok=True)
        loading.stop()
        loading.join() 
        set_terminal_title(video.title) 
        print_output(f"Title : {sanitize_filename(video.title)}")
        print_output(f"Author : {video.author}")
        print_output(f"Type : {typex}")
        loading = LoadingThread(prog('Downloading...'), 'default')
        loading.start()
        stream.download(output_path=current_dir, filename=output_path)
        loading.stop() 
        loading.join()
        print_success("Download completed.")
        print() 
    except Exception as e:
        if loading.is_run():
            loading.stop() 
            loading.join()
        print_error(str(e))

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]  # Remove newline ("\n") characters from each line
        return lines
    except FileNotFoundError:
        print_error("File not found : " + file_name)
        return []

def downloads_from_lists(txt_file, typep):
    urls = read_file(txt_file)
    index = 0;
    for url in urls:
        index+=1
        printc(custom_title(index, "Monitoring...")) 
        youtube_downloader(url, typep)

def sanitize_filename(filename):
    return filename.replace("/", "|")
    
def menu():
    print_output("Select Type")
    type_print(custom_title("1","Audio - Type downloaded is audio"))
    type_print(custom_title("2","Video - Video downloaded is full high resulotion"))
    in_type = print_input("Select : ")
    if in_type == "1":
        print() 
        print_output("Selected : Audio")
        start("a")
    elif in_type == "2":
        print() 
        print_output("Selected : Video")
        start("v")
    else:
        print_error("Invalid selected")
        time.sleep(1) 
        create()
    
def start(type):
    txtin_url = "Enter YouTube video URL : "
    url = print_input(txtin_url)
    if "http" in url:
        youtube_downloader(url,type)
    else:
        print_error("Invalid url")
        start(type)

def main():
    parser = argparse.ArgumentParser(description=" YouTube to mp4/mp3 Downloader", 
            usage="ytmp3 [OPTION] [param] [type]\n   or: ytmp3 [-p]") 
    parser.add_argument("param", type=str, nargs='?', default="",
                        help="YouTube URL to convert to mp3, or if use [-r] option, this param for a txt file")
    parser.add_argument("type", type=str, nargs='?', default="",
                        help="Type output, audio or video")
    parser.add_argument("-r", "--read", action="store_true", help="Parameter to download music from a list in a txt file")
    parser.add_argument("-p", "--path", action="store_true", help="To show main path ytmp3")
    
    parser.add_argument("-v", "--version", action="store_true", help="To show main script version")
    parser.add_argument("-u", "--uninstall", action="store_true", help="To uninstall this module script")
    args = parser.parse_args()
    if args.uninstall:
        os.system("ytmp3-uninstaller")
        sys.exit() 
    
    if args.path:
        print_output("Audio Path : " + os.path.dirname(os.path.abspath(__file__)) + "/Audio")
        print_output("Video Path : " + os.path.dirname(os.path.abspath(__file__)) + "/Video")
        sys.exit() 
    elif args.version:
        print_output("Version : v"+version) 
        sys.exit()
    elif args.param:
        if not args.read:
            youtube_downloader(args.param, args.type)
        else:
            downloads_from_lists(args.param, args.type)
    else:
        menu()
        
def create():
    os.system("clear") 
    set_terminal_title("YouTube mp3") 
    type_print(title_script)
    main()
    
if __name__ == "__main__":
    create()
    
