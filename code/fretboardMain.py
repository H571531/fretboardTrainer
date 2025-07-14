import random as rnd
import time

fretBoard={'E':[['E,F,F#,G,G#,A,A#,B,C,C#,D,D#'],['A,A#,B,C,C#,D,D#,E,F,F#,G,G#'],['D,D#,E,F,F#,G,G#,A,A#,B,C,C#'],['G,G#,A,A#,B,C,C#,D,D#,E,F,F#'],['B,C,C#,D,D#,E,F,F#,G,G#,A,A#'],['E,F,F#,G,G#,A,A#,B,C,C#,D,D#']],
           'D':[['D,D#,E,F,F#,G,G#,A,A#,B,C,C#'],['G,G#,A,A#,B,C,C#,D,D#,E,F,F#'],['C,C#,D,D#,E,F,F#,G,G#,A,A#,B'],['F,F#,G,G#,A,A#,B,C,C#,D,D#,E'],['A,A#,B,C,C#,D,D#,E,F,F#,G,G#'],['D,D#,E,F,F#,G,G#,A,A#,B,C,C#']],
           'B':[['B,C,C#,D,D#,E,F,F#,G,G#,A,A#'],['E,F,F#,G,G#,A,A#,B,C,C#,D,D#'],['A,A#,B,C,C#,D,D#,E,F,F#,G,G#'],['D,D#,E,F,F#,G,G#,A,A#,B,C,C#'],['F#,G,G#,A,A#,B,C,C#,D,D#,E,F'],['B,C,C#,D,D#,E,F,F#,G,G#,A,A#']]}
noteArray=[]
stringTranslator={'E':{0:'E',1:'A',2:'D',3:'G',4:'B',5:'E'},
                  'D':{0:'D',1:'G',2:'C',3:'F',4:'A',5:'D'},
                  'B':{0:'B',1:'E',2:'A',3:'D',4:'F#',5:'B'}
                  }

def findAvg(timeArray):
    tot=0
    for t in timeArray:
        tot=t+tot
    return tot/len(timeArray)

def main():
    tuning='E'
    for i in range(len(fretBoard[tuning])):
        for n in fretBoard[tuning][i]:
            notes=n.split(',')
            noteArray.append(notes)
     
    
    lp=True
    timeArray=[]
    while(lp):
        ranString=rnd.randint(0,5)
        ranFret=rnd.randint(0,11)  
        st=time.perf_counter()
        answer=noteArray[ranString][ranFret]
        userIn=''
        print(f"What note is on string: {stringTranslator[tuning][ranString]} fret: {ranFret}")
        while(answer!=userIn):
            userIn=input()
            if(answer!=userIn):
                print('Wrong...')
        et=time.perf_counter()
        timeUsed=et-st
        print(f"You spent {timeUsed:.1f} seconds")
        a=input("again? (y/n)")
        lp=(a=="y")
        timeArray.append(timeUsed)

    print(f"You spent on average: {findAvg(timeArray):.1f} seconds")


if __name__ == '__main__':
    main()