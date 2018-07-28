import sys
print(sys.path)

path='C:\Program Files\Common Files\Microsoft Shared\Windows Live;C:\Program Files (x86)\Common Files\Microsoft Shared\Windows Live;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\AMD APP\bin\x86_64;C:\Program Files (x86)\AMD APP\bin\x86;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\ATI Technologies\ATI.ACE\Core-Static;C:\Program Files (x86)\Windows Live\Shared;C:\Program Files (x86)\QuickTime\QTSystem\;C:\Program Files (x86)\AMD\ATI.ACE\Core-Static;C:\Program Files (x86)\Brackets\command;G:\Program Files\Git\cmd;G:\Program Files\MATLAB\R2016b\runtime\win64;G:\Program Files\MATLAB\R2016b\bin;C:\Users\Kyle\Anaconda3;C:\Users\Kyle\Anaconda3\Scripts;C:\Users\Kyle\Anaconda3\Library\bin;C:\Users\Kyle\AppData\Local\Microsoft\WindowsApps;C:\Program Files (x86)\AllWinnertech\PhoenixSuit\'
paths = path.split(';');

for each paths as p
sys.path.append(p);

while True:
    Welcome_statement = print ('Hello! welcome to Politics app v1.0 :))))))')

    ###categories = [legislative, social, bills]

    user_input = input('What would you like to research?:')



    ### this is the parcer###
    from lxml import html
    import requests

    page = requests.get('https://www.congress.gov/search?q={%22congress%22:%22115%22,%22source%22:%22legislation%22,%22search%22:%22' + user_input + '%22}&searchResultViewType=expanded')
    tree = html.fromstring(page.content)



    #https://www.congress.gov/search?q={%22congress%22:%22115%22,%22source%22:%22legislation%22,%22search%22:%22user_input%22}&searchResultViewType=expanded
    if tree == no:
        break
