quests = []

def quest_id(list):
	output = {}
	for each in list:
		output.update({list.index(each)+1:each})
	return output
		
ans = {}
