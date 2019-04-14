### To fix stupid Swarp headers with float NAXIS



from functools import partial
import sys, shutil
with open('fileX.resamp.fits', 'rb') as input_file:
    with open('temp.fits', 'wb') as temp_file:
         while True: # Until EOF
            chunk = input_file.read(80)  #
            if not chunk:
                break
            if chunk.startswith(b'NAXIS '):
               chunk = chunk.replace(b'NAXIS   =   2.000000000000E+00 /',b'NAXIS   =                    2 /')
            temp_file.write(chunk)

shutil.move('temp.fits', 'fileX.resamp.fits')
