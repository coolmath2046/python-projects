import urllib.request
import xml.etree.ElementTree as ET
#import xmltodict


#constants
mw_key = '8feb0353-b60a-45b8-ba4f-6f317d5e2c20'
collegiate_dict = 'collegiate'
learners_dict = 'learners'
url_prefix = 'http://www.dictionaryapi.com/api/v1/references'
wav_url_prefix = 'http://media.merriam-webster.com/soundc11'
SLASH = '/'

################# mw web service XSD tag elements #########################
entry_list = 'entry_list'   #this is most likely the root element
entry = 'entry'             #Dictionary Entry, child of <entry_list>
#children of <entry>
pronunciation_tag = 'pr'
etymology_tag = 'et'
part_of_speech_tag = 'fl'             #FUNCTIONAL LABEL

###########
definition_tag = 'def'      #umbrella field for definition info
sense_no_tag = 'sn'         #SENSE NUMBER (if there are multiple meanings, a sense refers to a meaning)
definition_text_tag = 'dt'  #DEFINING TEXT
###########
##########################################################################


def createWebSrvcUrl(word, ref = collegiate_dict, key = mw_key):
    '''
    Create the URL that will be used to access the Merriam-Webster dictionaryapi web service
    Parameters:
    word = the word to look up
    ref = the dictionary to use for the lookup (collegiate or learner's).  default is the collegiate
    key = the key to use to access the API. Provided by M-W. defaults to the mw_key constant
    '''
    word = urllib.parse.quote(word)  #handle encoding special characters in url (e.g. change space char to "%20")
    url = url_prefix + SLASH + ref + SLASH + 'xml' + SLASH + word + '?key=' + key
    return url

def callMW(word):
    '''Calls the Merriam Webster Dictionary API to get the definition of the passed in word'''
    mw_url = createWebSrvcUrl(word)
    data = urllib.request.urlopen(mw_url).read()
    #print(data)
    strData = data.decode("utf-8") #convert bytes to string
    return strData

def writeToFile(fileName,data):
    '''
    Copy the data to file
    in open() method, 'w' means to write, and encoding ='utf-8' is necessary to handle unicode in the xml file
    '''
    with open(fileName,'w', encoding='utf-8') as myfile:
        myfile.write(data)
    return

def test_readFromFile() :
    #from file
    tree  = ET.parse('testfile.xml')   
    root = tree.getroot()
    return root

def test_callWebService(word) :
    data = callMW(word)
    writeToFile('testfile.xml',data)
    root = ET.fromstring(data)
    return root

def test(lookup):
    '''my test class'''

    root = test_callWebService(lookup)
    #root = test_readFromFile()    #run against the file we already created from a previous web service call
    
    for wordentry in root.findall(entry):
        #find the matching entry.  there might be multiple words that match, and we only want the exact match

        ew_node = wordentry.find('ew')
        wordtext = ew_node.text
        
        if (wordtext == lookup):
            #get the location of the .wav (sound) file
            wavnode = wordentry.find("./sound/wav")
            if wavnode is not None:
                wavtext = wavnode.text
                wavurl = wav_url_prefix + SLASH + wavtext[0] + SLASH + wavtext
                print ('URL of wav file:', wavurl)
            #get the pronunciation
            pronunc_node = wordentry.find(pronunciation_tag)
            if (pronunc_node is not None) :
                print ('pronunciation:',pronunc_node.text)

            #get the part of speech
            pos_node = wordentry.find(part_of_speech_tag)
            if (pos_node is not None) :
                print(pos_node.text)
                      
            #get the etymology
            etymology_node = wordentry.find(etymology_tag)
            if (etymology_node is not None) :
                print ('etymology:',etymology_node.text)

            #get the definition
            definition_node = wordentry.find(definition_tag)
            #get all the child elements of the definition
            for child in definition_node:
                print(child.tag, child.attrib, child.text)
               #TODO: if there are additional child elements, then the parent.text tag doesn't work properly
               #e.g., there's a 3rd <dt> element with value of ":<sx>cuisine></sx>", but .text only shows the ":"
                #figure out how to fix this using child.itertext()
                #for i in child.itertext:
                #   print(i)
                
            
            
            

            break;  #break out of the loop once the word is found
    return

test('string')

