def calculateIncome(salary, salaryType, festival=0, allowance=0, others=0):
    festival = 0 if festival is None else festival
    allowance = 0 if allowance is None else allowance
    others = 0 if others is None else others
    if salaryType.lower() == "monthly":
        return (salary + allowance + others) * 12 + festival
    else:
        return salary + festival + allowance + others


def calculateDeduction(income, pf=0, cit=0, ssf=0, li=0, mi=0):
    pf = 0 if pf is None else pf
    cit = 0 if cit is None else cit
    ssf = 0 if ssf is None else ssf
    li = 0 if li is None else li
    mi = 0 if mi is None else mi
    if pf != 0 and ssf != 0:
        raise ValueError("You can't contribute to both Provident Fund and Social Security Fund.")
    if pf > (income * 20 / 100):
        raise ValueError("Provident Fund must not be greater than 20% of total income.")
    if cit > 300000:
        raise ValueError("Contribution must not be greater than 300000 per year.")
    li = 40000 if li > 40000 else li
    mi = 20000 if mi > 20000 else mi
    return pf + cit + ssf + li + mi


def calculateTax(status, income, deduction):
    taxSlab = [[500000, 200000, 300000, 1000000, float('inf')], [600000, 200000, 300000, 900000, float('inf')]]
    taxRate = [.01, .10, .20, .30, .36]
    taxAmount = 0
    slabTax = 0
    taxableAmount = income - deduction
    print("\nNet Taxable Amount: ", taxableAmount)
    married = 1 if status.lower() == "married" else 0
    index = 0
    print(f'slab,   slabAmount, \ttaxRatee, \tslabTax')
    while taxableAmount > 0:
        taxSlabb = taxSlab[married][index]
        taxRatee = taxRate[index]
        slabAmount = taxSlabb if taxableAmount >= taxSlabb else taxableAmount

        slabTax = slabAmount * taxRatee
        taxAmount = taxAmount + slabTax

        print(f'slab {index+1}, {slabAmount},\t \t{taxRatee}, \t\t {slabTax}')
        taxableAmount = taxableAmount - slabAmount
        index += 1
    return taxAmount

def main(tax_info):
    salary = tax_info.get('basic_salary')
    status = tax_info.get('marital_status')
    salaryType = tax_info.get('salary_type')
    festival = tax_info.get('additional', {}).get('festival', 0)
    allowance = tax_info.get('additional', {}).get('allowance', 0)
    others = tax_info.get('additional', {}).get('others', 0)

    income = calculateIncome(salary, salaryType, festival, allowance, others)
    print("\nIncome:", income)

    pf = tax_info.get('deduction', {}).get('pf', 0)
    cit = tax_info.get('deduction', {}).get('cit', 0)
    ssf = tax_info.get('deduction', {}).get('ssf', 0)
    li = tax_info.get('deduction', {}).get('li', 0)
    mi = tax_info.get('deduction', {}).get('mi', 0)
    deduction = calculateDeduction(income, pf, cit, ssf, li, mi)
    print("\nDeduction: ", deduction)

    tax = calculateTax(status, income, deduction)
    print("\nNet Tax Liability (yearly):", tax)


tax_info = {
    'basic_salary': 50000,
    'marital_status': 'married',
    'salary_type': 'monthly',
    'additional': {
        'festival': 100000,
        'allowance': 50000,
        'others': 50000,
    },

    'deduction': {
        'pf': 10000,
        'cit': 10000,
        'ssf': None,
        'li': 10000,
        'mi': 10000 
    }
}

main(tax_info)
