# Section - A
# Source Code


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
Train=pd.read_csv(r'D:\train.csv')
Test=pd.read_csv(r'D:\test.csv')
Train.columns
Test.columns
Train.dtypes
print("Shape train dataset", Train.shape)
Train.head()
print("Shape test dataset", Test.shape)
Test.head()
Train["Loan_Status"].count()
Train["Loan_Status"].value_counts()
Train['Loan_Status'].value_counts(normalize=True)*100
Train['Loan_Status'].value_counts(normalize=True).plot.bar(title='Loan Status')
plt.ylabel('Percentage ')
plt.xlabel('Status')
plt.show()
print("loan of 422(approx 70%) people out of 614 has been approved.")
print("Categorical features: These features have categories (Gender, Married, Self_Employed, Credit_History, Loan_Status)")
Train["Gender"].count()
Train['Gender'].value_counts()
Train['Gender'].value_counts(normalize=True)*100
Train['Gender'].value_counts(normalize=True).plot.bar(title ='Gender of the loan applicant data')
print("QUESTION 1-a: Find out the number of male and female in loan applicants data.")
plt.xlabel('Gender of loan applicant')
plt.ylabel('Percentage')
plt.show()
print("Answer of  QUESTION 1-a: ")
print( "There are 81% of Male and 19% of Female in loan applications" )
Train["Married"].count()
Train["Married"].value_counts()
print("Total number of people: 611")
print("Married: 398")
print("Unmarried: 213")
Train['Married'].value_counts(normalize=True)*100
print("QUESTION 1-b: Find out the number of married and unmarried loan applicants.")
Train['Married'].value_counts(normalize=True).plot.bar(title='Martial Status of Loan applicant')
plt.xlabel('Martial Status')
plt.ylabel('Percentage')
plt.show()
print("Answer  of QUESTION 1-b:")
print("Number of married people : 65%")
print("Number of unmarried people : 35%")
Train["Self_Employed"].count()
Train['Self_Employed'].value_counts()
Train['Self_Employed'].value_counts(normalize=True)*100
print("QUESTION 1-c: Find out the overall dependent status in the dataset.")
Train['Self_Employed'].value_counts(normalize=True).plot.bar(title='Dependent Status')
plt.xlabel('Dependent Status')
plt.ylabel('Percentage')
plt.show()
print("Answer for QUESTION 1-c: ")
print("In a total of 582 people - 14% are SelfEmployed and - 86% are Not SelfEmployed")
Train["Education"].count()
Train["Education"].value_counts()
Train["Education"].value_counts(normalize=True)*1
print(" QUESTION 1-d: Find the count how many loan applicants are graduate and non graduate.")
Train["Education"].value_counts(normalize=True).plot.bar(title = "Graduate or not")
plt.xlabel('Graduate')
plt.ylabel('Percentage')
plt.show()
print("Answer for QUESTION 1-d:  ")
print("Total number of People : 614")
print("78% are Graduated  ")
print("22% are not Graduated ")
Train["Property_Area"].count()
Train["Property_Area"].value_counts()
Train["Property_Area"].value_counts(normalize=True)*100
print("QUESTION 1-e: Find out the count how many loan applicants property lies in urban, rural and semi-urban areas.")
Train["Property_Area"].value_counts(normalize=True).plot.bar(title="Area of Applicant")
plt.xlabel('Area')
plt.ylabel('Percentage')
plt.show()
print("Answer of Question 1-E:")
print("Applicants from Semiurban area = 38%  ")
print("Applicants from Urban area = 33% ")
print("Applicants from Rural area = 29% ")
Train["Credit_History"].count()
Train["Credit_History"].value_counts()
Train['Credit_History'].value_counts(normalize=True)*100
Train['Credit_History'].value_counts(normalize=True).plot.bar(title='Credit History')
plt.xlabel('Debt')
plt.ylabel('Percentage')
plt.show()
print("QUESTION 3:")
print("To visualize and plot the distribution plot of all numerical attributes of the given train dataset i.e. ApplicantIncome, CoApplicantIncome and LoanAmount. ")
print("Applicant Income distribution")
plt.figure(1)
plt.subplot(121)
sns.distplot(Train["ApplicantIncome"]);
plt.subplot(122)
Train["ApplicantIncome"].plot.box(figsize=(16,5))
plt.show()
Train.boxplot(column='ApplicantIncome',by="Education" )
plt.suptitle(" ")
plt.show()
print("Loan Amount distribution")
plt.figure(1)
plt.subplot(121)
df=Train.dropna()
sns.distplot(df['LoanAmount']);
plt.subplot(122)
Train['LoanAmount'].plot.box(figsize=(16,5))
plt.show()
print("Loan Amount  Distribution")
plt.figure(1)
plt.subplot(121)
df = Train.dropna()
sns.distplot(df["Loan_Amount_Term"]);
plt.subplot(122)
df["Loan_Amount_Term"].plot.box(figsize=(16,5))
plt.show()
print("Question 4")
print("Relation between Loan_Status and Gender")
print(pd.crosstab(Train["Gender"],Train["Loan_Status"]))
Gender = pd.crosstab(Train["Gender"],Train["Loan_Status"])
Gender.div(Gender.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Gender of applicant ")
plt.ylabel("Percentage")
plt.show()
print("Conclusion from Relation between Loan_Status and Gender")
print("Female whose Loan was approved = 75")
print("Male whose Loan was approved = 339 ")
print("Female whose Loan was not0 approved = 37")
print("Female whose Loan was approved = 150")
print("Ee can observe that the proportion of Male applicants is higher for the approved loans.")
print("Relation between Loan Status and martial status")
print(pd.crosstab(Train["Married"],Train["Loan_Status"]))
Married=pd.crosstab(Train["Married"],Train["Loan_Status"])
Married.div(Married.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Married")

plt.ylabel("Percentage")
plt.show()
print("Conclusion of relation between Loan_Status and Married status")
print("Married people whose Loan was approved = 285")
print("Married people whose Loan was not approved = 113")
print("Unmarried people whose Loan was approed = 134")
print("Unmarried people whose Loan was not approed = 79")
print("We can observe that the proportion of Married applicants is higher for the approved loans.")
print("Relation between LoanStatus and Dependent")
print(pd.crosstab(Train['Dependents'],Train["Loan_Status"]))
Dependents = pd.crosstab(Train['Dependents'],Train["Loan_Status"])
Dependents.div(Dependents.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Dependents")
plt.ylabel("Percentage")
plt.show()
print("Conclusion of relation between Loan_Status and Dependents")
print("Number of dependents on the loan applicant")
print("0 and Loan was approed : 238")
print("0 and Loan was not approed : 107")
print("1 and Loan was approed : 66")
print("1 and Loan was not approed : 36")
print("2 and Loan was approed : 76")
print("2 and Loan was not approed : 25")
print("3+ and Loan was approed : 33")
print("3+ and Loan was not approed : 18")
print("We can observe that the distribution of applicants with 1 or 3+ dependents is similar across both the categories of Loan_Status.")
print("Relation between Loan Status and Education")
print(pd.crosstab(Train["Education"],Train["Loan_Status"]))
Education = pd.crosstab(Train["Education"],Train["Loan_Status"])
Education.div(Education.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Education")
plt.ylabel("Percentage")
plt.show()
print("Conclusion of relation between Loan_Status and Education.")
print("People who are Graduate and Loan was approed : 340")
print("People who are Graduate and Loan was no approed : 140")
print("people who are Not Graduate and Loan was approed : 82")
print("People who are Not Graduate and Loan was not approed : 52")
print("We can observe that the proportion of Graduate applicants is higher for the approved loans.")
print("Relation between Loan Status and Self Employed")
print(pd.crosstab(Train["Self_Employed"],Train["Loan_Status"]))
SelfEmployed = pd.crosstab(Train["Self_Employed"],Train["Loan_Status"])
SelfEmployed.div(SelfEmployed.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Self Employed")
plt.ylabel("Percentage")
plt.show()
print("Conclusion from Relation between Loan_Status and Self_Employed")
print("People who are Self_Employed and Loan was approed : 56")
print("People who are Self_Employed and Loan was not approed : 26")
print("People who are not Self_Employed and Loan was approed : 343")
print("People who are not Self_Employed and Loan was not approed : 157")
print("There is nothing thatnwe can signify and  infer from Self_Employed vs Loan_Status plot.")
print("Relation between Loan_Status and Credit_History")
print(pd.crosstab(Train["Credit_History"],Train["Loan_Status"]))
CreditHistory = pd.crosstab(Train["Credit_History"],Train["Loan_Status"])
CreditHistory.div(CreditHistory.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Credit History")
plt.ylabel("Percentage")
plt.show()
print("Conclusion from relation between Loan Status and Credit History")
print("People with credit history as 1 and loan was approved : 378")
print("People with credit history as 1 and loan was not approved : 97")
print("People with credit history as 0 and loan was approved : 7")
print("People with credit history as 0 and loan was not approved : 82")
print("We can observe that, it seems people with credit history as 1 are more likely to get their loans approved.")
print("Relation between Loan Status and Property Area")
print(pd.crosstab(Train["Property_Area"],Train["Loan_Status"]))
PropertyArea = pd.crosstab(Train["Property_Area"],Train["Loan_Status"])
PropertyArea.div(PropertyArea.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.show()
print("conclusion from Relation between Loan Status and Property Area")
print("People who are from Rural area and loan was approved : 110")
print("People who are from Rural area and loan was not approved : 69")
print("People who are from Semiurban area and loan was approved : 179")
print("People who are from Semiurban area and loan was not approved : 54")
print("People who are from Urban area and loan was approved : 133")
print("People who are from Semiurban area and loan was not approved : 69")
print("We can observe that theProportion of loans getting approved in semiurban area is higher as compared to that in rural or urban areas")
print("Relation between Loan_Status and Income")
Train.groupby("Loan_Status")['ApplicantIncome'].mean().plot.bar(title= " Relation between Applicant Income and Loan Status")
plt.ylabel(" Applicant Income")
bins=[0,2500,4000,6000,81000]
groups=['Low','Mid','High', 'Very high']
Train['Income_bin']=pd.cut(df['ApplicantIncome'],bins,labels=groups)
print(pd.crosstab(Train["Income_bin"],Train["Loan_Status"]))
Income_bin = pd.crosstab(Train["Income_bin"],Train["Loan_Status"])
Income_bin.div(Income_bin.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))
plt.xlabel("Applicant Income")
plt.ylabel("Percentage")
plt.show()
print("We can observe that applicant income does not affect the chances of loan approval ")
bins=[0,1000,3000,42000]
groups =['Low','Mid','High']
Train['CoapplicantIncome_bin']=pd.cut(df["CoapplicantIncome"],bins,labels=groups)
print(pd.crosstab(Train["CoapplicantIncome_bin"],Train["Loan_Status"]))
CoapplicantIncome_Bin = pd.crosstab(Train["CoapplicantIncome_bin"],Train["Loan_Status"])
CoapplicantIncome_Bin.div(CoapplicantIncome_Bin.sum(1).astype(float),axis=0).plot(kind='bar',stacked=True,figsize=(4,4))
plt.xlabel("Co-applicant Income")
plt.ylabel("Percentage")
plt.show()
print("We can observe that if coapplicant’s income is less the chances of loan approval are high. This might be because of if there is no coapplicant then his income is marked as ZERO. So I think so we cannot infer any conclusion from here.")
Train["TotalIncome"]=Train["ApplicantIncome"]+Train["CoapplicantIncome"]
bins =[0,2500,4000,6000,81000]
groups=['Low','Average','High','Very High']
Train["TotalIncome_bin"]=pd.cut(Train["TotalIncome"],bins,labels=groups)
print(pd.crosstab(Train["TotalIncome_bin"],Train["Loan_Status"]))
TotalIncome = pd.crosstab(Train["TotalIncome_bin"],Train["Loan_Status"])
TotalIncome.div(TotalIncome.sum(1).astype(float),axis=0).plot(kind='bar',stacked=True,figsize=(2,2))
plt.xlabel("Total Income")
plt.ylabel("Percentage")
plt.show()
print("We can observe that low income people have less change of getting loan approved compared to Average, High and Very High Income ")
print("Applicants whose TotalIncome was Low and loan was approved : 10")
print("Applicants whose TotalIncome was Low and loan was not approved : 14")
print("Applicants whose TotalIncome was Aerage and loan was apprvoed : 87")
print("Applicants whose TotalIncome was Average and loan was not approved : 32")
print("Applicants whose TotalIncome was High and loan was approved : 159")
print("Applicants whose TotalIncome was High and loan was not approved : 65")
print("Applicants whose TotalIncome was Very High and loan was approved : 166")
print("Applicants whose TotalIncome was Very High and loan was not approed : 81")
print("Relation between Loan Status and Loan Amount")
bins = [0,100,200,700]
groups=['Low','Average','High']
Train["LoanAmount_bin"]=pd.cut(df["LoanAmount"],bins,labels=groups)
print(pd.crosstab(Train["LoanAmount_bin"],Train["Loan_Status"]))
LoanAmount=pd.crosstab(Train["LoanAmount_bin"],Train["Loan_Status"])
LoanAmount.div(LoanAmount.sum(1).astype(float),axis=0).plot(kind='bar',stacked=True,figsize=(4,4))
plt.xlabel("Loan Amount")
plt.ylabel("Percentage")
plt.show()
print("Conclusions from Relation between Loan Status and Loan Amount")
print("Applicants whose Loan Amount was low and Loan was approved : 86")
print("Applicants whose Loan Amount was low and Loan was not approved : 38")
print("Applicants whose Loan Amount was Average and Loan was approved : 207")
print("Applicants whose Loan Amount was Average and Loan was not approved : 83")
print("Applicants whose Loan Amount was High and Loan was approved : 39")
print("Applicants whose Loan Amount was High and Loan was not approved : 27")
print("We can observe that the proportion of approved loans is higher for Low and Average Loan Amount as compared to that of High Loan Amount")
Train=Train.drop(["Income_bin","CoapplicantIncome_bin","LoanAmount_bin","TotalIncome","TotalIncome_bin"],axis=1)
Train['Dependents'].replace('3+',3,inplace=True)
Test['Dependents'].replace('3+',3,inplace=True)
Train['Loan_Status'].replace('N', 0,inplace=True)
Train['Loan_Status'].replace('Y', 1,inplace=True)
matrix = Train.corr()
f, ax = plt.subplots(figsize=(10, 12))
sns.heatmap(matrix, vmax=.8, square=True, cmap="BuPu",annot=True);
print("From the above HEAT MAP the variables with darker color means their correlation is more.")
print("More correlated variables:")
print("ApplicantIncome - LoanAmount")
print("Credit_History - Loan_Status")