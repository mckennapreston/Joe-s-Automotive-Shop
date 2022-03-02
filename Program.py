
import CarClass as c
import CustomerClass as cc
import ServiceQuoteClass as sqc 

Jaguar = c.Car("Jaguar","XF","2012")
print("1st Car Type:",Jaguar.get_make(), Jaguar.get_model(), Jaguar.get_year())


Jaguar.set_make("Ford")
Jaguar.set_model("F150")
Jaguar.set_year("2007")

print("2nd Car Type:",Jaguar.get_make(), Jaguar.get_model(), Jaguar.get_year())


Mckenna = cc.Customer("Mckenna","1001 Speight Ave","713-351-9799")
print("1st Customer Information:", Mckenna.get_name(), Mckenna.get_address(), Mckenna.get_phone())

Mckenna.set_name("Kevin")
Mckenna.set_address("5201 S University Parks Dr.")
Mckenna.set_phone("832-289-9921")

print("2nd Customer Information:", Mckenna.get_name(), Mckenna.get_address(), Mckenna.get_phone())

OilChange = sqc.ServiceQuote(35,20)
print("1st Customer Price:", OilChange.get_labor_charges(), OilChange.get_parts_charges(),'$', format(OilChange.get_sales_tax(),',.2f'),'$', format(OilChange.get_total_charges(),',.2f'))

OilChange.set_parts_charges(45)
OilChange.set_labor_charges(30)
print("2nd Customer Price:", OilChange.get_labor_charges(), OilChange.get_parts_charges(),'$', format(OilChange.get_sales_tax(),',.2f'),'$', format(OilChange.get_total_charges(),',.2f'))