basic_sales_tax = 0.1
imported_sales_tax = 0.05
sumit=0
def main():
	imported_item1 = float(input("Enter price of imported perfume : "))
	non_imp_item = float(input("Enter price of perfume : "))
	medical_item = float(input("Enter price of headache pills : "))
	imported_item2 = float(input("Enter price of imported chocolate box : "))
	impt = calculate_imported_totals(imported_item1)
	nonimpt = calculate_nonImp_totals(non_imp_item)
	met = calculate_medical_totals(medical_item)
	impft = calculate_impfood_totals(imported_item2)
	display_total_amount(impt,nonimpt,met,impft)
	
	
def calculate_imported_totals(imported_item1):
	basic_sales_tax = imported_item1 * 0.05
	imported_sales_tax = imported_item1 * 0.05
	total_sales_tax = basic_sales_tax + imported_sales_tax
	total_price_imp_item = imported_item1 + basic_sales_tax + imported_sales_tax
	print("imported perfume price including tax : ",total_price_imp_item)
	return total_price_imp_item

def calculate_nonImp_totals(non_imp_item):
	basic_sales_tax = non_imp_item * 0.1
	total_price = non_imp_item + basic_sales_tax
	print("1 bottle of perfume price including tax : ",total_price)
	return total_price

def calculate_medical_totals(medical_item):
	print("price of headache pills : ",medical_item)
	return medical_item

def calculate_impfood_totals(imported_item2):
	imported_sales_tax = imported_item2 * 0.05
	total_impfood_price = imported_item2 + imported_sales_tax
	print("price of imported chocolate box including tax : ",total_impfood_price)
	return total_impfood_price

def display_total_amount(impt, nonimpt,met,impft):
	sum = impt + nonimpt + met + impft
	print(sum)
	
main()