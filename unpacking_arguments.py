def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

keis_data = [21, 0, 0]

health_calculator(keis_data[0], keis_data[1], keis_data[2])
health_calculator(*keis_data)   #unpacking an argument list