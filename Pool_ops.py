# pool_ops.py
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
# Text explaining script usage
# Parameters: c_in h_in w_in h_pool w_pool s p
# Output:
# A description of the script output
#
# Written by Devon Throckmorton

# import Python modules
import math # math module
import sys # argv
# initialize script arguments
c_in = float('nan')    
h_in = float('nan')        
w_in = float('nan')
h_pool = float('nan')
w_pool = float('nan')    
s = float('nan')        
p = float('nan')
if len(sys.argv) == 8:
    c_in = sys.argv[1]    
    h_in = sys.argv[2]        
    w_in = sys.argv[3]
    h_pool = sys.argv[4]
    w_pool = sys.argv[5]    
    s = sys.argv[6]        
    p = sys.argv[7]
else:
    print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
    exit()
c_out = 0
h_out = ((h_in+2*p-h_pool)/s + 1)
w_out = ((w_in+2*p-w_pool)/s + 1)
adds = h_out*w_out*c_in*(h_pool*w_pool-1)
muls = 0
divs = c_in*h_out*w_out
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed