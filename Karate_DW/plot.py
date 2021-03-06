from matplotlib import pyplot as plt
import numpy as np
import os
from sklearn.decomposition import PCA

#file_name='karate.embeddings'
file_name='output'

def get_embeddings(file_name):
	f=open(file_name)
	s=f.readlines()
	s=[x.strip() for x in s]
	s=[row.split(" ") for row in s]
	label=[]
	data,t=[],[]
	for row in s[1:]:
		label.append(int(row[0]))
		t=[]
		for element in row[1:]:
			t.append(float(element))
		data.append(t)
	print np.array(data).shape
	return label,np.array(data)

def get_map(labels):
	f=open('Karate_labels')
	f.next()
	ret={}
	for row in f:
		q =  map(int,row.strip().split(','))
		ret[q[0]+1]=q[1]
	return ret

def new_get_map():

	f=open('Karate_labels_1')
	f=f.readlines()
	clas={}
	for row in f:
	    temp=row.strip().split('-')
	    for x in map(int,temp[0].split(',')):
	        clas[x]=int(temp[1])

	return clas

def plot_output(file_name,count=None,image=None):
	label,data=get_embeddings(file_name)
	if data.shape[1]>2:
		pca=PCA(n_components=2)
		data=pca.fit_transform(data)
	print data.shape
	const_val=new_get_map()
	#c_dict={0:'r',1:'g',2:'b',3:'k'}
	c_dict={0:'+',1:'o',2:'*',3:'^'}
	done =[]
	for index in xrange(len(data)):
		val=const_val[label[index]]
		if val in done: 
			plt.scatter(data[index,0],data[index,1],marker=c_dict[val],s=100)
		else:
			done.append(val)
			plt.scatter(data[index,0],data[index,1],marker=c_dict[val],s=100,label=str(val))
	        plt.annotate('%s' %str(label[index]),(data[index,0],data[index,1]))
	plt.legend(loc='upper left')
	plt.show()

	"""
	#print target
	for index,val in enumerate(label):
		if index<=9476:  #positive
			c='r'
		else:           #negative
			c='b'
		plt.scatter(x[index],y[index],c=c)
		#print index,val,target[val]
	#image=image.ravel()
	figure=plt.figure()
	for index,val in enumerate(label):
		if image!=None:
			if image[val-1]==0:
				figure.scatter(x[index],y[index],c='b')
		else:
			plt.scatter(x[index],y[index],c='b')
		#plt.annotate('%s' %str(val),(x[index],y[index]))
	plt.show()
#if __name__=="__main__":
#plot_output(file_name)
"""
