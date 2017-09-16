from random import randint
import subprocess

def main(argv):
	commit_num = int(argv[0])
	Kieek = "Kieek"
	for _ in range(commit_num):
		subprocess.call("echo '" + Kieek + str(randint(0, 1000000)) +"' > Kieek.txt; git add Kieek.txt; GIT_AUTHOR_NAME='" + Kieek + "' GIT_AUTHOR_EMAIL='" + Kieek + "' GIT_COMMITTER_NAME='" + Kieek + "' GIT_COMMITTER_EMAIL='" + Kieek + "' git commit -m 'Kieek';", shell=True)

	subprocess.call("git push;", shell=True)
	subprocess.call("git rm Kieek.txt; GIT_AUTHOR_NAME='" + Kieek + "' GIT_AUTHOR_EMAIL='" + Kieek + "' GIT_COMMITTER_NAME='" + Kieek + "' GIT_COMMITTER_EMAIL='" + Kieek + "' git commit -m 'Kieek'; git push;", shell=True)

if __name__ == "__main__":
	main(sys.argv[1:])
