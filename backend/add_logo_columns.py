import sqlite3

# Connect to database
conn = sqlite3.connect('rtb_planner.db')
cursor = conn.cursor()

print("Adding logo columns to session_plans table...")

try:
    # Add rtb_logo_path column
    cursor.execute("ALTER TABLE session_plans ADD COLUMN rtb_logo_path VARCHAR(500)")
    print("✓ Added rtb_logo_path column")
except sqlite3.OperationalError as e:
    print(f"rtb_logo_path: {e}")

try:
    # Add school_logo_path column
    cursor.execute("ALTER TABLE session_plans ADD COLUMN school_logo_path VARCHAR(500)")
    print("✓ Added school_logo_path column")
except sqlite3.OperationalError as e:
    print(f"school_logo_path: {e}")

conn.commit()
conn.close()

print("\nDatabase updated successfully!")
print("You can now restart the backend.")
