from collections import OrderedDict
# validate barcode has correct  number of digit in each section
def barcode_validator(barcode):
    barcode = barcode.replace('-', ' ')
    sections = {
        'group-Identifier': 4,
        'publisher-Identifier': 6,
        'Title-Identifier': 5,
        'checkDigit': 1
    }
    segment = 0
    segments = barcode.split()
    sections=OrderedDict()
    for section_name, maxlen in sections.items():
        if len(segments[segment]) > maxlen:
               raise ValueError(f'length of section {section_name} is more than {maxlen}')
    return True

def clean_barcode(barcode):
    barcode = barcode.replace('-', '')
    barcode = barcode.replace(' ', '')
    if len(barcode)>10:
       raise ValueError('barcode has more than 10 digit, this function handles 10 digit barcode') 
    return(barcode)

def calculate_isbn10_barcode_check_digit():
    barcode=input("scan your barcode to get the checkDigit: ")
    if barcode_validator(barcode):
        barcode=clean_barcode(barcode)
        print(barcode)
        temp_barcode = barcode[:-1]
        print(temp_barcode)
        list_barcode=[int(x) for x in str(temp_barcode)]
        total=0
#calculate the check digit and print that out
    sorted(list_barcode , reverse= True)
    print(len(list_barcode))
    for item in range(0,len(list_barcode)): 
        total+=(list_barcode[item]*(10-item))
    checkDigit=11-(total%11)
    print(checkDigit)

def validate_isbn10_barcode_check_digit(): 
    barcode=input("scan your barcode to validate the checkDigit: ")
    if barcode_validator(barcode):
        barcode=clean_barcode(barcode)   
    if barcode[-1]=='X':
        barcode=barcode.replace(barcode[-1],'10')
    barcode=[int(x) for x in str(barcode)]       
    total=0
    for y in range(0,len(barcode)):
        total+=(barcode[y]*(10-y))
    if total%11 == 0:
        print ('This is a valid isbn10 barcode.')
    else:
        print('barcode is not a valid isbn10 barcode')    
    
calculate_isbn10_barcode_check_digit()
validate_isbn10_barcode_check_digit()





		
        
	
    


        
    
	
	
            
               
                
    