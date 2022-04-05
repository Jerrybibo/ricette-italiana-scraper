from subprocess import Popen, PIPE

build_process = Popen(['pyinstaller', '--name=ricette-italiana-scraper',
                       '--onefile', 'main.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = build_process.communicate()