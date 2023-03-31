


def calculate_bill(name,clean,cavity,Xray):

            cleaning_rate=60
            Cavity_filling_rate=200
            XRay_rate= 100
            Tax_rate= 0.15
            total=0
            tax=0
            subtotal=0
            if clean=="y":
                total+=cleaning_rate
            if cavity=="y":
                total+=Cavity_filling_rate
            if Xray=="y":
                total+=XRay_rate
            
            
            if total> 200 and total <= 300:
               total *= 0.95  # 5% discount
            elif total > 300:
                total *= 0.90  # 10% discount
            
            
            tax=total*Tax_rate
            subtotal=total
            total=total+tax
            

            print("Melanie Dental Clinic")
            print("* ----------------------------*" )
            print("Receipt for patient name: ???",name)
            print("----------------------------------------------")
            print(" Subtotal:$",subtotal)
            print("Tax:$",tax)
            print("------------------------------------------------")
            print("Total:$",round(total,2))


name = input("Enter patient's name: ")
clean = input("Was cleaning performed? (y/n): ")
cavity = input("Was cavity-filling performed? (y/n): ")
Xray = input("Was X-Ray performed? (y/n): ")

calculate_bill(name,clean,cavity,Xray)