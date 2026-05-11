from docx import Document
import os

print("="*80)
print("DEEP ANALYSIS OF RTB FACILITATION TECHNIQUES")
print("="*80)

docs = [
    'DOC TO REFER TO/#1_session_plan1.docx',
    'DOC TO REFER TO/#2_sessionplan_iteration2.docx', 
    'DOC TO REFER TO/#3_session_plan3.docx'
]

for doc_path in docs:
    if os.path.exists(doc_path):
        print(f"\n{'='*80}")
        print(f"DOCUMENT: {doc_path}")
        print(f"{'='*80}")
        
        doc = Document(doc_path)
        table = doc.tables[0]
        
        # Facilitation Technique
        print("\n--- FACILITATION TECHNIQUE ---")
        print(table.rows[8].cells[0].text)
        
        # Introduction Section
        print("\n--- INTRODUCTION SECTION ---")
        print("Headers:", [cell.text.strip() for cell in table.rows[9].cells])
        print("\nContent:")
        print(table.rows[10].cells[0].text)
        
        # Development/Body Section (rows 11-14)
        print("\n--- DEVELOPMENT/BODY SECTION ---")
        for i in range(11, 15):
            print(f"\n*** Row {i} ***")
            for j, cell in enumerate(table.rows[i].cells):
                if cell.text.strip():
                    print(f"Column {j}: {cell.text[:500]}")
        
        # Conclusion
        print("\n--- CONCLUSION SECTION ---")
        print(table.rows[15].cells[0].text)
        
        # Assessment
        print("\n--- ASSESSMENT SECTION ---")
        for i in range(16, 19):
            print(f"Row {i}:", table.rows[i].cells[0].text[:200])

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
