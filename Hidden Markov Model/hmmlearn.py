
import sys


class pre:
	def preprocessing(self,file):
		#data=[]
		read1=file.read().rstrip("\n")
		data=read1.split("\n")
		#print "data is",data
		sentences=[]
		emission={}
		transition={}
		unique_tags={}
		unique_words={}
		special_tags={}
		for sentence in data:
			sentence="/q0"+" "+sentence
			temp=[" ","q0"]
			sent_obj=[]
			sent_obj.append(temp)
			previous=""
			for splitt in sentence.split(" "):
				#print splitt
				word_tag=[]
				word=splitt[:-3].strip()
				tag=splitt[-2:].strip()
				#print "previous:",previous
				#print "tag:",tag
				if previous=="":
					previous=tag
					unique_tags[previous]=unique_tags.get(tag,0)+1
					continue
				else:
					t=previous+":"+tag
					transition[t]=transition.get(t,0)+1
					#print "hhhh",t
					
				#word_tag.append(word)
				#word_tag.append(tag)
				#sent_obj.append(word_tag)
					word_tag=word+":"+tag
					emission[word_tag]=emission.get(word_tag,0)+1
				special_tags[previous]=special_tags.get(previous,0)+1
				previous=tag
				unique_tags[previous]=unique_tags.get(previous,0)+1

				unique_words[word]=unique_words.get(word,0)+1
			#sentences.append(sent_obj)
		
		#print "unique words",unique_tags
		#print "transition:",transition

		#print sent_obj
		#for i in range(0,len(sent_obj)):
		#	print sent_obj[i].dict
			
		#print "Transition table", transition
		for tag in unique_tags.keys():
			for tag1 in unique_tags.keys():
				if tag1!='q0':
					#print tag
					transition[tag+":"+tag1]=transition.get(tag+":"+tag1,0)+1
					#unique_tags[tag]=unique_tags.get(tag)+1
					special_tags[tag]=special_tags.get(tag)+1
			
					
		#print "special tags:",special_tags
		
		#print "--------------------------------------------------------------------"
		#print 				
		for key in transition.keys():
			#sum=0
			split=key.split(":")
			
			transition[key]=transition[key]/float(special_tags[split[0]])

		#print "UNique tags", unique_tags
		#print "sentences:",emission
		for key in emission.keys():
			#print emission[key
				#`AZprint key
				splitt=key[-2:]
				emission[key]=emission[key]/float(unique_tags[splitt])
			
		for tag in unique_words.keys():
			for tag1 in unique_tags.keys():
				if tag1!='q0':
					key=tag+":"+tag1
					emission[tag+":"+tag1]=emission.get(key,0)
						
				
		#print "_____________________________________________________________"
		#print "Emission probabilities",emission
		
		#print "unique tags:",unique_tags
		


		#print emission
		
		#print "---------------------------------------------------------------"
		
		#print transition
		#print transition
		f=open("hmmmodel.txt","w")
		
		em=str(emission)
		tr=str(transition)
		un=str(unique_tags)
		uw=str(unique_words)
		f.write(un+"\n"+tr+"\n"+em+"\n"+uw)
		



if __name__ == "__main__":
	f=open(sys.argv[1],'r')
	
	t=pre()
	t.preprocessing(f)
	
