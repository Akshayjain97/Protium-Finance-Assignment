#!/usr/bin/env python
# coding: utf-8

# # customer14235_loan14235_crif_report

# In[90]:


import xml.etree.ElementTree as ET


# In[91]:




# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer14235_loan14235_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[92]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer14235_loan14235_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[93]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer14235_loan14235_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}

for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer16475_loan16475_crif_report

# In[94]:




# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer16475_loan16475_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[95]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer16475_loan16475_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[96]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer16475_loan16475_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}

for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer40409_loan40409_crif_report

# In[97]:




# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer40409_loan40409_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[98]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer40409_loan40409_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[99]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer40409_loan40409_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}

for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer773504_loan774538_crif_report

# In[100]:




# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer773504_loan774538_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[101]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer773504_loan774538_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[102]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer773504_loan774538_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer787561_loan788638_crif_report

# In[103]:


# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer787561_loan788638_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[104]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer787561_loan788638_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[105]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer787561_loan788638_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s  having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer794397_loan795497_crif_report

# In[106]:


# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer794397_loan795497_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[107]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer794397_loan795497_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[108]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer794397_loan795497_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer898231_loan899591_crif_report

# In[109]:


# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer898231_loan899591_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[110]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer898231_loan899591_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[111]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer898231_loan899591_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer1113697_loan1115483_crif_report

# In[112]:


# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1113697_loan1115483_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[113]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1113697_loan1115483_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[114]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1113697_loan1115483_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer1129550_loan1131339_crif_report

# In[115]:


# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1129550_loan1131339_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[116]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1129550_loan1131339_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[117]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1129550_loan1131339_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))


# # customer1195586_loan1197471_crif_report.html

# In[118]:


# Question 1: What percentage of trades are with 30+ DPD (more than 30 days past due) among all the trades available?

# Solution: 
# Assumption : considering each LOAN-DETAILS/COMBINED-PAYMENT-HISTORY as 1 trade for the calculation of Percentage 30+DPD


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1195586_loan1197471_crif_report.html.xml')
new_root = new_tree.getroot()
tot = 0
count = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if cph == None:continue
    cph = cph.text
    if cph == None:continue
    flag = 0
    tot = tot + 1
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            flag=1
            break
    
    
    count = count + flag

perc = count / tot
print("total no of Trades:", tot)
print("Count of 30+DPD Trades:", count)
print("Percentage of 30+DPD Trades:",perc*100)


# In[119]:


# Question 2:  What is the sum of total disbursed amount for all loans for each customer?

# Solution:

new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1195586_loan1197471_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
sum = 0
for i in new_root.findall(".//LOAN-DETAILS"):
    ltype = i.find('ACCT-TYPE')
    amt = i.find('DISBURSED-AMT')
    if amt == None or ltype == None:continue
    ltype = ltype.text
    if ltype == None or amt.text ==None: continue
    if ltype in dict.keys():
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = dict[ltype] + int(a)
    else: 
        amt = amt.text
        a = amt.replace(",","")
        dict[ltype] = int(a)
        
total = 0
for i in dict.keys():
    print(i ," : ",dict[i])
    total = total + dict[i]
    
print("Total loan: ", total)


# In[120]:


# Question 3. What is the maximum number of months of 30+ due per trade was there? e.g. for trade 1 there are 3 occurrences of 30+, for trade 2 there are 6 occurrences and
# for trade 3 there are 3 occurrences then the answer will be 6.

# solution 


new_tree = ET.parse('/home/leno/Documents/Coding_data/customer1195586_loan1197471_crif_report.html.xml')
new_root = new_tree.getroot()
dict = {}
for i in new_root.findall(".//LOAN-DETAILS"):
    count = 0
    ltype = i.find('ACCT-TYPE')
    cph = i.find('COMBINED-PAYMENT-HISTORY')
    if ltype == None or cph == None: continue
    cph = cph.text
    if cph == None:continue
    ltype = ltype.text
    individual = cph.split('|')
    individual = individual[:-1]
    for j in individual:
        further = j.split(',')[1]
        final = further.split('/')[0]
        if final =="XXX" or final == "DDD":continue
        elif int(final) > 30: 
            count = count + 1
            
    if ltype in dict.keys():
        dict[ltype] = dict[ltype] + count
    else: 
        dict[ltype] = count
    
    
print(dict ,"\n")
    
maxim = 0
mtype = ""
for i in dict.keys():
    if dict[i] > maxim:
        maxim = dict[i]
        mtype = i
        
print("%s having Maximum 30+DPD, which is: %d" %(mtype,maxim))

