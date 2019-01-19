import numpy as np
import Preprocessing as pre

def multibandfeat(name, index=0):
    feat = []
    kaiser, phase, power = pre.preprocess(name, index)
    print(np.asarray(kaiser).shape)
    # print(np.ravel(kaiser[:,1,:]).shape)
    return kaiser[:, 1:3, :]

def check_score(model, data_test, label_test):
    dic = {}
    count = 0
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dic[count] = i  # {0:'A',1:'B',...,25:'Z'}
        count = count + 1

    Prob = []
    cc = 0
    answer=model.decision_function(data_test)
    print(len(answer[0]))

    for trials in answer:

        Seq = []
        for j in range(len(trials)):  # 26 letter
            Seq.append([-trials[j], j])  # กำกับ percentage ด้วย Alphabet_index
        Seq.sort() # sort percentage
        print(Seq[0],model.predict([data_test[cc]]))
        w = []
        is_valid = 0
        for t in Seq[0:9]:  # เลือก 9 ตัวที่มี percent มากสุด
            w.append(dic[t[1]])  # แปรผลเป็นตัวอักษร
        Prob.append(w)
        # print(w,label_test[cc])
        cc += 1
        #print(np.asarray(Prob))
    # print(np.asarray(Prob).shape)
    score = 0
    miss = []
    for i in range(len(label_test)):
        if label_test[i] in Prob[i]:
            score = score + 1  # นับคะแนนความถูกต้อง
        else:
            # print(label_test[i],Prob[i])
            miss.append(label_test[i])
    # print(score)
    # print(score*100/len(label_test))
    # print(sorted(miss))
    return score * 100 / len(label_test)