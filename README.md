# dir_word_searcher
### Search a given keyword in all files and subfolders in a given directory

1. insert a keyword to search the directory
2. insert the directory to do the searching
3. add additional cases for the search. Inserted as a single string. Ignore if not applicable.
    - C: for case sensitive searches
    - B: to include searching for binary files, otherwise ignored
    - J: to just show the files involved, no line number
    - F: to include search for file/dir names
    - M: to search multiple keywords in a single line
    - ~~N: to search multiple keywords within the document
    > sample search:
    > - `C` - to include case sensitive search
    > - `B` - to search binary file
    > - `BC` - to perform case sensitive search and binary file search

#### Patch 1.1 8th Oct 2020
- Added options J, F, M, N
- Enable searching of multiple keywords

#### Patch 1.2 11th Oct 2020
- Removed option N. If option M is not selected, the searching performs the search for multiple keywords within the document.
- Added error handling for wrong file path
- Added support for Linux
