#A program that draws a certificate for Marathon participant
#Mholi Mncube
#created 1 May 2014 modified 11 May 2014
def main():
    name_marathon=input("Enter marathon's name: ")
    name_participant=input("Enter participant's name: ")
    year=input("Enter year: ")
    position=input("Enter position: ")
    distance=float(input("Enter distance (0.000-49.999)km: "))
    time=float(input("Enter completion time (in mins): "))
    prize=input("Enter prize money: ")
    date=input("Enter date(dd/mm/yy/): ")
    avg=round(distance/(time/60),2)
    print(date[:2],date[2:4],date[4:8],sep=".")
    a="MARATHON CERTIFICATE"
    b="PARTICIPANT'S NAME:"
    c="YEAR:"
    d="DISTANCE:"
    e="AVERAGE SPEED:"
    f="DATE:"
    g="POSITION:"
    h="COMPLETION TIME:"
    i="PRIZE:"
    j="DATE:"
    u="MARATHON'S NAME:"
    print("+",66*"-","+",sep='')
    print("|","{0:^64}".format(a),"|")
    print("|",64*" ","|")
    print("|","{0:<33}".format(u),"{0:<30}".format(name_marathon),"|")
    print("|",64*" ","|")
    print("|","{0:<33}".format(b),"{0:<30}".format(name_participant),"|")
    print("|",64*" ","|")
    print("|","{0:<5}".format(c),"{0:<27}".format(year),"{0:}".format(g),"{0:<20}".format(position),"|")
    print("|",64*" ","|")
    print("|","{0:<9}".format(d),"{0:<5}".format(round(distance,2)),"{0:<17}".format("km"),"{0:<16}".format(h),"{0:<8}".format(round(time,2)),"mins","|")
    print("|",64*" ","|")
    print("|","{0:<14}".format(e),"{0:<5}".format(round(avg,2)),"{0:<12}".format("km/hr"),"{0:<6}".format(i),"{0:<23}".format(prize),"|")
    print("|",64*" ","|")
    print("|","{0:<2}".format(j),date[:2]+"."+date[3:5]+"."+"20"+date[6:8],47*" ","|")
    print("|",64*" ","|")
    print("+",66*"-","+",sep='')
    q=input("Press enter to exit.")
main()