import pandas as pd
trust = pd.read_csv('trust.csv')
first_group = trust[(trust['TrustIndexPSKfiz'] >= 75.) & (trust['TrustIndexPSKfiz'] <= 100.) & (trust['TrustIndexPSKODN'] >= 75.) & (trust['TrustIndexPSKODN'] <= 100.) & (trust['TrustIndexPSKurik'] >= 75.) & (trust['TrustIndexPSKurik'] <= 100.)]
if len(first_group) != 0:
    first_group.to_csv('first_group.csv', index=False)
first_group = trust[(trust['TrustIndexPSKfiz'] >= 75.) & (trust['TrustIndexPSKfiz'] <= 100.) & (trust['TrustIndexPSKODN'] >= 75.) & (trust['TrustIndexPSKODN'] <= 100.) & (trust['TrustIndexPSKurik'] >= 75.) & (trust['TrustIndexPSKurik'] <= 100.)]
if len(first_group) != 0:
    first_group.to_csv('first_group.csv', index=False)
third_group = trust[(trust['TrustIndexPSKfiz'] >= 1.) & (trust['TrustIndexPSKfiz'] <= 49.) & (trust['TrustIndexPSKODN'] >= 1.) & (trust['TrustIndexPSKODN'] <= 49.) & (trust['TrustIndexPSKurik'] >= 1.) & (trust['TrustIndexPSKurik'] <= 49.)]
if len(third_group) != 0:
    third_group.to_csv('third_group.csv', index=False)
fourth_group = trust[((trust['TrustIndexPSKfiz'] >= 101.) | (trust['TrustIndexPSKfiz'] <= 0.)) & ((trust['TrustIndexPSKODN'] >= 101.) | (trust['TrustIndexPSKODN'] <= 0.)) & ((trust['TrustIndexPSKurik'] >= 101.) | (trust['TrustIndexPSKurik'] <= 0.))]
if len(fourth_group) != 0:
    fourth_group.to_csv('fourth_group.csv', index=False)
d_fiz = {}
d_odn = {}
d_ur = {}
for i in range(len(trust)):
    if trust.TrustIndexPSKfiz[i] > 101 and trust.TrustIndexPSKfiz[i] in d_fiz.keys():
        d_fiz[trust.TrustIndexPSKfiz[i]] += 1
    elif trust.TrustIndexPSKfiz[i] > 101:
        d_fiz.update({trust.TrustIndexPSKfiz[i]: 1})
    if trust.TrustIndexPSKODN[i] > 101 and trust.TrustIndexPSKODN[i] in d_odn.keys():
        d_odn[trust.TrustIndexPSKODN[i]] += 1
    elif trust.TrustIndexPSKODN[i] > 101:
        d_odn.update({trust.TrustIndexPSKODN[i]: 1})
    if trust.TrustIndexPSKurik[i] > 101 and trust.TrustIndexPSKurik[i] in d_ur.keys():
        d_ur[trust.TrustIndexPSKurik[i]] += 1
    elif trust.TrustIndexPSKurik[i] > 101:
        d_ur.update({trust.TrustIndexPSKurik[i]: 1})
ans = pd.DataFrame()
for i in range(len(trust)):
    if trust.TrustIndexPSKfiz[i] in d_fiz.keys() and d_fiz[trust.TrustIndexPSKfiz[i]] > 1:
        line = {'BalanceId': trust.BalanceId[i], 'DateMonth': trust.DateMonth[i], 'Index': trust.TrustIndexPSKfiz[i]}
        ans = ans.append(line, ignore_index=True)
    if trust.TrustIndexPSKODN[i] in d_odn.keys() and d_odn[trust.TrustIndexPSKODN[i]] > 1:
        line = {'BalanceId': trust.BalanceId[i], 'DateMonth': trust.DateMonth[i], 'Index': trust.TrustIndexPSKODN[i]}
        ans = ans.append(line, ignore_index=True)
    if trust.TrustIndexPSKurik[i] in d_ur.keys() and d_ur[trust.TrustIndexPSKurik[i]] > 1:
        line = {'BalanceId': trust.BalanceId[i], 'DateMonth': trust.DateMonth[i], 'Index': trust.TrustIndexPSKurik[i]}
        ans = ans.append(line, ignore_index=True)
ans = ans.sort_values('Index')
ans.reset_index(drop=True, inplace=True)
ans.to_csv('task2.csv', index=False)
