import git
import os

repo = git.Repo.init(path='.')

g = repo.git
g.add("--all")
g.commit("-m Push Github")
g.push()
print("成功推上去了!")