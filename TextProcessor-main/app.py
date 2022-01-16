from flask import Flask, json, request
import re
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm') #Trained language model from spacy
app = Flask(__name__) #create an instance of the class app flask
args = [
                ("\\\r\\\n", " "), #Removes \r\n
                ("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", " "), #Removes links
                ("\\< \\>", " "), #removes < >
                ("\\[ \\]", " "),# Removes [\\]
                ("\\[.*?\\]", " "), #Removes text within [ ]
                ("\\<.*?\\>", " "), #Removes text within <>
                ("________________________________", " "), #Removes dashes
                ("\\*", " "), #Removes dashes
                ("CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe.", " "),
                ("  ", " "),
                ("[ ]{2,}"," "), #Removes every empty space whose len is greater than 1
    ]
def clean_data(args, text):
    # Create a regular expression  from the tuple
    for old, new in args:
        text = re.sub(old, new, text)
    return text
def claflin():
    matcher = Matcher(nlp.vocab)
    #Needs improvement
    pattern = [
            [{"LOWER": "apply"}],[{"LOWER": "opportunity"}],[{"LOWER": "internship"}],[{"LOWER": "intern"}], [{"LOWER": "recruiter"}],[{"LOWER": "opportunities"}],[{"LOWER": "event"}]
            ]
    finalData = {"mimetype":"application/json"   
    } #Holds cleaned data whose senders are from Claflin and whose body contains the above keywords
    arr = []
    for mail in data:  
        subdata = {}
        claflinMail = re.search('@claflin\\.edu$', mail['sender']['emailAddress']['address'] )  
        if claflinMail:
            #Save links in a separate map for later use
            subdata['Links'] = re.search("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", mail['body']['content'])
            body = clean_data(args, mail['body']['content'])
            doc = nlp(body)
            #text1= spacy.NER(bod)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            print(entities)
            matcher.add("OpportunityKeys", pattern)
            matches = matcher(doc)
            for match_id in matches:
                if match_id and (mail['id'] not in finalData):
                    document = nlp(body)
                    entities = [(ent.text, ent.label_) for ent in document.ents]
                    finalData[str(mail["id"])] = {"body": body, "subject":mail["subject"], "sender": mail["sender"], "entities": entities}
    return finalData
@app.route('/', methods=['GET', 'POST'])
def filterSenders():
    main_data = request.get_json()
    if main_data is not None:
        data = json.dumps(claflin(), indent = 5)
        return data
    else:
        return "<h1>empty response</h1>"