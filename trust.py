import pandas as pd
trust = pd.read_csv('trust.csv')
fiz_m100 = trust['TrustIndexPSKfiz'] >= 101.
fiz_s100 = trust['TrustIndexPSKfiz'] <= 100.
fiz_m75 = trust['TrustIndexPSKfiz'] >= 75.
fiz_s75 = trust['TrustIndexPSKfiz'] <= 74.
fiz_m50 = trust['TrustIndexPSKfiz'] >= 50.
fiz_s50 = trust['TrustIndexPSKfiz'] <= 49.
fiz_m0 = trust['TrustIndexPSKfiz'] >= 1.
fiz_s0 = trust['TrustIndexPSKfiz'] <= 0.
odn_m100 = trust['TrustIndexPSKODN'] >= 101.
odn_s100 = trust['TrustIndexPSKODN'] <= 100.
odn_m75 = trust['TrustIndexPSKODN'] >= 75.
odn_s75 = trust['TrustIndexPSKODN'] <= 74.
odn_m50 = trust['TrustIndexPSKODN'] >= 50.
odn_s50 = trust['TrustIndexPSKODN'] <= 49.
odn_m0 = trust['TrustIndexPSKODN'] >= 1.
odn_s0 = trust['TrustIndexPSKODN'] <= 0.
ur_m100 = trust['TrustIndexPSKurik'] >= 101.
ur_s100 = trust['TrustIndexPSKurik'] <= 100.
ur_m75 = trust['TrustIndexPSKurik'] >= 75.
ur_s75 = trust['TrustIndexPSKurik'] <= 74.
ur_m50 = trust['TrustIndexPSKurik'] >= 50.
ur_s50 = trust['TrustIndexPSKurik'] <= 49.
ur_m0 = trust['TrustIndexPSKurik'] >= 1.
ur_s0 = trust['TrustIndexPSKurik'] <= 0.
first_group = trust[fiz_m75 & fiz_s100 & odn_m75 & odn_s100 & ur_m75 & ur_s100]
if len(first_group) != 0:
    first_group.to_csv('first_group.csv', index=False)
second_group = trust[fiz_m50 & fiz_s75 & odn_m50 & odn_s75 & ur_m50 & ur_s75]
if len(second_group) != 0:
    second_group.to_csv('second_group.csv', index=False)
third_group = trust[fiz_m0 & fiz_s50 & odn_m0 & odn_s50 & ur_m0 & ur_s50]
if len(third_group) != 0:
    third_group.to_csv('third_group.csv', index=False)
fourth_group = trust[(fiz_m100 | fiz_s0) & (odn_m100 | odn_s0) & (ur_m100 | ur_s0)]
if len(fourth_group) != 0:
    fourth_group.to_csv('fourth_group.csv', index=False)
# Берем значения из таблицы, в которых хотя бы 1 индекс превышал 100
non_unique = trust[fiz_m100 | odn_m100 | ur_m100]
# Ищем повторяющихся айди
non_unique_id = non_unique['BalanceId']
non_unique_chels = non_unique_id[non_unique_id.duplicated()]
# Получаем таблицу с повторяющимися
non_unique_table = non_unique[non_unique_id.isin(non_unique_chels)]
# Берем максимальное значение
non_unique_table['max_index'] = non_unique_table[['TrustIndexPSKfiz', 'TrustIndexPSKODN', 'TrustIndexPSKurik']].max(axis=1)
non_unique_table[['BalanceId', 'DateMonth', 'max_index']].to_csv('task2.csv', index=False)
