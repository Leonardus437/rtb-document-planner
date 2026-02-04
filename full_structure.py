from docx import Document

doc = Document('DOC TO REFER TO/#1_session_plan1.docx')
table = doc.tables[0]

print("="*80)
print("COMPLETE RTB SESSION PLAN STRUCTURE")
print("="*80)

print("\n### INTRODUCTION (Row 10) ###")
print(table.rows[10].cells[0].text)

print("\n### DEVELOPMENT/BODY (Rows 12-14) ###")
print(table.rows[12].cells[0].text)

print("\n### CONCLUSION (Row 15) ###")
intro_cell = table.rows[15].cells[1]
print(intro_cell.text)

print("\n### ASSESSMENT SECTIONS (Rows 16-18) ###")
print("\n--- Summary (Row 16) ---")
print(table.rows[16].cells[0].text)

print("\n--- Assessment/Assignment (Row 17) ---")
print(table.rows[17].cells[0].text)

print("\n--- Evaluation (Row 18) ---")
print(table.rows[18].cells[0].text)

print("\n" + "="*80)
