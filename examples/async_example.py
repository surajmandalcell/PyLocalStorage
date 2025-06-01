#!/usr/bin/env python3
"""Async example for localStoragePro."""

import asyncio
import sys
print("Python version:", sys.version)

try:
    from localStoragePro import async_lsp
    print("Successfully imported async_lsp")
except ImportError as e:
    print("Import error:", e)

async def main():
    """Main async function."""
    print("=== Testing Asynchronous API ===")
    
    try:
        # Initialize
        print("Initializing async_lsp...")
        await async_lsp('example.async', 'sqlite').clear()
        print("Initialization successful")
        
        # Set values
        await async_lsp.setItem('name', 'Suraj Mandal')
        await async_lsp.setItem('project', 'localStoragePro')
        print("Values set successfully")
        
        # Get values
        name = await async_lsp.getItem('name')
        project = await async_lsp.getItem('project')
        print(f"Name: {name}")
        print(f"Project: {project}")
        
        # Get all values
        all_data = await async_lsp.getAll()
        print(f"All data: {all_data}")
        
        # Cleanup
        await async_lsp.clear()
        print("Storage cleared")
    except Exception as e:
        print(f"Error during async operations: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Starting async example...")
    try:
        asyncio.run(main())
        print("Async example completed successfully")
    except Exception as e:
        print(f"Error running async example: {e}")
        import traceback
        traceback.print_exc() 