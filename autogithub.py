#https://blog.imind.jp/entry/2020/01/18/065638
import webbrowser,sys,os
import git

url = 'https://github.com/gurasho/pythonmemo.git'
to_path = 'foo'
if not os.path.exists('foo'):
    git.Repo.clone_from(
        url,
        to_path
    )

with open('foo/autogithub.py', 'w') as fp:
    with open('autogithub.py', 'r', encoding='utf-8') as fp2:
        fp.write(fp2.read())
        fp2.close()
        fp.close()

repo = git.Repo(to_path)
# repo.git.branch('new_branch') 
repo.git.checkout('main')
ufiles = repo.untracked_files
for f in ufiles:
    repo.git.add(f)
    repo.git.commit(f, message='new file', author='gurasho')
repo.git.push('origin', 'main')
# repo.git.push('--delete', 'origin', 'main')

webbrowser.open('https://github.com/gurasho')
