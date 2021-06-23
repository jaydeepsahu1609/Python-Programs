import platform

def SystemInfo():
    print('-'*22, "System Information", '-'*22)
    uname = platform.uname()     #user
    print(f"\tSystem : {uname.system}")
    print(f"\tNode Name : {uname.node}")
    print(f"\tRelease : {uname.release}")
    print(f"\tVersion : {uname.version}")
    print(f"\tMachine : {uname.machine}")
    print(f"\tProcessor : {uname.processor}")
    print('-'*62)
    print()

if __name__ == '__main__':
    SystemInfo()