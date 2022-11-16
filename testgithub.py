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

with open('foo/testgithub.py', 'w') as fp:
    with open('testgithub.py', 'r', encoding='utf-8') as fp2:
        fp.write(fp2.read())
        fp2.close()
        fp.close()

repo = git.Repo(to_path)
repo.git.checkout('new_branch')
<<<<<<< HEAD
repo.git.push('--delete', 'origin', 'new_branch')
=======
ufiles = repo.untracked_files
for f in ufiles:
    print(ufiles)
    repo.git.add(f)
    repo.git.commit(f, message='new file', author='gurasho')
repo.git.push('origin', 'new_branch')
print(repo.git.branch() )
>>>>>>> d0b9b0eba42b0d28a7273579ee0b9d5595e207f3

