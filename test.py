#patients [weight, height]
patients = [[70, 1.8], [80, 1.9], [150, 1.7], [65, 1.76]] 

def calculate_bmi(weight, height):
    return weight / (height ** 2)
for patient in patients:
    weight = patient[0]
    height = patient[1]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)