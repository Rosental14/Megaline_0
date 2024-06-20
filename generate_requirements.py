import pandas as pd
import numpy as np
import scipy as sp
import seaborn as sns
import matplotlib as mpl

# Obtendo as versões das bibliotecas
libraries = {
    'pandas': pd.__version__,
    'numpy': np.__version__,
    'scipy': sp.__version__,
    'seaborn': sns.__version__,
    'matplotlib': mpl.__version__
}

# Escrevendo no arquivo requirements.txt
with open('requirements.txt', 'w') as f:
    for lib, version in libraries.items():
        f.write(f'{lib}=={version}\n')
