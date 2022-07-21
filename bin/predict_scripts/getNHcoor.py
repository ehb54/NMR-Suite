import numpy as np

from predict_scripts.select import select
#from select import select
    
def getNHcoor(coor, atnam, at_res, reslst, offs = 0):
    selN = select(atnam, at_res, reslst, 'N ', 2)
    iN = selN.size
    if offs == -1:
        selH = select(atnam, at_res, reslst, ' H ', 3, -1)
    else:
        selH = select(atnam, at_res, reslst, 'HN', 2, offs)
    iH = selH.size
    if iH == 0:
        print ("offs = {}: no amide protons found!".format(str(offs)))
        NH_coor = []
        return NH_coor
    print ("{} amide protons found".format(str(iH)))
    NH_coor = np.full((iH, 7), float("nan"))
    NH_coor[:, 0] = np.add(at_res[selH, 1].flatten(), 1)
    for i in range(iH): 
        for j in range(iN): 
            if (at_res[selN[j], 1] == at_res[selH[i], 1]):
                NH_coor[i, 1:4] = coor[selN[j], :]
                NH_coor[i, 4:7] = coor[selH[i], :]
                break
    return NH_coor

