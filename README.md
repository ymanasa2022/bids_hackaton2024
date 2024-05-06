The goal is to see if the phenotypic groups match groups identified from transcriptomic data.

 

Download the prostate cancer samples data from TCGA using the TCGAbiolinks or TCGA2STAT packages in R or the python packages gdc-client or pytcga.  

Download the meta data for the prostate cancer samples and chack if they have grade/subtype/PSA level (look up commonly used thresholds) information and create meta data that contains the group information for these samples.

The result will be either read count or gene/transcript expression level (FPKM, TPM …)  for each prostate cancer sample and associated group meta data.

If you have read counts – normalize them to compute a metric for the gene/transcript expression level.

Apply a clustering technique (k-means, hierarchical clustering, or any other type of unsupervised learning) to identify subtypes.

Used the group labels to compute the accuracy for your clustering.

You can also use any type of evaluation metric for the clustering.

 

Alternative analysis:    

Goal: Build a model that we can use on transcriptomic data from a new prostate cancer patient to identify the subtype.

 

If there is enough data for all groups, you could split the data in two (training, testing), do supervised machine learning on the training data to build a model to distinguish between the subgroups that the meta data provided.

The testing data will be used to evaluate the model and metrics like accuracy can be computed.


The scikit-learn python package can be used to apply the machine learning approach on the data.

https://scikit-learn.org/stable/unsupervised_learning.html

https://scikit-learn.org/stable/supervised_learning.html

In R there are packages like: mclust, cluster, caret, e1071, randomForest, and many others.
