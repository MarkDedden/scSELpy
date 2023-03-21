
import nbclean

def AppendToMDFile():
    """
        # Tutorial
    ```{eval-rst}
    .. role:: small
    ```
    
    
    ```{eval-rst}
    .. role:: smaller
    ```
    """



def RemoveMockMentions():
    RemoveMockList = ['FirstMock','SecondMock','ThirdMock','OverwriteMock','Mock_line','White_line_mock','Own_name_mock']    
    with open("docs/source/Tutorial.ipynb", "r") as initial_file:
        text = initial_file.read()
        for Remove in RemoveMockList:
            text = text.replace(",mock="+Remove, '')
    
    with open("docs/source/Tutorial.ipynb", "w") as new_file:
            new_file.write(text)

        
def CleanNB():
    ntbk = nbclean.NotebookCleaner("docs/Mock/Tutorial.ipynb")
    
    
    ntbk.clear('stderr')
    ntbk.remove_cells(tag='remove')
    ntbk.remove_cells(tag='remove_if_empty', empty=True)

    
    ntbk.save("docs/source/Tutorial.ipynb")
    RemoveMockMentions()
    ntbk2 = nbclean.NotebookCleaner("docs/Mock/Mock.ipynb")
    
    
    ntbk2.clear('stderr')
    ntbk2.remove_cells(tag='remove')
    ntbk2.remove_cells(tag='remove_if_empty', empty=True)
    
    ntbk2.save("docs/source/Mock.ipynb")
    
    
    
