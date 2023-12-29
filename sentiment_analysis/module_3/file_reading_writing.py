'''
Authors: Alex Wernex and Zachery Linscott
Purpose:
    file_reading_writing.py
    This file simply takes a list of the comments and the filepath of the output file
    and outputs said file. This function opens the file, then goes throught the list
    comment by comment. It then alternates writting the comment and a line separator
    to the file.                                                                                                                                                   #
    Added by Zach:
    extract_cleaned_comments(): simply reads the comments from a file and puts them
    in a list.

    sentiments_file_write(): takes a file name, a list of reddit comments,
    and a list of the comments' sentiments, writing them to the file
    with the given name in CSV format.
'''



def output_comments(data, to_file):
    page_break = f"\n"
    output = open(to_file, "w", encoding="utf8")
    for line in data:
        output.write(line.replace("\n", " "))
        output.write(page_break)

    output.close()


# reads  the processed comments from comments.txt and returns them in a list
def extract_file_lines(file_name: str) -> []:
    with open(file_name, 'r', encoding='utf-8') as f:
        lst = [line.strip() for line in f]

    return lst


# writes the comments and sentiment of the comments to a new file.
def sentiments_file_write(file_name: str, comments: [], comment_sentiments: []):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(len(comments)):
            f.write("{}\n".format(comment_sentiments[i]))
