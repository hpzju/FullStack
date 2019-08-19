import os


def child():
    print('Hello from child',  os.getpid())
    os._exit(0)
    # else goes back to parent loop


def parent():
    while True:
        if hasattr(os, 'fork'):
            # we don't care what OS, so long as it allows forking
            newpid = os.fork()
        else:
            newpid = os.getpid()

        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)

        if input() == 'q':
            break


if __name__ == "__main__":
    parent()
