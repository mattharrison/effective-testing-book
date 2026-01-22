import sys

def pytest_runtest_setup(item):
    with open('.demo_test_log', 'a') as f:
        f.write(f"\nAbout to run: {item.name}\n")
    