import pandas as pd
import os
import time

timestamp = time.strftime("%Y%m%d-%H%M%S")

csvPath = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFileb2.csv'

df = pd.read_csv(csvPath)

html_table = df.to_html(index=False, classes=["table", "table-striped", "table-bordered"])
workingDir = os.path.dirname(csvPath)
filename, file_extension = os.path.splitext(str(csvPath))
fileBaseName = os.path.basename(filename)
htmlFileName = f'{workingDir}/{fileBaseName}_{timestamp}.html'

with open(htmlFileName, "w") as f:
    f.write(html_table)