
from time import sleep
delay = 0.4
print("Hello, welcome to to The Time Telling Tool aka T4.")
Your_timeh = input("Please input your current time in hours.\n")
if Your_timeh.isdigit():
    nothing = 'nothing'
else:
    print('Sorry, but that is not a real time! Please try again.')
    sleep(3)
    exit()
if int(Your_timeh) > 23:
    print('Sorry, but that is not a real time! Please try again.')
    sleep(3)
    exit()
sleep(0.3)
Your_timem = input("And now minutes.\n")
if Your_timem.isdigit():
    nothing = '4nothing'
else:
    print('Sorry, but that is not a real time! Please try again.')
    sleep(3)
    exit()
if int(Your_timem) > 59:
    print('Sorry, but that is not a real time! Please try again.')
    sleep(3)
    exit()
Your_zone = input("Alrighty and now input your timezone. (UTC offsets)\n")

if Your_zone == 'UTC-12':
    Your_zone_nmb = 1
elif Your_zone == 'UTC-11':
    Your_zone_nmb = 2
elif Your_zone == 'UTC-10':
    Your_zone_nmb = 3
elif Your_zone == 'UTC-9':
    Your_zone_nmb = 4
elif Your_zone == 'UTC-8':
    Your_zone_nmb = 5
elif Your_zone == 'UTC-7':
    Your_zone_nmb = 6
elif Your_zone == 'UTC-6':
    Your_zone_nmb = 7
elif Your_zone == 'UTC-5':
    Your_zone_nmb = 8
elif Your_zone == 'UTC-4':
    Your_zone_nmb = 9
elif Your_zone == 'UTC-3':
    Your_zone_nmb = 10
elif Your_zone == 'UTC-2':
    Your_zone_nmb = 11
elif Your_zone == 'UTC-1':
    Your_zone_nmb = 12
elif Your_zone == 'UTC':
    Your_zone_nmb = 13
elif Your_zone == 'UTC+1':
    Your_zone_nmb = 14
elif Your_zone == 'UTC+2':
    Your_zone_nmb = 15
elif Your_zone == 'UTC+3':
    Your_zone_nmb = 16
elif Your_zone == 'UTC+4':
    Your_zone_nmb = 17
elif Your_zone == 'UTC+5':
    Your_zone_nmb = 18
elif Your_zone == 'UTC+6':
    Your_zone_nmb = 19
elif Your_zone == 'UTC+7':
    Your_zone_nmb = 20
elif Your_zone == 'UTC+8':
    Your_zone_nmb = 21
elif Your_zone == 'UTC+9':
    Your_zone_nmb = 22
elif Your_zone == 'UTC+10':
    Your_zone_nmb = 23
elif Your_zone == 'UTC+11':
    Your_zone_nmb = 24
elif Your_zone == 'UTC+12':
    Your_zone_nmb = 25
else:
    print("Sorry, but this isn't a real timezone. (Use for eg. UTC+1)\n Please try again.")
    sleep(5)
    exit()

Other_zone = input('Ok and lastly the timezone you want your time to be converted to. (UTC offsets)\n')

if Other_zone == 'UTC-12':
    Other_zone_nmb = 1
elif Other_zone == 'UTC-11':
    Other_zone_nmb = 2
elif Other_zone == 'UTC-10':
    Other_zone_nmb = 3
elif Other_zone == 'UTC-9':
    Other_zone_nmb = 4
elif Other_zone == 'UTC-8':
    Other_zone_nmb = 5
elif Other_zone == 'UTC-7':
    Other_zone_nmb = 6
elif Other_zone == 'UTC-6':
    Other_zone_nmb = 7
elif Other_zone == 'UTC-5':
    Other_zone_nmb = 8
elif Other_zone == 'UTC-4':
    Other_zone_nmb = 9
elif Other_zone == 'UTC-3':
    Other_zone_nmb = 10
elif Other_zone == 'UTC-2':
    Other_zone_nmb = 11
elif Other_zone == 'UTC-1':
    Other_zone_nmb = 12
elif Other_zone == 'UTC':
    Other_zone_nmb = 13
elif Other_zone == 'UTC+1':
    Other_zone_nmb = 14
elif Other_zone == 'UTC+2':
    Other_zone_nmb = 15
elif Other_zone == 'UTC+3':
    Other_zone_nmb = 16
elif Other_zone == 'UTC+4':
    Other_zone_nmb = 17
elif Other_zone == 'UTC+5':
    Other_zone_nmb = 18
elif Other_zone == 'UTC+6':
    Other_zone_nmb = 19
elif Other_zone == 'UTC+7':
    Other_zone_nmb = 20
elif Other_zone == 'UTC+8':
    Other_zone_nmb = 21
elif Other_zone == 'UTC+9':
    Other_zone_nmb = 22
elif Other_zone == 'UTC+10':
    Other_zone_nmb = 23
elif Other_zone == 'UTC+11':
    Other_zone_nmb = 24
elif Other_zone == 'UTC+12':
    Other_zone_nmb = 25
else:
    print("Sorry, but this isn't a real timezone. (Use for eg. UTC+1)\n Please try again.")
    sleep(5)
    exit()
Zone_tot = Other_zone_nmb - Your_zone_nmb
Zone_tot_E = Zone_tot



Your_tot = int(Your_timeh) + int(Zone_tot_E)
Your_timemm = int(Your_timem)
Your_tot_E = Your_tot
sleep(0.4)
print("\n")
print("Loading.\n")
sleep(0.8)
print("Loading..\n")
sleep(1)
print("Loading...\n")
sleep(1.3)
print("Done!\n\n")

if Your_tot > 23:
    Your_tot_E = int(Your_tot) - 24
if Your_tot < 0:
    Your_tot_E = 24 + int(Your_tot)
if Your_timemm < 10:
    print("Thank you for using The Time Telling Tool\n" + "The time you are looking for is " + str(Your_tot_E) + ':' + '0' + str(Your_timemm) + '.\n')
else:
    print("Thank you for using The Time Telling Tool\n" + "The time you are looking for is " + str(Your_tot) + ':' + str(Your_timemm) + '.\n')
sleep(0.5)
print('___   ___  ____     ____    ____   ___   ___   ____    ____   |C|        ')
print('| |   | |  | _ \   |    \  /    |  | |   | |  |    \  /    |       ')
sleep(delay)
print('| |   | |  | __/   |     \/     |  | |   | |  |     \/     |      ')
print('| |___| |  | \     |   |    |   |  | |___| |  |   |    |   |          ')
sleep(delay)
print('|_______|  |  \    |___|    |___|  |_______|  |___|    |___|  \n\n  ')
input("Press Enter to end.")