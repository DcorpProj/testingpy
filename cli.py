import glob
import subprocess
to_test = glob.glob("./test_*.py") + glob.glob("./*_test.py")
for file in to_test:
    print(f"-------- {file} --------")
    subprocess.run(["python3", file])
