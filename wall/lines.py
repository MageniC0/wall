import os

def dn(s):
    a_=[]
    a0=os.path.abspath(s)
    for a1,_,a2 in os.walk(a0):
        a3 = a1.replace(a0,'').count(os.sep)
        a_.append("|   "*a3+f"[{os.path.basename(a1)}]\n")
        a_.extend("|   "*(a3+1)+f"{a6}\n" for a6 in a2)
    print("\033[90m"+"".join(a_))

def io(s):
    if not os.path.exists(s):
        os.makedirs(s)
        print(f"creat floder \033[94m{s}\033[0m.")
    else:
        print(f"floder \033[94m{s}\033[0m is being.")
    dn(s)

def set_up():
    io("terrain")
    io("textures")

if __name__ == "__main__":
    set_up()