# dir_word_searcher
### Search a given keyword in all files and subfolders in a given directory

#### Running the program
1. insert a keyword to search the directory
2. insert the directory to do the searching
3. add additional cases for the search. Inserted as a single string. Not necessarily upper case. Ignore if not applicable.
    - C: for case sensitive searches
    - B: to include searching for binary files, otherwise ignored
    - J: to just show the files involved, no line number
    - F: to include search for file/dir names
    - M: to search multiple keywords in a single line. Only appear if 2 or more words given.
    > sample search:
    > - `C` - to include case sensitive search
    > - `B` - to search binary file
    > - `BC` - to perform case sensitive search and binary file search

#### Using the program from CLI (update patch 1.3)
1. Run the program from CLI using the keywords:
    - `<file_name> <space-separated searched words> --path="<file path>" --option=<options>`, where:
      - `<file_name>` is the Python file name, which is `dir_word_search.py`. Mandatory.
      - `<space-separated searched words>` are the words you need to search. Mandatory.
      - `--path="<file path>"` is the path to the folder you want to perform the search. Please include in double quote `"`. If not included, the search will be done within the current directory where the file `dir_word_search.py` exist.
      - `--option=<options>` is the string that contains the action hotkeys. Not mandatory.
> Sample usage:
> - `dir_word_search.py div --path="D:\coding\python\" --option=BJF`
> - `dir_word_search.py class mdi mdi-delete --path="D:\flask\flask_project\templates" --option=JM`

#### Patch 1.1 8th Oct 2020
- Added options J, F, M, N.
- Enable searching of multiple keywords.

#### Patch 1.2 11th Oct 2020
- Removed option N. If option M is not selected, the searching performs the search for multiple keywords within the document.
- Added error handling for wrong file path.
- Added support for Linux.

#### Patch 1.3 4th Mar 2021
- Added functionality to be accessible from CLI without the need for the program to be executed.
- Implemented code linting onto main file using [pycodestyle](https://pypi.org/project/pycodestyle/), ignoring rule E501.
