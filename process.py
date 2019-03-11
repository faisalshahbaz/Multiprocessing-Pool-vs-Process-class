
from multiprocessing import Process


def printFunction(country='Pakistan'):
    print('The name of Country is : ', country)

if __name__ == "__main__":
    names = ['Turkey', 'China', 'Iran']
    procs = []
    proc = Process(target=printFunction)
    procs.append(proc)
    proc.start()

    for name in names:
        proc = Process(target=printFunction, args=(name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

