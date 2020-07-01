
"""
This is a small program to take a basic text file and convert it into a basic html page
Because this is a learning project meant to be done at the end of the day 'before bed', 
it's super basic. It works none the less though.

Therer's bound to be bugs in this code if you experiment enough with it.
For instance, there's no error handling for reading in and saving files.
Think of it more of a 'proof of concept' rather than an actual software.

In a basic run-down of the idea:
There is a template file called 'template.html'. In it there is a string --> |b|
The code searches for that string in the template file and replaces it with the contents of
whatever is in test.txt, or whatever other text document you chose to use.
It then saves the whole document as a new file, called 'test.html' in this case.

The new text is 'inserted' (really it's been replaced) between the body tags inside the template file.

That's all this code does. 

Software By Anguel Esperanza
"""


def read_file(filename):
    with open(filename) as f:
        filename = f.readlines()
    return filename

def get_template():
    template = ''
    with open('template.html', 'r') as f:
        template = f.readlines()
    return template

def put_in_body(file, template):
    count = 0
    body_tag = 0
    for i in template:
        count += 1
        if '|b|' in i:
            body_tag = count - 1
    
    text_to_append = ""
    for line in file:
        text_to_append += line

    formatted_text = ""
    for word in text_to_append:
        formatted_text += word
        if '\n' in word:
            formatted_text += word.replace('\n', '<br/>\t')    

    template[body_tag] = template[body_tag].replace('|b|', formatted_text)

    for i in template:
        print(i)


    return template 

def save_template(name_of_doc, saved_doc_file):
    with open(name_of_doc, 'w') as f:
        f.writelines(saved_doc_file)
    

def put_in_title():
    pass


def main():
    content = read_file('test.txt')
    template = get_template()
    formatted_template = put_in_body(content, template)

    save_template('test.html',formatted_template)

if __name__=='__main__':
    main()