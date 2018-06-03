Sign = ['+', '-']
# Para_uplims_lolims is a (2^ParaLen) x ParaLen matrix
i = 0
for Iter in product(range(2), repeat=ParaLen):
	for j in range(ParaLen):
        Para_uplims_lolims[i, j] = eval('{}{}{}'.format(
        	Para_uplims_lolims[i,j],Sign[Iter[j]],Uncertainty[j]))
    i += 1