import subprocess

# subprocess.run("service kibana status")

# subprocess.run(["echo", "hello "])

def maisy(name, number):
    if number == 4:
        print("mika is a terrible dancer")
    else:
        subprocess.run(["echo", "hello "])


def weston():
    return maisy('mika', 4)


weston()