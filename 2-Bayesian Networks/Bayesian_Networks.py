# packages
import seaborn as sns
import pandas as pd
import numpy as np

# get data
peng = sns.load_dataset('penguins', cache=True, data_home=None)
print(peng.shape)

# clean data to make continous variables categorical
cont_cols = list( peng.select_dtypes('float64').columns )

# number of levels
levels = 2

for col in cont_cols:
    peng[col] = pd.cut(  peng[col], levels )
    

# joint probs for only two variables
def joint_probs(DF, index, cols ):
    all_cols = index + cols
    N = DF.shape[0]
    
    joint_counts = pd.pivot_table( DF[all_cols] , index = index , columns= cols , aggfunc= 'size' ).replace(np.nan,0)
    
    joint_prob = np.round( joint_counts / N, 3)
    
    return joint_prob

    
JPD = joint_probs(peng, ['species'], ['island','sex'] )
print(JPD,'\n')
    
JP2 = joint_probs(peng, ['island'], ['species'])
print(JP2,'\n')
    
    

# conditional probs

def cond_prob_dist(joint_probs):
    # P(A | B) = P( A and B ) / P(B)
    ## https://en.wikipedia.org/wiki/Conditional_probability
    
    """
    calculates the conditions prob. distribution where:
    joint_probs: is a joint prob distribution as pandas dataframe
    A = {index   of joint_probs} = {a1, a2, .. an }
    B = {columns of joint_probs} = {b1, b2, .. bn }
    
    
    returns:
    CPD = the conditional probability dist P(A|B) as a pandas dataframe
    """
    
    CPD = joint_probs.copy()

    # column sum
    col_totals = joint_probs.sum(axis=0)
    
    for col in col_totals.index:
        CPD[col] =   CPD[col] / col_totals.loc[col]
        
    # rename columns
    CPD.columns = [ f'b{i+1} = {x}' for i,x in enumerate(CPD.columns) ]
    CPD.index   = [ f'a{i+1} = {x}' for i,x in enumerate(CPD.index) ]
        
    return CPD.round(3)
    
# conditional probs are not symmetric
print( cond_prob_dist(JPD) , '\n'*2)


print( cond_prob_dist(JP.T).T  )



# sex
JP = joint_probs(peng, ['species','sex'], ['island'] )
print( cond_prob_dist(JP) , '\n'*2)



## possible combinations
print( peng.nunique().to_string() )



