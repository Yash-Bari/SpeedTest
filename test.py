from tkinter import *
import speedtest
import threading

def speedcheck():
    # Display loading message
    lab_down.config(text="Testing...")
    lab_up.config(text="Testing...")

    # Create a new thread to perform the speed test
    t = threading.Thread(target=perform_speed_test)
    t.start()

def perform_speed_test():
    # This function will be executed in a separate thread
    sp = speedtest.Speedtest()
    sp.get_best_server()

    # Download speed test in a separate thread
    download_thread = threading.Thread(target=perform_download, args=(sp,))
    download_thread.start()

    # Upload speed test
    upload_thread = threading.Thread(target=perform_upload, args=(sp,))
    upload_thread.start()

def perform_download(sp):
    # Perform download speed test
    download_speed = sp.download()
    down = str(round(download_speed / (10**6), 3)) + " Mbps"
    lab_down.config(text=down)

def perform_upload(sp):
    # Perform upload speed test
    upload_speed = sp.upload()
    up = str(round(upload_speed / (10**6), 3)) + " Mbps"
    lab_up.config(text=up)

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x650")
sp.config(bg="Blue")

label_main = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Blue", fg="White")
label_main.place(x=60, y=40, height=50, width=380)

label_download = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"))
label_download.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

label_upload = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"))
label_upload.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button_check = Button(sp, text="Check Speed", font=("Time New Roman", 20, "bold"), command=speedcheck)
button_check.place(x=160, y=450, height=50, width=180)

sp.mainloop()
