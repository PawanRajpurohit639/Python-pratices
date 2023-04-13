from PyPDF2 import PdfReader
import re
import pandas as pd
# creating a pdf reader object
reader = PdfReader('Fastra_20230131.pdf')

print("pdf page length",len(reader.pages))
text = ''
for p in reader.pages:
    #print(p.extract_text())
    text+= p.extract_text()
    #with open("test.txt","a") as file:
    #    file.write(p.extract_text())

splitText = text.splitlines()

invoiceNumber : str = ""
jobNumber: str = ""
invoiceDate : str = ""
lineDataFound:bool = False
lineAmount:list = []
lineDate:list = []
subtotal:str = ""
vatTotal:str = ""
invoiceTotal:str = ""

for lines in splitText:
    if lines.startswith("Factuur"):
        invoiceNumber = re.search("[0-9]{5,}",lines).group()

    if "Dossiernummer" in lines:
        jobNumber = re.search("[A-Za-z]+[0-9]{5,}",lines).group()
    
    if lines.startswith("Vervaldatum"):
        invoiceDate = re.search("[0-9-]+",lines).group()

    if lines.startswith("Datum"):
        lineDataFound = True    

    if "Subtotaal" in lines:
        lineDataFound = False
    
    if lineDataFound:
        #print(lines)
        if re.search("[A-Za-z-]{4,}[0-9-]+",lines):
            lineAmount.append(re.search("[0-9.]+,[0-9]+",lines).group())
            lineDate.append(re.search("[0-9-]{1,}[A-Za-z]{3}",lines).group())

    if "Subtotaal" in lines:
        subtotal = re.search("^[0-9.]+,[0-9]{2}",lines).group()
       # print(re.search("^[0-9.]+,[0-9]{2}",lines).group())

    if "BTW" in lines and re.search("^[€0-9.]+,[0-9]{2}",lines):
        vatTotal = re.search("^[€0-9.]+,[0-9]{2}",lines).group().replace("€","").strip()
        invoiceTotal = re.search("[0-9.]+,[0-9]{2}\s€$",lines).group().replace("€","").strip()

invoiceDetailDT = pd.DataFrame({'InvoiceNumber':[invoiceNumber],'InvoiceDate':[invoiceDate],'InvoiceSubTotal':[subtotal],'Vat Total':[vatTotal],'Invoice Total':[invoiceTotal]})
invoiceLineDT = pd.DataFrame({'LineDate':lineDate,'LineAmount':lineAmount})


with pd.ExcelWriter("C:\\Users\\pawan\\OneDrive\\Documents\\Python pratices\\test.xlsx") as writer:
   
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    invoiceDetailDT.to_excel(writer, sheet_name="Invoice Detail", index=False)
    invoiceLineDT.to_excel(writer, sheet_name="InvoiceLine Detail", index=False)