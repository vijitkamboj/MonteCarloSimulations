'''Simulating the Monty hills contest'''
import argparse,random
def simulate(Num_Doors,Switch,verbose):
    closed_doors=list(range(Num_Doors))
    winning_door=random.randint(0,Num_Doors-1)
    if verbose:
        print("winning prize is behind door no.{}".format(winning_door+1))

    choice=random.randint(0,Num_Doors-1)
    if verbose:
        print("Contestant chooses door {}".format(choice+1))
    
    while len(closed_doors)>2:
        door_remove=random.choice(closed_doors)
        if door_remove==winning_door or door_remove==choice:
            continue
        closed_doors.remove(door_remove)
        if verbose:
            print("Host removes door {}".format(door_remove+1))
    assert len(closed_doors) == 2

    if Switch:
        closed_doors.remove(choice)
        choice=closed_doors[0]
        if verbose:
            print("Contestant switches from door {}".format(choice+1),end="")
            print("to {}".format(choice+1))
    
    if choice==winning_door:
        won=True
    else:
        won=False

    if verbose:
        if won==True:
            print("Contestant Won",end="\n\n")
        else:
            print("Contestant Loses",end="\n\n")
    return(won)
########################################################3

def trials():
    parser=argparse.ArgumentParser(description="Simulate the monty hall problem")
    parser.add_argument("--doors", default=5,type=int, metavar='int', help="No of doors offered to contestant")
    parser.add_argument("--trials",default=50000,type=int,metavar='int',help="No of trials to perform")
    parser.add_argument("--verbose",default=False,action="store_true",help="Display the result of each trial")
    args=parser.parse_args()

    print("Simulating {} trials".format(args.trials))

    winning_non_switchers=0
    winning_switchers=0

    for i in range(args.trials):
        won=simulate(args.doors,Switch=False,verbose=args.verbose)
        if won==True:
            winning_non_switchers+=1
        won=simulate(args.doors,Switch=True,verbose=args.verbose)
        if won==True:
            winning_switchers+=1
    
    print("Switching won {0} times out of {1}({2}% of the time)".format(winning_switchers,args.trials,(winning_switchers/args.trials * 100)))
    print("Not Switching won {0} times out of {1}({2}% of the time)".format(winning_non_switchers,args.trials,(winning_non_switchers/args.trials * 100)))
if __name__=="__main__":
    trials()


    



        
