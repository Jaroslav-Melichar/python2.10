Office = {
    'Employee0': {'jmeno': 'Jarda','Přijmeni':'Melichar','pozice': 'IT Specialista','Email':'jarda@neco.cz','Kancelar':'4.C'},
    'Employee1': {'jmeno': 'Pepa','Přijmeni':'Novak','pozice': 'IT neco','Email':'pepek@seznam.cz','Kancelar':'3.C'},
    'Employee2': {'jmeno': 'Jana','Přijmeni':'Kralova','pozice': 'IT neco','Email':'jana@neco.cz','Kancelar':'3.C'},
    'Employee3': {'jmeno': 'Jitka','Přijmeni':'Kralova','pozice': 'IT neco','Email':'Jitka@blabla.cz','Kancelar':'2.C'},
    'Employee4': {'jmeno': 'Filip','Přijmeni':'Dubina','pozice': 'IT neco','Email':'dubina@seznam.cz','Kancelar':'1.C'},
}

## 2) Vypište všechny zaměstnance pod sebe, viz obrázek 1. 

for Employee, info in Office.items():
        print("jmeno : ",info['jmeno'])
        print("Přijmeni : ",info['Přijmeni'])
        print("pozice : ",info['pozice'])
        print("Email : ",info['Email'])
        print("Kancelar : ",info['Kancelar'])
        print("")

## 3a)Vypište pod sebe pouze jméno a příjmení a email všech zaměstnanců.

for Employee, info in Office.items():
        print("jmeno : ",info['jmeno'])
        print("Přijmeni : ",info['Přijmeni'])
        print("Email : ",info['Email'])
        print("")

##  Vyberte si jednoho konkrétního zaměstnance a vypište pouze jeho jméno a příjmení a pozici. 

for Employee, info in Office.items():
    if info['jmeno'] == 'Jarda':
        print("jmeno : ",info['jmeno'])
        print("Přijmeni : ",info['Přijmeni'])
        print("pozice : ",info['pozice'])
        print("")

## 4)Vypište pouze zaměstnance, kteří sídlí ve stejné kanceláři.

for Employee, info in Office.items():
    if info['Kancelar'] == '3.C':
        print("jmeno : ",info['jmeno'])
        print("Přijmeni : ",info['Přijmeni'])
        print("pozice : ",info['pozice'])
        print("Email : ",info['Email'])
        print("Kancelar : ",info['Kancelar'])
        print("")
