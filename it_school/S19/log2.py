from datetime import datetime
from pathlib import WindowsPath
import pathlib
import sys
import logging

# configuram root logger pentru a scrie in fisier
# default fisierele se deschid in mode append(adaugare)

# file mode :
#   r = read
#   a = append
#   w = write

root = pathlib.Path(__file__).parent

log_path = root.joinpath("logs")
log_filename = datetime.now().strftime("%d%m%Y_%H%M.log")
log_abs_path = log_path.joinpath(log_filename)
# creem folderul de loguri
try:
    log_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)



logging.basicConfig(filename="log2.log", level = logging.INFO, filemode="w")

logging.info("Starting...")

logging.debug(f"Running on Python: {sys.version}")

logging.info("Job done. Existing...")




#23062022_1925.log

