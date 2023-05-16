def calculate_tax(income, marital_status):
    if marital_status == "unmarried":
        tax_slabs = [
            (500000, 0.01),
            (700000, 0.1),
            (1000000, 0.2),
            (2000000, 0.3),
            (float('inf'), 0.36)
        ]
    elif marital_status == "married":
        tax_slabs = [
            (600000, 0.01),
            (800000, 0.1),
            (1100000, 0.2),
            (2000000, 0.3),
            (float('inf'), 0.36)
            (2000000, 0.3),
        ]

    tax_amount = 0
    remaining_income = income

    for slab in tax_slabs:
        taxable_amount, tax_rate = slab
        if remaining_income <= 0:
            break
        if remaining_income <= taxable_amount:
            tax_amount += remaining_income * tax_rate
            break
        else:
            tax_amount += taxable_amount * tax_rate
            remaining_income -= taxable_amount

    return tax_amount

def calculate_payroll(salary, yearly_bonus, allowance, other_income, marital_status):
    yearly_salary = salary * 12
    yearly_income = yearly_salary + yearly_bonus + (allowance * 12) + (other_income * 12)
    yearly_taxable_income = yearly_income

    pf_contribution = salary * 0.1
    cict_contribution = 0 
    ssf_contribution = salary * 0.05
    life_insurance = 0  

    yearly_deductions = pf_contribution * 12 + cict_contribution * 12 + ssf_contribution * 12 + life_insurance * 12
    yearly_taxable_income -= yearly_deductions

    tax = calculate_tax(yearly_taxable_income, marital_status)
    net_payable_tax = tax
    annual_gross_salary = yearly_income
    taxable_income = yearly_taxable_income

    return annual_gross_salary, taxable_income, net_payable_tax

salary = 100000
yearly_bonus = 0
allowance = 0
other_income = 0
marital_status = "unmarried"

annual_gross_salary, taxable_income, net_payable_tax = calculate_payroll(
    salary, yearly_bonus, allowance, other_income, marital_status
)

print("Tax Calculation")
print(f"Annual Gross Salary: {annual_gross_salary}")
print(f"Taxable Income: {taxable_income}")
print(f"Net Payable Tax: {net_payable_tax}")