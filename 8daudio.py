from pydub import AudioSegment
from time import sleep

# UPDATE: 10-05-2021
# Have'nt been updated for like 2 years now, will add some new features soon

print("8D AUDIO CONVERTER FOR MP3s ~by WinterSoldier\n\n Contact the developer for any help")
print("Make sure that you have 'ffmpeg' folder placed in the same directory\n\n")
print("Please place the song in the same folder as this application and rename it to 'test'\n\n\n")
input('Hit enter when done\n\n')
sound = AudioSegment.from_mp3("test.mp3")



print("Type: 'normal' to use default settings or 'custom' to use your custom settings")
inp = input("")

if inp=='normal':
    adjust_jump =8
    segment_length = 200
    
elif inp=='custom':
    inp2 = input("Please input custom jump speed (INTEGER value between 2 to 20) >>>")
    adjust_jump = int(inp2)
    inp3 = input("Please input the segment length(INTEGER value between 200 to 5000) >>>")
    segment_length = int(inp3)
    
else:
    print("Wrong choice...Run Again")

_8d = sound[0]
pan_limit=[]

limit_left  = -100


for i in range(100):
    if int(limit_left) >= 100:
        break
    pan_limit.append(limit_left)
    limit_left+=adjust_jump

pan_limit.append(100)

for i in range(0,len(pan_limit)):
    pan_limit[i] = pan_limit[i] /100

print(len(pan_limit))
print(pan_limit)
print("Please wait...it may take a few seconds")
sleep(2)




c=0
flag = True


for i in range(0,len(sound)-segment_length, segment_length):

    peice = sound[i:i+segment_length]

    if c==0 and not flag:
        flag =True
        c=c+2

    if c==len(pan_limit):
        c = c-2
        flag =False

    if flag:
        panned = peice.pan(pan_limit[c])
        c+=1


    else:
        panned = peice.pan(pan_limit[c])
        c-=1

    


    _8d =_8d+panned
    print(panned)
	






print(len(_8d))
print("Writing the audio from the MEMORY to the drive")

# lets save it!
out_f = open("compiled.mp3", 'wb')

_8d.export(out_f, format='mp3')







