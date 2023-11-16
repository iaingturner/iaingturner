import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ydata-profiling'])

import pandas as pd
df = pd.read_csv('testfile.csv')

from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')