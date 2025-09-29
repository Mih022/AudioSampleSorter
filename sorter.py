import os
import shutil
from sorter_config import SOURCE_FOLDER, TARGET_FOLDER, IGNORED_PATHS, MAX_DEPTH, SORTING_RULES

def copy_if_not_exists(source_path, dest_folder, filename):
    """
    Copies a file only if a file with the same name doesn't already
    exist in the destination. Returns the final path if copied,
    or None if skipped because it was a duplicate.
    """
    dest_path = os.path.join(dest_folder, filename)
    if os.path.exists(dest_path):
        return None
    else:
        shutil.copy2(source_path, dest_path)
        return dest_path


def sort_files():
    """
    Main function to orchestrate the file sorting process with priority logic.
    """
    print("🚀 Starting the sorting process...")

    if not os.path.isdir(SOURCE_FOLDER):
        print(f"❌ ERROR: Source folder not found at '{SOURCE_FOLDER}'")
        return

    stats = {
        'total': 0,
        'copied': 0,
        'conflicts': 0,
        'unsorted': 0,
        'duplicates': 0
    }

    conflict_path = os.path.join(TARGET_FOLDER, "Conflict")
    unsorted_path = os.path.join(TARGET_FOLDER, "Unsorted")
    os.makedirs(conflict_path, exist_ok=True)
    os.makedirs(unsorted_path, exist_ok=True)

    #Create a set of full, normalized paths to ignore
    full_ignored_paths = {os.path.normpath(os.path.join(SOURCE_FOLDER, p)) for p in IGNORED_PATHS}

    source_folder_depth = SOURCE_FOLDER.rstrip(os.sep).count(os.sep)

    for root, dirs, files in os.walk(SOURCE_FOLDER):
        #Pruning logic to skip ignored folders ---
        normalized_root = os.path.normpath(root)
        if normalized_root in full_ignored_paths:
            print(f"⏭️  Skipping ignored directory: {os.path.relpath(root, SOURCE_FOLDER)}")
            dirs[:] = [] # Don't traverse any deeper into this directory
            continue # Skip processing files in this directory

        if MAX_DEPTH is not None:
            current_depth = root.count(os.sep) - source_folder_depth
            if current_depth >= MAX_DEPTH:
                del dirs[:]

        for filename in files:
            stats['total'] += 1
            
            source_file_path = os.path.join(root, filename)
            lowercase_filename = filename.lower()
            
            matching_rules = []
            for rule in SORTING_RULES:
                if any(lowercase_filename.endswith(ext) for ext in rule['extensions']) and \
                   all(keyword.lower() in lowercase_filename for keyword in rule['keywords']):
                    matching_rules.append(rule)

            try:
                if not matching_rules:
                    # Unsorted
                    final_path = copy_if_not_exists(source_file_path, unsorted_path, filename)
                    if final_path:
                        print(f"❓ Unsorted: {filename} -> Copied to Unsorted")
                        stats['unsorted'] += 1
                    else:
                        print(f"🚫 Duplicate: {filename} already exists in Unsorted, skipped.")
                        stats['duplicates'] += 1
                else:
                    max_priority = max(rule['priority'] for rule in matching_rules)
                    top_priority_rules = [rule for rule in matching_rules if rule['priority'] == max_priority]
                    unique_top_destinations = set(rule['destination'] for rule in top_priority_rules)

                    if len(unique_top_destinations) == 1:
                        # Successfully sorted
                        destination = unique_top_destinations.pop()
                        destination_subfolder = os.path.join(TARGET_FOLDER, destination)
                        os.makedirs(destination_subfolder, exist_ok=True)
                        
                        final_path = copy_if_not_exists(source_file_path, destination_subfolder, filename)
                        if final_path:
                            print(f"✅ Copied: {filename} -> {os.path.relpath(final_path, TARGET_FOLDER)}")
                            stats['copied'] += 1
                        else:
                            print(f"🚫 Duplicate: {filename} already exists in destination, skipped.")
                            stats['duplicates'] += 1
                    else:
                        # Conflict
                        final_path = copy_if_not_exists(source_file_path, conflict_path, filename)
                        if final_path:
                            print(f"⚠️ Conflict: {filename} has a priority tie between {list(unique_top_destinations)} -> Copied to Conflict")
                            stats['conflicts'] += 1
                        else:
                            print(f"🚫 Duplicate: {filename} already exists in Conflict, skipped.")
                            stats['duplicates'] += 1

            except Exception as e:
                print(f"🚨 ERROR processing file {filename}: {e}")

    print("\n🎉 Sorting complete!")
    print(f"Your original files in '{SOURCE_FOLDER}' are untouched.")
    
    print("\n" + "="*20 + " 📊 Sorting Summary " + "="*20)
    if stats['total'] == 0:
        print("No files were found to process (or all were in ignored paths).")
    else:
        # Calculate percentages safely
        copied_pct = (stats['copied'] / stats['total']) * 100
        conflicts_pct = (stats['conflicts'] / stats['total']) * 100
        unsorted_pct = (stats['unsorted'] / stats['total']) * 100
        
        print(f"Total files processed: {stats['total']}\n")
        print(f"✅ Sorted:      {stats['copied']:>5} files ({copied_pct:.1f}%)")
        print(f"❓ Unsorted:    {stats['unsorted']:>5} files ({unsorted_pct:.1f}%)")
        print(f"⚠️ Conflicts:   {stats['conflicts']:>5} files ({conflicts_pct:.1f}%)")
        print(f"🚫 Duplicates:  {stats['duplicates']:>5} files (skipped)")
        print("="*58)

if __name__ == "__main__":
    sort_files()