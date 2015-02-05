import shutil,os,sys,subprocess,glob

def getDirs(foldername):
    return os.walk(foldername).next()[1]

os.chdir('WaveletCode')
print "\n"
print "\t   ################ PyMC WAVELET CODE ################"
print "\n "
print "\t      Author: Nestor Espinoza (nespino@astro.puc.cl)"
print "\n"
print "\t    ---------------------------------------------------"
print "\t   About the code:"
print "\n"
print "\t   If you use this code for your research, please cite the work "
print "\t   of Carter & Winn (2009, http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:0909.0747) and "
print "\t   acknowledge the hardwork put into this implementation by the author."
print "\t   "
print "\t   For a tutorial on using this code, please go to: http://randomastronomy.wordpress.com"
print "\t   ---------------------------------------------------"
print "\n"
print "\t   > Installing the FWT library..."
p = subprocess.Popen('python setup.py build',stdout = subprocess.PIPE, stderr = subprocess.PIPE,shell = True)
p.wait()
if(p.returncode != 0 and p.returncode != None):
     print "     ----------------------------------------------------------"
     print "     > ERROR: FWT Library couldn't be installed."
     print "     > Problem building the code. The error was:\n"
     out, err = p.communicate()
     print spaced(err,"\t \t")
     print "     > If you can't solve the problem, please communicate"
     print "     > with the Nestor Espinoza (nespino@astro.puc.cl) for help.\n \n"
     os.chdir(cwd)
     sys.exit()

libfolder = getDirs('build/.')
for name in libfolder:
     if(name[0:3]=='lib'):
        filename = glob.glob('build/'+name+'/*')
        shutil.copy2(filename[0],'.')
shutil.rmtree('build')
os.chdir('..')
print '\t   > FWT Library installed successfully!'
print '\t   > PyMC Wavelet Code installed successfully!'
print '\n'
