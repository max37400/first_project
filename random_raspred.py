def raspr_12(add='data.xlsx'):  
    import pandas as pd
    import numpy as np
    data=pd.read_excel(add)
    teams={'team1':[],'team2':[],'team3':[],'team4':[],'team5':[],'team6':[],'team7':[],'team8':[],'team9':[],'team10':[],'team11':[],'team12':[]}
    raw_data=[]
    keys=['team1','team2','team3','team4','team5','team6','team7','team8','team9','team10','team11','team12']
    i=0
    for name in data.columns:
        l=list(data[name])
        raw_data.append(l)
    for lis in raw_data:
        for key in keys:
            k=lis.pop(np.random.randint(len(lis)))
            teams[key].append(k)
    for ost in raw_data:
        while len(ost)!=0:
            l=ost.pop()
            teams[keys[i]].append(l)
            i+=1
    new_data = pd.DataFrame(data=teams)
    new_data.to_excel("raspred_12.xlsx")
def  raspr_10(add='data.xlsx'):
    import pandas as pd
    import numpy as np
    data=pd.read_excel(add)
    teams={'team1':[],'team2':[],'team3':[],'team4':[],'team5':[],'team6':[],'team7':[],'team8':[],'team9':[],'team10':[]}
    raw_data=[]
    keys=['team1','team2','team3','team4','team5','team6','team7','team8','team9','team10']
    i=0
    for name in data.columns:
        l=list(data[name])
        raw_data.append(l)
    for lis in raw_data:
        for key in keys:
            k=lis.pop(np.random.randint(len(lis)))
            teams[key].append(k)
    for ost in raw_data:
        while len(ost)!=0:
            if i>=len(keys):
                i=0
            l=ost.pop()
            teams[keys[i]].append(l)
            i+=1
    for i in ['team5','team6','team7','team8','team9','team10']:
        teams[i].append(' ')
    new_data = pd.DataFrame(data=teams)
    new_data.to_excel("raspred_10.xlsx")
def raspr_7(add='data.xslx'):
    import pandas as pd
    import numpy as np
    data=pd.read_excel(add)
    teams={'team1':[],'team2':[],'team3':[],'team4':[],'team5':[],'team6':[],'team7':[]}
    raw_data=[]
    keys=['team1','team2','team3','team4','team5','team6','team7']
    i=0
    for name in data.columns:
        l=list(data[name])
        raw_data.append(l)
    for lis in raw_data:
        for key in keys:
            k=lis.pop(np.random.randint(len(lis)))
            teams[key].append(k)
    for lis in raw_data:
        for key in keys:
            k=lis.pop(np.random.randint(len(lis)))
            teams[key].append(k)
    new_data = pd.DataFrame(data=teams)
    new_data.to_excel("raspred_7.xlsx")
def raspr_9(add='data.xlsx'):
    import pandas as pd
    import numpy as np
    data=pd.read_excel(add)
    teams={'team1':[],'team2':[],'team3':[],'team4':[],'team5':[],'team6':[],'team7':[],'team8':[],'team9':[],'team10':[]}
    raw_data=[]
    keys=['team1','team2','team3','team4','team5','team6','team7','team8','team9','team10']
    i=0
    t=2
    np.random.seed(42)
    for name in data.columns:
        l=list(data[name])
        raw_data.append(l)
    for lis in raw_data:
        for key in keys:
            k=lis.pop(np.random.randint(len(lis)))
            teams[key].append(k)
    for ost in raw_data:
        while len(ost)!=0:
            if i>=len(keys):
                i=0
            l=ost.pop()
            teams[keys[i]].append(l)
            i+=1
    for i in ['team5','team6','team7','team8','team9','team10']:
        teams[i].append(' ')
    for i in teams['team1']:
        teams['team{}'.format(str(t))].append(i)
        t+=1
    r=dict(teams)
    del r['team1']
    new_data = pd.DataFrame(data=r)
    new_data.to_excel("raspred_9.xlsx")
