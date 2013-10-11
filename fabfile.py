import os
from fabric.api import *

top = ['Systems','Programming','Networking','Web','Cloud','Robotics','Misc']

@task
def clean():
    local('rm -rf _build/doctrees')

def _load_meta(dname):
    '''read meta file in named directory'''
    try:
        fin = open('%s/_meta.rst' % dname, 'r')
        lines = fin.readlines()
        fin.close()
    except:
        lines = []
    return lines

def _open_index(dname):
    '''
        Given a dirname, create an index.rst file in that directory
        Add an entry for each subdirectory and any bare files
    '''
    title = ''
    desc = []
    fout = open(dname + '/index.rst','w')
    lines = _load_meta(dname)
    nlines = len(lines)
    # parse the lines
    for lc in range(nlines):
        if lines[lc].startswith('title'):
            try:
                name, value = lines[lc].split('=')
                title = value.strip()
            except:
                title = 'Bad title in meta'
        if lines[lc].startswith('description'):
            lc += 1
            while lc < nlines:
                line = lines[lc].strip()
                if line.startswith('=='): break
                desc.append(line)
                lc += 1
    if title == '':
        title = dname.split('/')[-1]

    # output the title part
    lt = len(title)
    fout.write("#"*lt + '\n')
    fout.write(title + '\n')
    fout.write("#"*lt + '\n\n')
    fout.write("..  include::  /references.inc\n\n")

    # now output the description, if it exists
    for line in desc:
        fout.write('%s\n' % line)

    # now, set up the TOC part
    fout.write('\n\n..  toctree::\n    :maxdepth: 2\n\n')
    fout.close()


def _add_entry(dname,fname):
    fout = open(dname + '/index.rst','a')
    fout.write('    %s\n' % fname)

def _gen_index(dirname):
    _open_index(dirname)
    entries = os.listdir(dirname)
    entries.sort()
    for entry in entries:
        # scan the entries and add file entries and index files for subdirectories
        if entry.startswith('_') or entry.startswith('.'): continue
        if entry == 'index.rst': continue
        fullname = dirname + '/' + entry
        if os.path.isdir(fullname):
            # recursively handle subdirectories
            _add_entry(dirname,entry + '/index')
            _gen_index(fullname)
        else:
            # add file name to index.rst
            if not entry.endswith('.rst'): continue
            ientry = entry.split('.')[0]
            _add_entry(dirname,ientry)

@task
def build():
    for dname in top:
        _gen_index(dname)
    local('sphinx-build -b html -d _build/doctrees . _build/html')

