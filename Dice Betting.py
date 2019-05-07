import random 
import matplotlib
import matplotlib.pyplot as plt
import argparse
def Roll_Dice():
    roll=random.randint(1,100)
    if roll==100:
        return(False)
    elif roll in range(1,51):
        return(False)
    elif roll in range(51,100):
        return(True)
########################################################################################
def Single_bettor(Budget,Initial_Wager,Wager_Count,verbose):
    value=Budget
    wager=Initial_Wager
    wX=[]
    vY=[]
    current_wager=0
    while current_wager<=Wager_Count:
        if Roll_Dice():
            value+=wager
            wX.append(current_wager)
            vY.append(value)
            if verbose:
                print("You win, Here is your {}$".format(wager))
        else:
            value-=wager
            wX.append(current_wager)
            vY.append(value)
            if verbose:
                print("You Win,You owe us {}$".format(wager))
        current_wager+=1
    if value<=0:
        value="Broke"
        if verbose:
            print("You are Broke ")
    plt.plot(wX,vY)
##########################################################################################    
def Multiple_bettors():
    parser=argparse.ArgumentParser(description="Simulate Multiple Bettors and Results")
    parser.add_argument("--Bgt", default=5000,type=int, metavar='int', help="Budget of Bettors")
    parser.add_argument("--InWage",default=50,type=int,metavar='int',help="Initial wager amount")
    parser.add_argument("--BtCnt",default=50,action="store_true",help="Bettors count")
    parser.add_argument("--WgCnt",default=10000,action="store_true",help="NO of wagers per bettor")
    parser.add_argument("--verbose",default=False,action="store_true",help="Display the result of each trial")
    args=parser.parse_args()
    ########################
    A=list(range(args.WgCnt))
    B=[]
    for i in range(args.WgCnt):
        B.append(args.Bgt)
    plt.plot(A,B)
    #######################
    
    for i in range(args.BtCnt):
        Single_bettor(args.Bgt,args.InWage,args.WgCnt,args.verbose)
        #print("Final value ={} \n\n".format(value))
##############################################################################################
if __name__ =="__main__":
    Multiple_bettors()
    plt.ylabel("Account Value")
    plt.xlabel("Wager Count")
    plt.show()
