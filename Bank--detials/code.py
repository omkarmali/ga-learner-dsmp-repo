# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)


categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts hered
banks=bank.drop('Loan_ID',axis=1)

print(banks.isnull().sum())

bank_mode=banks.mode()
print(bank_mode)

banks=pd.DataFrame(banks.fillna('bank_mode'))
print(banks)


#code ends here


# --------------
# Code starts here




avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc=np.mean)
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

con1=banks.Self_Employed=='Yes'
con2=banks.Loan_Status=='Y'

#loan_approved_se=banks.count(banks[con1 & con2])
loan_approved_se=len(banks[con1 & con2])
print(loan_approved_se)
#loan_approved_se=loan_approved_se.value_counts()

con3=banks.Self_Employed=='No'
con4=banks.Loan_Status=='Y'

#loan_approved_nse=banks.count(banks[con3 & con4])
loan_approved_nse=len(banks[con3 & con4])
print(loan_approved_nse)
#loan_approved_nse=loan_approved_nse.value_counts()

percentage_se=(loan_approved_se/614)*100
print(percentage_se)

percentage_nse=(loan_approved_nse/614)*100
print(percentage_nse)

# code ends here


# --------------
# code starts here

loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)
con=loan_term>=25
big_loan_term=(len(banks[con]))
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby=banks.groupby('Loan_Status')[['ApplicantIncome','Credit_History']]

mean_values=loan_groupby.mean()
print(mean_values)


# code ends here


