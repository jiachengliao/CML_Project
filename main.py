from data_processing.batch import batch_all_images

target = "sheep"
working_dir = "/Users/Kun/Desktop/Project_CML/sample/"
input_image_path = working_dir + "JPEGImages/"
annotation_path = working_dir + "Annotations/"
output_parent_path = "%soutput/%s/" % (working_dir, target)
target_pos_path = working_dir + "ImageSets/Main/"
unit_ratio_list = [0.2, 0.3 , 0.4, 0.5, 0.6, 0.7, 0.8]
overlap_ratio = 0.1
target_count = 5
k = 3
max_iter = 10
voca_path = output_parent_path + "vocabulary.txt"
dataset_mode = True
overlap_threshold = 0.5
preVLAD = True

batch_all_images(input_image_path, annotation_path, output_parent_path,
            unit_ratio_list, overlap_ratio, target,
            target_pos_path, target_count=target_count, k=k, max_iter=max_iter, preVLAD=preVLAD,
            voca_path=voca_path, dataset_mode=dataset_mode, overlap_threshold=overlap_threshold)
