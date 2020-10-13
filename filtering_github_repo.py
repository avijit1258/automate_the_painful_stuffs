import csv
import os
import random


def get_all_py_files(root):
        all_py = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                if name.endswith('.py'):
                    all_py.append(os.path.join(path, name))
                    # print(os.path.join(path, name))

        return all_py


def clone_count_repo(repository):
    # print(repository.split('/'))
    repo_last_name = repository.split('/')[4]
    print("Cloning repo: ", repository)

    git_clone = "git clone  " + repository

    os.system(git_clone)
    current_wd = os.getcwd()
    target_repo = current_wd + "/" + repo_last_name

    print(' Github repo:  ' +repository + ' py files :' + str(len(get_all_py_files(target_repo))))

    os.system("rm -rf "+ repo_last_name)
    return 

def get_count_of_selected_repos(repos):

    for r in repos:
        clone_count_repo(r)

    return




def read_csv():

    """
    Reads a csv file and process the repo for git clone command
    Returns a list of repositories to be analyzed 
    """

    
    with open('PythonProj_numPR.csv', mode='r') as csv_file:
        repos = []
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            line_count += 1
            # print(row['url'].split('/'))
            # if line_count == 5:
            #     break
            try:
                raw_url = row['url'].split('/') # ['https:', '', 'api.github.com', 'repos', 'pydata', 'pandas']
            except AttributeError as error:
                # print('ops' + row['url'])
                return len(repos)
            url = 'https://github.com/' + raw_url[4]+ '/'+ raw_url[5]
            repos.append(url)
            # clone_repo(url)

            
    # csv_to_dict = {id[i]: [date[i], message[i]] for i in range(len(id))}

    # return csv_to_dict
    repos = random.sample(repos, 10)
    print(repos)
    return repos

if __name__ == "__main__":
    get_count_of_selected_repos(read_csv())