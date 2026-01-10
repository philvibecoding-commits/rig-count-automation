"""
Test script to verify rig count automation works locally before deploying to Railway
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_environment():
    """Check if all required environment variables are set"""
    print("Checking environment variables...")
    
    required_vars = ['EMAIL_ADDRESS', 'EMAIL_PASSWORD', 'TO_ADDRESS']
    missing = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing.append(var)
            print(f"  [X] {var}: Not set")
        else:
            # Mask password for security
            if 'PASSWORD' in var:
                masked = '*' * len(value)
                print(f"  [OK] {var}: {masked}")
            else:
                print(f"  [OK] {var}: {value}")
    
    if missing:
        print(f"\n❌ Missing required variables: {', '.join(missing)}")
        print("💡 Create a .env file based on env_template.txt")
        return False
    
    return True

def check_dependencies():
    """Check if all required Python packages are installed"""
    print("\nChecking dependencies...")
    
    required_packages = [
        'requests',
        'beautifulsoup4',
        'pandas',
        'matplotlib',
        'openpyxl',
        'dotenv',
        'schedule'
    ]
    
    missing = []
    
    for package in required_packages:
        try:
            if package == 'beautifulsoup4':
                __import__('bs4')
            elif package == 'dotenv':
                __import__('dotenv')
            else:
                __import__(package)
            print(f"  [OK] {package}: Installed")
        except ImportError:
            missing.append(package)
            print(f"  [X] {package}: Not installed")
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    return True

def test_imports():
    """Test if main script can be imported"""
    print("\nTesting script imports...")
    
    try:
        import rig_count_automation
        print("  [OK] rig_count_automation.py: Can be imported")
    except Exception as e:
        print(f"  [X] rig_count_automation.py: {e}")
        return False
    
    try:
        import rig_count_scheduler
        print("  [OK] rig_count_scheduler.py: Can be imported")
    except Exception as e:
        print(f"  [X] rig_count_scheduler.py: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("Rig Count Automation - Local Test")
    print("=" * 60)
    
    all_passed = True
    
    # Check environment
    if not check_environment():
        all_passed = False
    
    # Check dependencies
    if not check_dependencies():
        all_passed = False
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("SUCCESS: All checks passed! Ready to deploy.")
        print("\nTo test the automation locally:")
        print("   python rig_count_automation.py")
        print("\nTo test the scheduler:")
        print("   python rig_count_scheduler.py")
    else:
        print("ERROR: Some checks failed. Please fix issues above.")
        sys.exit(1)
    print("=" * 60)

if __name__ == '__main__':
    main()

