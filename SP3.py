from art import *
import os
import subprocess

class SP3:
    def __init__(self):
        self.data = []

    def run(self):
        os.chdir('video')
        tprint("Welcome again Javi!")
        print("Welcome to SP3 of the Audio and Video Encoding Systems.")

        while (1):
            print('------------------------------------------')
            print("Please select what exercise you'd like to run:")
            print("1. Exercise 1.")
            print("2. Exercise 2.")
            print("3. Exercise 3.")
            print("4. Exercise 4.")
            print("0. Exit.")
            option = input('Select your option here: ')
            if option != "0":
                print('------------------------------------------')
                print('EXERCISE ' + str(option))
                print('------------------------------------------')

            if option == "1":
                self.exercise1()
            elif option == "2":
                self.exercise2()
            elif option == "3":
                self.exercise3()

            elif option == "4":
                self.exercise4()

            elif option == "0":
                print('------------------------------------------')
                print("Thanks for you attention!")
                tprint("Goodbye Javi!")
                break
            else:
                print("The option you wrote is not valid!")
    def exercise1(self):
        start = "00:00:20.0"
        ending = "00:00:30.0"
        print('Converting BBB.mp4...')

        print('...into 720p.')
        subprocess.call(['ffmpeg', '-i', 'bbb.mp4', '-ss', start, '-vf', 'scale=1280:720', '-t', ending, 'bbb_720p.mp4'])
        print('...into 480p.')
        subprocess.call(['ffmpeg', '-i', 'bbb.mp4', '-ss', start, '-vf', 'scale=720:480', '-t', ending, 'bbb_480p.mp4'])
        print('...into 360x240.')
        subprocess.call(['ffmpeg', '-i', 'bbb.mp4', '-ss', start, '-vf', 'scale=360:240', '-t', ending, 'bbb_360_240.mp4'])
        print('...into 160x120.')
        subprocess.call(['ffmpeg', '-i', 'bbb.mp4', '-ss', start, '-vf', 'scale=160:120', '-t', ending, 'bbb_160_120.mp4'])

        # Reference: https://trac.ffmpeg.org/wiki
        print('Converting file into VP8...')
        subprocess.call('ffmpeg -i bbb_720p.mp4 -c:v libvpx -crf 30 -b:v 0 -c:a libopus -b:a 128k bbb_vp8.webm', shell=True)
        print('Converting file into VP9...')
        subprocess.call('ffmpeg -i bbb_480p.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a libopus -b:a 128k bbb_vp9.webm', shell=True)
        print('Converting file into H265...')
        subprocess.call('ffmpeg - i bbb_360_240.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k bbb_h265.mp4', shell=True)
        print('Converting file into AV10...')
        subprocess.call('ffmpeg -i bbb_160_120.mp4 -c:v libaom-av1 -crf 30 -b:v 0 bbb_av1.mkv', shell=True)

    def exercise2(self):
        subprocess.call('ffplay -i bbb_vp8.webm -i bbb_vp9.webm -i bbb_h265.mp4 -i bbb_av1.mkv -filter_complex "[0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; [2:v] setpts=PTS-STARTPTS, scale=qvga [a2]; [3:v] setpts=PTS-STARTPTS, scale=qvga [a3]; [a0][a1][a2][a3]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[out]" -map "[out]" -c:v libx264 -f matroska')

    def exercise3(self):
        # Reference: https://ffmpeg.org/ffmpeg-devices.html
        subprocess.call('ffmpeg -re -i bbb.mp4 -c:v copy -f mpegts udp://@localhost:8080', shell=True)

    def exercise4(self):
        ip_address = input('Introduce the IP address: ')
        port = input('Introduce the port: ')
        subprocess.call(['ffmpeg', '-re', '-i', 'bbb.mp4', '-c:v', 'copy', '-f', 'mpegts', 'udp://@', ip_address, ':', port])