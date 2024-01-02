from django.http import HttpResponse
from django.shortcuts import render


def index2(request):
    # return HttpResponse(request, 'index2.html')
    return render(request, 'index2.html')


from playsound import playsound
print ("Select Your Song List:\n1. Agar Tum Mil Jao (Zeher)\n2. Wo Ladki (Andhadhun)\n3. Ajab Si (Om Shanti Om)\n4. Tum Jo Aaye (Once Upon A Time In Mumbai)\n5. Khuda Jaane (Bachna Ae Haseeno)\n6. Teri Yaadon Mein (The Killer)\n7. Tu Hi Meri Shab Hai (Gangster)\n8. Haa Tu Hai (Jannat)\n9. Pehli Nazar Mein (Race)\n10. Kya Mujhe Pyar Hai (Woh Lamhe)")

song = int(input())

if song==1:
    playsound("C:/Users/Acer/Music/Zeher/01 - Zeher - Agar Tum Mil Jao (Female)  www.DJMaza.Com .mp3")
elif song==2:
    playsound("C:/Users/Acer/Music/Andhadhun/05 Wo Ladki - Andhadhun.mp3")
elif song==3:
    playsound("C:/Users/Acer/Music/Om Shanti Om/Ajab_Si-VmusiQ.Com.mp3")
elif song==4:
    playsound("C:/Users/Acer/Music/Once Upon A Time In Mumbai/[Songs.PK] Once Upon A Time In Mumbai - 02 - Tum Jo Aaye.mp3")
elif song==5:
    playsound("C:/Users/Acer/Music/KK/Khuda Jaane (Bachna Ae Haseeno) - K.K - 320Kbps.mp3")
elif song==6:
    playsound("C:/Users/Acer/Music/KK/Teri Yaadon Mein (The Killer) - K.K - 320Kbps.mp3")
elif song==7:
    playsound("C:/Users/Acer/Music/KK/Tu Hi Meri Shab Hai (Gangster) - K.K - 320Kbps.mp3")
elif song==8:
    playsound("C:/Users/Acer/Music/Jannat [In Search of Heaven] (2008) Mp3 Songs  SongsMp3.Com/Haan-Tu-Hain.mp3")
elif song==9:
    playsound("C:/Users/Acer/Music/Race/Race 2008 - Pehli Nazar Mein.mp3")
elif song==10:
    playsound("C:/Users/Acer/Music/KK/Kya Mujhe Pyar Hai (Woh Lamhe) - K.K - 320Kbps.mp3")
else:
    print("Invalid Selection")