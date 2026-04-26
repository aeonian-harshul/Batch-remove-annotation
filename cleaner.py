import os
import pdfrw

print("--- PDF Annotation Batch Remover ---")
folder_path = input("Drag and drop your PDF folder here, then press Enter: ").strip()

# Clean up the path if dragging and dropping added extra quotes
folder_path = folder_path.strip('"').strip("'")

if not os.path.exists(folder_path):
    print("Hmm, I can't find that folder. Please check it and try again.")
else:
    # Look at every file in the folder you provided
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf') and not filename.startswith('cleaned_'):
            in_path = os.path.join(folder_path, filename)
            # Create a new name for the output file
            out_path = os.path.join(folder_path, "cleaned_" + filename)
            
            print(f"Cleaning {filename}...")
            
            try:
                reader = pdfrw.PdfReader(in_path)
                
                # Go through each page
                for page in reader.pages:
                    if page.Annots:
                        # Keep links, remove everything else (like highlights/comments)
                        page.Annots = [a for a in page.Annots if a.Subtype == "/Link"]
                
                # Save the new PDF
                pdfrw.PdfWriter(out_path, trailer=reader).write()
                
            except Exception as e:
                print(f"Skipped {filename} (Error: {e})")

print("------------------------------")
print("All done! Check your folder for the 'cleaned_' files.")
input("Press Enter to close this window...")