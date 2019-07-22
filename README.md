# BERT word-embeddings automatic extraction tool

This repository was created in order to perform the automatic word-embedding extraction task from any of the existing BERT pre-trained models.

# Instructions
1. Download the BERT repository: https://github.com/google-research/bert
2. Download any of the existing pre-trained models,
    the links to the models are here (right-click, 'Save link as...' on the name):

    *   **[`BERT-Large, Uncased (Whole Word Masking)`](https://storage.googleapis.com/bert_models/2019_05_30/wwm_uncased_L-24_H-1024_A-16.zip)**:
        24-layer, 1024-hidden, 16-heads, 340M parameters
    *   **[`BERT-Large, Cased (Whole Word Masking)`](https://storage.googleapis.com/bert_models/2019_05_30/wwm_cased_L-24_H-1024_A-16.zip)**:
        24-layer, 1024-hidden, 16-heads, 340M parameters
    *   **[`BERT-Base, Uncased`](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip)**:
        12-layer, 768-hidden, 12-heads, 110M parameters
    *   **[`BERT-Large, Uncased`](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-24_H-1024_A-16.zip)**:
        24-layer, 1024-hidden, 16-heads, 340M parameters
    *   **[`BERT-Base, Cased`](https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip)**:
        12-layer, 768-hidden, 12-heads , 110M parameters
    *   **[`BERT-Large, Cased`](https://storage.googleapis.com/bert_models/2018_10_18/cased_L-24_H-1024_A-16.zip)**:
        24-layer, 1024-hidden, 16-heads, 340M parameters
    *   **[`BERT-Base, Multilingual Cased (New, recommended)`](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip)**:
        104 languages, 12-layer, 768-hidden, 12-heads, 110M parameters
    *   **[`BERT-Base, Multilingual Uncased (Orig, not recommended)`](https://storage.googleapis.com/bert_models/2018_11_03/multilingual_L-12_H-768_A-12.zip)
        (Not recommended, use `Multilingual Cased` instead)**: 102 languages,
        12-layer, 768-hidden, 12-heads, 110M parameters
    *   **[`BERT-Base, Chinese`](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)**:
        Chinese Simplified and Traditional, 12-layer, 768-hidden, 12-heads, 110M
        parameters
        
3. Decompress the model, and download `embeddings_extraction.py`

4. The directory should look like this:

```
bert-master
embeddings_extraction.py 
your_model_folder

````
5. Execute `embeddings_extraction.py`, the input parameters need to be in the order shown below:

````
python embeddings_extraction.py <input_folder> <output_folder> <layers> <bert_model_dir_> <max_sequence_length> <batch_size>
````

Example:

````
python embeddings_extraction.py  /home/sebastian/Documents/txtfolder/ /home/sebastian/Documents/outputfolder/ -1,-2 /home/sebastian/Documents/BERT_Embeddings/uncased12/ 128 8
````


6. All extracted files are in JSON format. With one line per line of input containing the BERT activations from each Transformer layer specified in layers (-1 is the final hidden layer of the Transformer, etc.)

# Notes:
* Layers are expressed with negative index
* The bert folder shall remain with its original name
* max_seq_lenght's default value is 128, it has to be present anyway
* batch_size is 8 as default





# References

[BERT paper](https://arxiv.org/abs/1810.04805)

[BERT repository](https://github.com/google-research/bert)
