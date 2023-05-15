marital_status=input("enter the marital status:")
income=120000
if marital_status == "single":
    if income <= 500000:
        tax_rate = 0.01
        print("Net Payable tax:",income*tax_rate)
    elif 500000<income <= 700000:
        tax_rate = 0.10
        print("First slab",500000*0.01)
        print("Second slab",(income-500000)*tax_rate)
    elif 700000<income <=1000000:
        tax_rate=0.20
        print("First slab",500000*0.01)
        print("Second slab",(income-500000)*0.10)
        print("Third slab",(income-1000000)*tax_rate)

    elif income <=2000000:
        tax_rate=0.30
    else:
        tax_rate = 0.36
else:  
    if income <= 600000:
        tax_rate = 0.01
    elif income <= 800000:
        tax_rate = 0.10
    elif income <=1100000:
        tax_rate=0.20
    elif income <=2000000:
        tax_rate=0.30
    else:
        tax_rate = 0.36

