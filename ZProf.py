__author__ = 'Lalit Kumar'


class FileName:
    File = ''

class FileName2:
    File2 = ''


class FileName3:
    File3=''

class Viewdef:
    Zprof = 0

class Link:
    LinkDisp =0 #Flag to Set LinkDisplay ON and OF (0 for ON and 1 for OF)
    DispNo1 = 0  #Set for the Display for which Z-Profile Graph has to be Plot during Display Linking
    DispNo2 = 0
    DynamicOverlay = 0  #Flag to set Dynaamic Overlay ON and OF (0 for ON and 1 for OF)
    ActiveDisplays = 0  #Count the number of Active Viewers (Max allowed are 2)
    ActiveOpenImage = 0 #Count the Number of Open_Image Windows that are Currently been used been opened (Max allowed are 2)
    Open1 = 0   #Its set to One when open_Image class object is  constructed from the main HYDAS Screen
    Open2 = 0   #Its set to One when open_Image class object is  constructed from the main HYDAS Screen
    cursor1 = 0
    cursor2 = 0
    linkcursor = 0
    InfoWin = 0
