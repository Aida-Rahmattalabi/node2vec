import networkx	as nx
import pandas as pd




file = open('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/emb/genomic_full.txt')
#file = open('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/emb/genomic_subset.txt')

embeddings = []
i = 0
for line in file:
	if(i == 0):
		print(line)

	line = line.strip()
	line = line.split(' ')
	line = [float(i) for i in line]

	if(i >= 1):
		line[0] = int(line[0])
		embeddings.append(line)
	i += 1 


df = pd.DataFrame(embeddings, columns = ['source', 'f1', 'f2'])
 
print(embeddings, len(embeddings))
print(df)

#df.to_csv('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/emb/genomic_subset.csv', index = False)
df.to_csv('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/emb/genomic_full.csv', index = False)


# df = pd.read_csv('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/graph/node_pair.csv')


# df_subset = df[df['weight'] < 0.00001]

# # create fully-connected weigthed genomic graph
# Graphtype = nx.Graph()
# g = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)
# g = nx.convert_node_labels_to_integers(g, first_label=0, ordering='default', label_attribute=None)

# nx.write_edgelist(g, "/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/graph/genomic_full.edgelist")


# # create weight-truncated genomic graph
# Graphtype = nx.Graph()
# g_subset = nx.from_pandas_edgelist(df_subset, edge_attr='weight', create_using=Graphtype)
# g_subset = nx.convert_node_labels_to_integers(g_subset, first_label=0, ordering='default', label_attribute=None)

# nx.write_edgelist(g_subset, "/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/graph/genomic_subset.edgelist")



