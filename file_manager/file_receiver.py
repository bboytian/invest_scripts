# -------
# imports

import getpass as gp
import numpy as np
import os
import os.path as osp
import shutil as st


# ---------
# operation


investrepo_dir = osp.dirname(osp.dirname(osp.dirname(osp.abspath(
    __file__))))
inbox_dir = investrepo_dir + '/inbox'

# getting latest file
filedates_ara = np.array([f[-13:-5] for f in\
                          os.listdir(inbox_dir)\
                          if f[-5:] == '.xlsx'\
                          and f[:9] == 'datastore'])
filedates_ara.sort()
datastore_file = inbox_dir+'/datastore_{}.xlsx'.format(filedates_ara[-1])

# replacing old file; this doesnt copy permissions and metadata
#                   ; use st.copy or st.copy2 if that is desired
st.copyfile(datastore_file, investrepo_dir + '/datastore.xlsx')
