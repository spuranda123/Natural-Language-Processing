import sys
import operator

import math


class decode:
	def model(self,file,unique_tags,transition,emission,unique_words):
		infi=float("inf")
		f12=open("hmmoutput.txt","w")
		#print "HI"
		#file2=open("output.txt","w")
		#print "here:",unique_tags
		#print transition
		#print emission

		#data=file.read()
		read1=file.read().rstrip("\n")
		data=read1.split("\n")
		#print data
		sent_obj=[]
		for sentence in data:
			#print sentence
			#sentence=sentence
			sent=[]
			words=sentence.split(" ")
			#sent.append(words)
			sent_obj.append(words)
		#print "this :",sent_obj	
		backpointers={}
		prob={}
		for i in range(0,len(sent_obj)):
			#k='qo'
			#print transition[k]
			max=-infi
			state_no=0
			for key in unique_tags.keys():
				
				
				#print sent_obj[i][0]
				if key!='q0':
					#print "keys:",emission.get(sent_obj[i][0]+":"+key)
					check=emission.get(sent_obj[i][0]+":"+key,1)
					if check==0:
						#print "if 0"
						probability=-infi
						#probability=math.log(float(transition['q0'+":"+key]),10)
					else:
					#print transition['q0'+":"+key]
						#print emission.get(sent_obj[i][0]+":"+key,1)
						#print "else 1"
						probability=math.log(transition['q0'+":"+key])+math.log(check)
					backpointers[str(key+str(state_no))]='q0'
					prob[str(key+str(state_no))]=probability
					#print probability
			#print "here:",backpointers

			
			state_no=1
			for j in range(1,len(sent_obj[i])):
				
				for tag in unique_tags.keys():
					
					if tag!='q0':
						max=-infi
						state=''
						#print "tag is:",tag
						for tag1 in unique_tags.keys():
							if tag1!='q0':
								check=emission.get(sent_obj[i][j]+":"+tag,1)
								if check!=0:
								#print tag1#probability=1
									#print "trying:",prob[str(tag1+str(state_no-1))]
									#print "again:",transition[tag1+":"+tag]
									#print "woho:",math.log(check)
									probability=math.log(transition[tag1+":"+tag])+prob[str(tag1+str(state_no-1))]+math.log(check)
									#print "if:",probability
								else:
									#print math.log(float(transition[tag1+":"+tag]),10)
									add=-infi
									probability=math.log(transition[tag1+":"+tag])+prob[str(tag1+str(state_no-1))]+add
									#print "else",probability
								#print "P:",probability
								if (probability>max):
							
									max=probability
									#print "max:",max
									state=tag1
										#print "state:",tag1
						prob[str(tag+str(state_no))]=max
						backpointers[str(tag+str(state_no))]=state
					#state_no=state_no+1
				#print prob
				#print backpointers
			#print prob
				#print backpointers
				state_no +=1
				

			max=-infi
			max_state=''
			for tag in unique_tags.keys():
				if tag!='q0':
					#print "state",state_no-1
					#print "sent",len(sent_obj[i])-1
					probability=prob[str(tag+str(state_no-1))]
					#print probability
					if max<probability and probability!=-infi:
						max=probability
						max_state=tag
						#print max_state
			final=max_state
			
			#print final
			#i=0
			tags=[]
			tags.append(final)
			for h in range(len(sent_obj[i])-1,-1,-1):
				final=backpointers[final+str(h)]
				#print final
				#max_state=sent_obj[i][h]+"/"+final
				#print max_state,
				if final!='q0':
					tags.append(final)
			#print tags
			b=0
			for h in range(len(tags)-1,-1,-1):
				
				if b<len(sent_obj[i]):
					#print sent_obj[i][b]+"/"+tags[h]+" ",
					f12.write(sent_obj[i][b]+"/"+tags[h]+" ")
				b=b+1
			f12.write("\n")
f=open("hmmmodel.txt","r")
line=f.readlines()
unique_tags=eval(line[0])
transition=eval(line[1])
emission=eval(line[2])
unique_words=eval(line[3])
	#print "Hi"
d=decode()
f1=open(sys.argv[1],"r")
d.model(f1,unique_tags,transition,emission,unique_words)
print "done"
