import numpy as np
import string
import Preprocessing as pre

"""
need savemap and old-format-files
"""

savesmap = open('savesmap.txt', "r").read().strip().split("\n")
numpack = len(savesmap)
for i in savesmap:
    tosave = []
    tosavetmp = []
    print("gathering subject : ", i)
    for Alp in string.ascii_uppercase:
        fname = i + '-' + Alp + '.txt'
        if 'Tonklar291118S4R2-' in fname or 'Tonklar291118S4-' in fname:
            dataset2 = pre.preprocess("saves/" + fname, method="bandpass", index=1)
            # print(aaa.shape)
            tosavetmp.append(dataset2)

        dataset = pre.preprocess("saves/" + fname, method="bandpass")
        tosave.append(dataset)

    saveat = "NPsaves/" + i + ".npy"
    savedata = np.array(tosave)
    print(savedata.shape)
    np.save(saveat, np.array(savedata), allow_pickle=False)
    if 'Tonklar291118S4R2-' in fname or 'Tonklar291118S4-' in fname:
        tmpsaveat = "NPsaves/" + i + "P2.npy"
        tmpsavedata = np.array(tosavetmp)
        print(tmpsavedata.shape, "tmp")
        np.save(tmpsaveat, np.array(tmpsavedata), allow_pickle=False)
