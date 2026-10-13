import numpy as np
import matplotlib.pyplot as h
series_params = {
    'Uranium':  {'A': -30.6, 'B': 38.2},
    'Thorium':  {'A': -32.1, 'B': 39.0},
    'Actinium': {'A': -31.4, 'B': 38.5}
}


decay_constants = {
    'Uranium':  [1.54e-18, 5.0e-17, 1.3e-16, 5.8e-16, 1.4e-10],
    'Thorium':  [1.3e-20,  6.2e-19, 5.1e-18, 2.7e-17, 1.3e-13],
    'Actinium': [9.6e-19,  4.1e-17, 2.8e-16, 2.2e-15, 3.5e-11]
}
def Calculate_Range(lamba_val,A,B):
    log_lambda=np.log10(lamba_val)
    log_R=(log_lambda-A)/B
    return 10**log_R
h.figure(figsize=(9, 6))
colors = {'Uranium': 'crimson', 'Thorium': 'royalblue', 'Actinium': 'forestgreen'}

for name, params in series_params.items():
    A = params['A']
    B = params['B']
    
    R_list = []
    lambda_list = []
    
    for lam in decay_constants[name]:
        
        r_val = Calculate_Range(lam, A, B)
        
        
        R_list.append(r_val)
        lambda_list.append(lam)
    
    
    log_R = np.log10(np.array(R_list))
    log_lambda = np.log10(np.array(lambda_list))
    
    
    h.scatter(log_R, log_lambda, color=colors[name], label=f'{name} Series')
    h.plot(log_R, log_lambda, color=colors[name], linestyle='--', alpha=0.7)


h.xlabel(r'$\log_{10}(R)$ [Calculated Range in cm]', fontsize=12)
h.ylabel(r'$\log_{10}(\lambda)$ [Decay Constant $s^{-1}$]', fontsize=12)
h.title('Geiger-Nuttall Law: Calculated Range vs Decay Constant', fontsize=14)
h.legend()
h.grid(True, which='both', linestyle='--', alpha=0.6)

h.show()