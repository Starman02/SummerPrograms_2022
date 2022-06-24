import json

# define list with values
basicList = ["cope", "ringatony", "whatyuadoooooooin"]




# open output file for writing
with open('D:\Summer_Programs_2021\Project_ADAM\ADAM_AI_STORAGE\ADAM_SEARCH_ENGINE.txt', 'w') as filehandle:
    json.dump(basicList, filehandle)












# open output file for reading
with open('D:\Summer_Programs_2021\Project_ADAM\ADAM_AI_STORAGE\ADAM_SEARCH_ENGINE.txt', 'r') as filehandle:
    pickled_list = json.load(filehandle)
print(pickled_list)