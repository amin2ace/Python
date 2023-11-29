from math import pow
import argparse


###open((os.path.join(os.getcwd(), ".venv", "Parssing", "Morse.py")),'w')
def sort(numbers, descending):
    args_sorted = []
    ### If optional arg was given then 
    if descending:
        args_sorted = sorted(numbers, reverse=True)
    else:
        args_sorted = sorted(numbers)
    return args_sorted
    

def sum(numbers):
    sum = 0
    for n in numbers:
        sum += int(n)
    return sum

def avg(numbers):
    s = sum(numbers)/len(numbers)
    return s

def root(numbers, r):
    if r <= 1 or r == 0:
        return numbers
    rooted_num = []
    for i in numbers:
        rooted_num.append(f"{round(pow(i, 1/r), 5):.5f}")
        ### To prevent from division by zero error round the power result
    return rooted_num

def power(numbers, p):
    powerd_num = []
    for i in numbers:
        powerd_num.append(int(pow(i,p)))
    return powerd_num

try:
    act = argparse.ArgumentParser(description="### You can choose your aption of 'Sum' , 'min' , 'Max' , 'avg' , 'sort' , 'Power' , 'root'###")
except:
    print("The following arguments are required: action, numbers\naction: (a)verage, (m)inimum, (M)aximum, (P)ower, (r)oot, (s)ort, (S)um")
else:
    act.add_argument("action", default="sum", type=str, help="min(m) , Max(M) , Sum(S) , avg(a) , sort(s) , Power(P) , root(r)")
    act.add_argument("numbers", type=int, nargs=2, help="This mini parse will do action on your int entites")
    act.add_argument("--descending", default=False, action="store_true", help="will sort items Descending")
    act.add_argument("--root", default=2, type=int, help="Root number of the number")
    act.add_argument("--power", default=2, type=int, help="Number of power for exponential calculation")
    args = act.parse_args()


    if args.action == 's':
        print(f"your sorted items in order are: {sort(args.numbers, args.descending)}")
    elif args.action == 'S':
        print(f"The numbers sum is: {sum(args.numbers)}")
    elif args.action == 'a':
        print(f"Average of the numbers is : {avg(args.numbers):.3f}")
    elif args.action == 'M':
        print(f"Maximum number is: {max(args.numbers)}")
    elif args.action == 'm':
        print(f"Minimum number is: {min(args.numbers)}")
    elif args.action == 'r':
        print(f"The {args.root} d\\th root of the given numbers: {root(args.numbers, args.root)}")
    elif args.action == 'P':
        print(f"Numbers with power {args.power} are {power(args.numbers, args.power)}")