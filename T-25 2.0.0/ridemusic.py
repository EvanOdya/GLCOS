import winsound
import time

#On ride music library
def song1():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Cold.wav', winsound.SND_ASYNC)
song1n = "1- Cold"
def song2():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Heroes_Tonight.wav', winsound.SND_ASYNC)
song2n = "2- Heros Tonight"
def song3():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Light_It_Up.wav', winsound.SND_ASYNC)
song3n = '3- Light It Up'
def song5():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Lost_Sky.wav', winsound.SND_ASYNC)
song5n = '5- Lost Sky'
def song6():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\sop_gun_Anthem.wav', winsound.SND_ASYNC)
song6n = '6- Top Gun Anthem'

##Plays E-stop warning sound
def estopsound():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zirbus_autopilot.wav', winsound.SND_ASYNC)

##Plays error sound
def errorsound():
   winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\error_sound2.wav', winsound.SND_ASYNC)
   time.sleep(1)

