from docx import Document
from docx.oxml.ns import qn

doc = Document('DOC TO REFER TO/#1_session_plan1.docx')
table = doc.tables[0]

print("="*80)
print("CHECKING CELL COLORS IN OFFICIAL RTB DOCUMENT")
print("="*80)

for i in range(10):
    print(f"\n--- Row {i} ---")
    cell = table.rows[i].cells[0]
    
    # Check for shading
    tcPr = cell._element.tcPr
    if tcPr is not None:
        shading = tcPr.find(qn('w:shd'))
        if shading is not None:
            fill = shading.get(qn('w:fill'))
            print(f"Cell has shading/color: {fill}")
        else:
            print("No shading found")
    else:
        print("No cell properties")
