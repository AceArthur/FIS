def getMembership(mf,degree,x):
    a,b,c,d = mf[degree]
    if x<=a or x>=d:
        return 0.0
    else:
        if a == b:
            return 1.0 if a<=x<=c else (d-x)/(d-c)
        if c == d:
            return 1.0 if b<=x<=d else (x-a)/(b-a)
        else:
            if a<=x<=b:
                return 1.0 if a == b else (x-a)/(b-a)
            elif c<=x<=d:
                return 1.0 if b == c else (d-x)/(d-c)
            else:
                return 1.0

def FIS(get_speed,get_dist):
    mf_speed = {'LOW': (0,0,10,20),'MEDIUM':(15,25,35,45),'HIGH':(40,50,60,60)}
    mf_closeness = {'LOW':(1.0,1.5,2.0,2.0) ,'MEDIUM':(0.5,0.75,1.0,1.25),'HIGH':(0,0,0.25,0.75)}
    mfs = [[mf_speed,get_speed],[mf_closeness,get_dist]]
    
    rulebase = [['HIGH',-10],['MEDIUM',5],['LOW',10]]

    sum_w,sum_v = 0,0
    
    for j in xrange(len(mfs)):
        for i in rulebase:
            weight = getMembership(mfs[j][0],i[0],mfs[j][1])
            sum_w += weight
            sum_v += weight * i[-1]

    return sum_v / sum_w

get_speed = int(raw_input("Your Speend? (0-60 mph)"))
get_dist = float(raw_input("Your Distance to Target? (0-2.0 miles)"))
print "Adjust Speed by:", FIS(get_speed,get_dist), "mph."
