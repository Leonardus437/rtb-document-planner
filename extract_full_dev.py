from docx import Document

doc = Document('DOC TO REFER TO/#1_session_plan1.docx')
table = doc.tables[0]

print("="*80)
print("COMPLETE DEVELOPMENT SECTION - TRAINER GUIDED TECHNIQUE")
print("="*80)

# Get the full text from the development cell
dev_cell = table.rows[12].cells[0]
full_text = dev_cell.text

print(full_text)
print("\n" + "="*80)
