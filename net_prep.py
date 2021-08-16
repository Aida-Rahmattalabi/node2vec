import networkx	as nx
import pandas as pd




# file = open('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/emb/karate_1.txt')

# i = 0
# for line in file:

# 	line = line.strip()
# 	line = line.split(' ')
# 	line = [float(i) for i in line]
# 	print(i , line)
# 	i += 1 


df = pd.read_csv('/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/graph/node_pair.csv')


df_subset = df[df['weight'] < 0.0001]
print(df_subset)
# create fully-connected weigthed genomic graph
Graphtype = nx.Graph()
g = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)
#g = nx.convert_node_labels_to_integers(g, first_label=0, ordering='default', label_attribute=None)
print(nx.get_edge_attributes(g,'weight'))

nx.write_edgelist(g, "/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/graph/genomic_full.edgelist")


# create weight-truncated genomic graph
Graphtype = nx.Graph()
g_subset = nx.from_pandas_edgelist(df_subset, edge_attr='weight', create_using=Graphtype)
#g_subset = nx.convert_node_labels_to_integers(g_subset, first_label=0, ordering='default', label_attribute=None)

nx.write_edgelist(g_subset, "/Users/aida/Dropbox/PhD/Internship/RegLab/COVID-Outbreak/node2vec/graph/genomic_subset.edgelist")



