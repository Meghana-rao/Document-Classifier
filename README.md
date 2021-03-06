## Document-Classifier
Liabraries needed include
pdf2image, PyPDF2, os, numpy, subprocess, csv, sklearn, cv2, tensorflow

## Files to download
retrained_graph.pb <br/>
retrained_labels.txt<br/>
count_ops.py<br/>
evaluate.py<br/>
graph_pb2tb.py
<p>__init__.py</p>
label_image.py<br/>
retrain.py<br/>
quantize_graph.py<br/>
show_image.py<br/>
net_tester.py<br/>

## To retrain the model
```
python scripts/retrain.py  --image_dir ./tf_files/train --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --how_many_training_steps=1000
```

Adjust the training steps accordingly.

## To test it on unlabelled data (single file)
```
python3 scripts/label_image.py --graph=tf_files/retrained_graph.pb --image=test.png
```
## To test it on labelled data and drawing statistics (should have a .csv file with labels and file name)
```
python3 tester.py
```
Adjust src_label, src_graph, folder_name, csv_file file locations

The tester.py returns the classification report and the confusion matrix.
