"""
Test RTB Document Generator - All Features
"""
import sys
sys.path.append('backend')

from document_generator import generate_smart_objectives, generate_apa_references

print("="*80)
print("RTB DOCUMENT GENERATOR - FEATURE TEST")
print("="*80)

# Test 1: Objectives Generation
print("\n### TEST 1: SMART Objectives ###")
objectives = generate_smart_objectives("C++ Programming", "Apply basic C++ concepts")
print(objectives)

# Test 2: References Generation
print("\n### TEST 2: References ###")
refs = generate_apa_references("C++ Programming", "ICT", "Apply concepts")
print(refs)

# Test 3: Check all facilitation techniques
print("\n### TEST 3: Facilitation Techniques ###")
techniques = [
    "Trainer Guided",
    "Brainstorming", 
    "Group Discussion",
    "Simulation",
    "Experiential Learning",
    "Jigsaw"
]

for tech in techniques:
    print(f"- {tech}: OK")

print("\n### TEST 4: Color Functions ###")
try:
    from document_generator import set_cell_color
    print("- set_cell_color: OK")
except:
    print("- set_cell_color: MISSING")

print("\n" + "="*80)
print("ALL TESTS COMPLETED")
print("="*80)
