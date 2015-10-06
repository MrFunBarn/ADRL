import re


def read_arcsat_obs_log(logName):
    # The Latin-1 encoding is needed because of the degree symobl.
    log = open(logName,'r', encoding='Latin-1')
    log = log.read()
    return log

def extract_arcsat_log(log):
    filename = re.findall(r'(Imaging to) (\S+)', log)
    print(filename[:].group(1))
