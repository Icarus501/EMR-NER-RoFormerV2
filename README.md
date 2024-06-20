# Medical Entity Recognition and Knowledge Map Relationship Analysis of Chinese EMRs Based on Improved BiLSTM-CRF

## Dataset

The CCKS dataset is designed for the task of recognizing and extracting clinical entities from a given set of electronic medical record (EMR) text documents. The goal is to identify and categorize these entity mentions into predefined categories, such as diseases, treatments, and examinations.

1. **Diseases and Diagnoses:** Medically defined diseases and clinical judgments made by physicians regarding etiology, pathophysiology, classification, and staging.

2. **Examinations:** Imaging examinations (X-ray, CT, MR, PETCT, etc.), angiography, ultrasound, and electrocardiograms. To avoid overlap with surgical operations, other diagnostic procedures like gastroscopy and colonoscopy are not included.

3. **Tests:** Physical or chemical examinations conducted in a laboratory. Specifically, this refers to clinical laboratory tests conducted by the laboratory department, excluding immunohistochemistry and other broad laboratory tests.

4. **Surgeries:** Procedures involving the removal or suturing of body parts by physicians as a primary method of surgical treatment.

5. **Medications:** Specific chemical substances used for disease treatment.

6. **Anatomical Sites:** The anatomical locations in the human body where diseases, symptoms, and signs occur.

Each line of data in Task 1 is a JSON object. The JSON keys are `[originalText', 'entities']`, representing the original text and the list of entities.

The json`["entities"]` is a list where each element represents an entity. Each entity includes:

The training data has been preprossed into forms as below:

```
心	B-TESTIMAGE
脏	I-TESTIMAGE
彩	I-TESTIMAGE
超	I-TESTIMAGE
：	O
右	B-ANATOMY
房	I-ANATOMY
、	O
右	B-ANATOMY
室	I-ANATOMY
稍	O
增	O
大	O
，	O
E	B-TESTLAB
F	I-TESTLAB
正	O
常	O
。	O
```

ATTENTION:

- Use a tab character ("\t") to separate words and labels.
- Use a blank line to separate sentences.
- End the file with two newline characters.

You can run statistic.py to view information about sentence length and quantity.


## Requirements


- Keras==2.2.4

- matplotlib==3.4.0

- pandas==1.2.3

- tensorflow==1.14.0

- tqdm==4.61.2


## Steps


1. Replace the dataset.
2. Modify the addresses in path.py.
3. Delete the old `weights/{}_catagory.pkl` category set file.
4. Adjust the model structure in `model.py` as needed.
5. Update parameters in config.py.
6. Debug.
7. Train the model.

## Model

The model integrates RoFormerV2 with BiLSTM-CRF to enhance medical entity recognition and knowledge map relationship analysis in Chinese electronic medical records (EMRs). RoFormerV2, a transformer-based model, enhancing speed through structural simplification and improves effectiveness by combining unsupervised pre-training with supervised pre-training, while BiLSTM-CRF provides sequence labeling capabilities for precise entity extraction. This fusion leverages the strengths of both models, improving the accuracy and efficiency of the task. The overall framework ensures comprehensive processing from input to output, facilitating better understanding and application in clinical contexts.

## Configurations

- **maxlen**: The maximum length of a single sentence in each batch during training. Sentences shorter than this length will be padded, and sentences longer will be truncated.
- **epochs**: The maximum number of training epochs.
- **batch_size**: The size of each batch.
- **bert_layers**: The number of BERT layers. 
- **crf_lr_multiplier**: The learning rate multiplier for the CRF layer. 
- **model_type**: The model type, e.g., 'roformer_v2'.
- **dropout_rate**: The dropout rate.
- **max_lr**: The maximum learning rate. The higher the number of bert_layers, the lower this should be. For small models, it's recommended to use between 5e-5 to 1e-4, and for base models, between 1e-5 to 5e-5.
- **lstm_hidden_units**: The number of hidden units in the LSTM.


## Project Structure

```
./
├── README.md
├── __pycache__
├── chinese_roformer-v2-char_L-12_H-768_A-12    RoFormer_v2 base weight file
├── chinese_roformer-v2-char_L-6_H-384_A-6      RoFormer_v2 small weight file
├── config.py                                   Model hyperparameters that may need adjustment
├── data                                        Dataset folder
│   ├── yidu.test                               Officially provided 379 test samples
│   ├── yidu.train                              Training set split from the official 1000 training samples
│   ├── yidu.validate                           Validation set split from the official 1000 training samples
│   └── yidu_catagory.pkl                       Category set, generated by train.py, used in predict.py
├── evaluate.py
├── images                                      Images generated from training and evaluation data
├── log                                         Training log, generated by train.py
├── model.py                                    Model construction
├── path.py                                     All paths
├── predict.py                                  Model prediction output
├── preprocess.py                               Data preprocessing
├── statistic.py                                Statistics on sentence length and quantity, used to adjust and set maxlen
├── report                                      Evaluation report, generated by evaluate.py
│   └── yidu_bert_base.csv                      Precision, recall, F1 for each category
├── train.py                                    Training file
├── requirements.txt                            pip environments
├── plot.py                                     Plotting tool
├── utils                                       bert4keras toolkit, also available via pip
└── weights                                     Saved weights
    ├── yidu_catagory.pkl                       Entity categories
    ├── yidu_roformer_v2_base.h5                Model weights
    └── yidu_roformer_v2_crf_trans.pkl          Best model weights
```
