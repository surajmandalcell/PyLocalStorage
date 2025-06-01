#!/usr/bin/env python3
"""
LocalStoragePro Example - Demonstrating New Functionality

This example demonstrates the get_all, get_many, and remove_all functions
that have been added to LocalStoragePro.

Author: Suraj Mandal
GitHub: https://github.com/surajmandalcell/LocalStoragePro
"""

from localStoragePy import localStoragePy
import json

def main():
    print("LocalStoragePro - New Functionality Demo")
    print("=" * 45)
    print("Maintainer: Suraj Mandal")
    print("GitHub: https://github.com/surajmandalcell")
    print("=" * 45)
    
    # Initialize with JSON backend for easy inspection
    localStorage = localStoragePy('demo.surajmandal', 'json')
    localStorage.clear()  # Start fresh
    
    print("\n1. Setting up sample data...")
    
    # Store some sample user data
    localStorage.setItem('name', 'Suraj Mandal')
    localStorage.setItem('email', 'contact@surajmandal.com')
    localStorage.setItem('github', 'https://github.com/surajmandalcell')
    localStorage.setItem('project', 'LocalStoragePro')
    localStorage.setItem('language', 'Python')
    localStorage.setItem('version', '0.3.0')
    
    # Store JSON data
    settings = {
        'theme': 'dark',
        'notifications': True,
        'autoSave': False
    }
    localStorage.setItem('settings', json.dumps(settings))
    
    print("   ✓ Stored 7 items")
    
    print("\n2. Using getAll() to retrieve all data:")
    all_data = localStorage.getAll()
    for key, value in all_data.items():
        if key == 'settings':
            # Pretty print JSON data
            settings_obj = json.loads(value)
            print(f"   {key}: {settings_obj}")
        else:
            print(f"   {key}: {value}")
    
    print(f"\n   Total items stored: {len(all_data)}")
    
    print("\n3. Using getMany() to retrieve specific items:")
    user_info = localStorage.getMany(['name', 'email', 'github'])
    print("   Requested: ['name', 'email', 'github']")
    print("   Retrieved:")
    for key, value in user_info.items():
        print(f"     {key}: {value}")
    
    print("\n4. Using getMany() with mixed existing/non-existing keys:")
    mixed_request = ['name', 'nonexistent', 'version', 'missing_key']
    mixed_result = localStorage.getMany(mixed_request)
    print(f"   Requested: {mixed_request}")
    print(f"   Found: {list(mixed_result.keys())}")
    print(f"   Missing: {set(mixed_request) - set(mixed_result.keys())}")
    
    print("\n5. Performance comparison - individual vs bulk retrieval:")
    import time
    
    # Individual retrieval
    start_time = time.time()
    individual_results = {}
    for key in ['name', 'email', 'github', 'project', 'language']:
        individual_results[key] = localStorage.getItem(key)
    individual_time = time.time() - start_time
      # Bulk retrieval
    start_time = time.time()
    bulk_results = localStorage.getMany(['name', 'email', 'github', 'project', 'language'])
    bulk_time = time.time() - start_time
    
    print(f"   Individual getItem() calls: {individual_time*1000:.2f}ms")
    print(f"   Single getMany() call: {bulk_time*1000:.2f}ms")
    if bulk_time > 0:
        print(f"   Bulk retrieval is {individual_time/bulk_time:.1f}x faster!")
    else:
        print("   Both methods are very fast on this system!")
    
    print("\n6. Using removeAll() to clean up:")
    print(f"   Before removeAll(): {len(localStorage.getAll())} items")
    localStorage.removeAll()
    print(f"   After removeAll(): {len(localStorage.getAll())} items")
    
    print("\n7. Verifying storage is empty:")
    remaining_data = localStorage.getAll()
    if not remaining_data:
        print("   ✓ Storage is completely empty")
    else:
        print(f"   ⚠ Unexpected: {len(remaining_data)} items remaining")
    
    print("\n" + "=" * 45)
    print("Demo completed successfully!")
    print("\nNew methods demonstrated:")
    print("  • getAll() - Retrieve all stored key-value pairs")
    print("  • getMany(keys) - Efficiently retrieve multiple specific values")
    print("  • removeAll() - Remove all stored data")
    print("\nFor more examples, see the README.md file.")
    print("GitHub: https://github.com/surajmandalcell/LocalStoragePro")

if __name__ == "__main__":
    main()
