
# coding: utf-8

# In[27]:


# Question 1: Write a function so that the columns of the output matrix are powers of the input vector. 

# The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, 
# the i-th output column is the input vector raised element-wise to the power of N - i - 1.

#HINT: Such a matrix with a geometric progression in each row is named for AlexandreTheophile Vandermonde.


import numpy as np

def mat_Vander(input_vector,n,bool_arg):
    output_matrix=np.vander(x=input_vector,N=n,increasing=bool_arg)
    return output_matrix


input_vector=np.arange(5,13,2)
n=5
bool_arg_T = True
bool_arg_F = False


out_matrix_True=mat_Vander(input_vector,n,bool_arg_T)
out_matrix_False=mat_Vander(input_vector,n,bool_arg_F)

print("Input_Vector \n", input_vector, "\n")
print("Output Matrix when boolen argument is True \n", out_matrix_True, "\n")
print("Output Matrix when boolen argument is False \n", out_matrix_False,)

