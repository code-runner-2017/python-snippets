import pathlib
import itertools
import os

# https://pymotw.com/3/pathlib/index.html

# Operator '/' to compose paths
usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)

# joinpath
root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)

# parsing paths

p = pathlib.PurePosixPath('/usr/local')
print(p.parts)      # ('/', 'usr', 'local')

# .parent
p = pathlib.PurePosixPath('/usr/local/lib')

print('parent: {}'.format(p.parent))

print('\nhierarchy:')
for up in p.parents:
    print(up)

# name, suffix, stem
p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print('path  : {}'.format(p)) # path  : source/pathlib/pathlib_name.py
print('name  : {}'.format(p.name)) # name  : pathlib_name.py
print('suffix: {}'.format(p.suffix)) # suffix: .py
print('stem  : {}'.format(p.stem)) # stem  : pathlib_name

# directory contents

p = pathlib.Path('.')

for f in p.iterdir():
    print(f)

# find matching patterns
print('---- matching:')

for f in p.glob('*.py'):
    print(f)

# Directories

p = pathlib.Path('output/subdir/example_dir')

print('Creating {}'.format(p))
p.mkdir(exist_ok = True, parents=True)   # no error if exists, create the whole path

# Remove directory
# Note cannot remove directly 'subdir' because it isn't empty
p.rmdir();  # remove output/subdir/example_dir
pathlib.Path('output/subdir').rmdir(); # remove output/subdir

# Scan directory

root = pathlib.Path('.')

to_scan = itertools.chain(
    root.iterdir(),
    [pathlib.Path('/dev/disk0'),
     pathlib.Path('/dev/console')],
)
hfmt = '{:18s}' + ('  {:>5}' * 6)
print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block',
                  'Character'))
print('-------- directory scan -----------')

fmt = '{:20s}  ' + ('{!r:>5}  ' * 6)
for f in to_scan:
    print(fmt.format(
        str(f),
        f.is_file(),
        f.is_dir(),
        f.is_symlink(),
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
    ))
