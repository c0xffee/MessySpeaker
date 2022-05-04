import os


def fix_github_delay():
  fname = 'README.md'
  with open(fname, 'a+') as f:
    f.write(' ')

cmds = '''
git pull
git add -A
git commit -am "cool"
git push
'''
cmds = [cmd for cmd in cmds.split('\n') if cmd != '']

fix_github_delay()

for cmd in cmds:
  print(cmd)
  os.system(cmd)