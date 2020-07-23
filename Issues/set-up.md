## Setting up your development environment
You're almost ready to start coding, but first you have to set up your computer so  you can test your program while you code.
### Download git and connect to your GitHub account
- If you don't already have git on your computer you can download it [here](https://git-scm.com/downloads)
- Connect to GitHub on
   - [Windows](https://www.pluralsight.com/guides/using-git-and-github-on-windows)
   - [Mac](https://kbroman.org/github_tutorial/pages/first_time.html)
   - [Linux](https://www.howtoforge.com/tutorial/install-git-and-github-on-ubuntu/#-configuring-github)
### Adding the Project to your Local Machine
You need to add this repository to your computer to make changes and edit it in the development environment. Go ahead and [clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository on your computer. Make sure you're in a directory that you'll remember/ is easy to access. If you're not sure, your Desktop is a good go-to.
![cloning-repo](https://user-images.githubusercontent.com/45152371/86035053-800f5700-b9f0-11ea-9b7a-e2201286067b.GIF)
   
Open your **Command Line** (probably called Terminal or Command Prompt)

In command line:
```sh
>cd desktop
>git clone <copied link here>
```
example:
```sh
cd desktop
git clone https://github.com/hightechu/project-template.git
```

## Installing Requirements
If you don't already, make sure you [install python3](https://www.python.org/downloads/)

Now navigate into your project folder on command line and install the required packages:
```sh
>cd <project-repository-name>
>pip3 install -r requirements.txt
```
## Download Large Data Set

- Go to https://github.com/hightechu/sci-fi-or-fantasy-data
- Click on movie_description.csv

![click on movie_descriptions.csv](https://user-images.githubusercontent.com/45152371/88113402-94192500-cb66-11ea-8c28-08b353063819.png)
- Click download and it will take you to page with a lot of text

![click downlaod](https://user-images.githubusercontent.com/45152371/88113474-b3b04d80-cb66-11ea-9586-c12002c297aa.png)
- Right click in white space and select "save as" 

![right click and save as](https://user-images.githubusercontent.com/45152371/88113515-c460c380-cb66-11ea-9090-62f8c3c3ac47.png)
- Save as **movie_descriptions.csv** into your project folder

![save as movie_descriptions.csv](https://user-images.githubusercontent.com/45152371/88113567-df333800-cb66-11ea-96f2-c44d9f9c34d1.png)
 
- Create a [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
