import subprocess


class toolHandler():

    def executeScan(self, path, args, whiteList):
        cmd = path + " " + args + " " + whiteList
        p = subprocess.Popen(cmd, shell = True, stderr = subprocess.PIPE)
