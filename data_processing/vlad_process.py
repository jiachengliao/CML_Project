from scipy.cluster.vq import vq, kmeans
from numpy import zeros, subtract, add, ndarray, savetxt, asarray, append
from utility import read_feature_vector, list_all_files
# from kmeans.kmeans import mykmeans_plus

def learn_vocabulary(input_path, k, max_iter, single_file):
    if single_file:
        vector_matrix = read_feature_vector(input_path)
    else:
        file_names = list_all_files(input_path)
        vector_matrix = read_feature_vector(input_path + file_names[0])
        for f in xrange(1, len(file_names)):
            vector = read_feature_vector(input_path + file_names[f])
            if vector is not None:
                vector_matrix = append(vector_matrix, vector, axis=0)
    # return mykmeans_plus(data=vector_matrix,k=k, max_iter=max_iter)[0]
    return kmeans(obs=vector_matrix, k_or_guess=k, iter=max_iter)[0]
     
def vlad_vector(vector_path, vocabulary):
    features = read_feature_vector(vector_path)
    codes = vq(features, vocabulary)[0]
    vlad = zeros(vocabulary.shape)
    for idx in range(codes.size):
        diff = subtract(features[idx], vocabulary[codes[idx]])
        vlad[codes[idx]] = add(diff, vlad[codes[idx]])
    return ndarray.flatten(vlad)
    
def vlad_vector_batch(input_path, output_path, vocabulary):
    vladL = []
    file_names = list_all_files(input_path)
    for f in file_names:
        vec = vlad_vector(vector_path=input_path + f, vocabulary=vocabulary)
        vladL.append(vec)
    output_path = output_path + '_vlad.txt'
    savetxt(output_path, asarray(vladL), delimiter=",", fmt='%.4f')