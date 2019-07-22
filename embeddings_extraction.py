import codecs
import glob
import sys
import shutil
import os
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
path_app = os.path.dirname(os.path.abspath(__file__))

if __name__=="__main__":
    prompt = ' <input_folder> <output_folder>'
    prompt += ' <layers / default:-1>'
    prompt += ' <bert_model_dir_>'
    prompt += ' <max_sequence_length (default 128)>'
    prompt += ' <batch_size (default 8)>'

    if (len(sys.argv) == 7):
        doc_list = sys.argv[1]
        docs=0
        if os.path.isdir(doc_list):
            print('document folder OK')
            for x in os.listdir(sys.argv[1]):
                docs+=1
            if (docs == 0):
                print('empty folder')
                sys.exit()
            else:
                print('# of docs : ', docs)
                docs = 0
        else:
            print('folder does not exist')
            sys.exit()

        output_txt = sys.argv[2]
        if os.path.isdir(output_txt):
            for x in os.listdir(output_txt):
                docs+=1
            if (docs == 0):
                print('output folder OK')
            else:
                print('WARNING, Folder is not empty, there are : ', docs,' items')
                docs = 0
        else :
            print('folder does not exist, creating folder inside the location of documents')
            os.mkdir(sys.argv[1]+'output_embeddings/')
            sys.exit()

        bert_dir = sys.argv[4]
        bert_dir = bert_dir[:-1]
        if os.path.isdir(bert_dir):
            print('model folder OK')
        else:
            print('could not find model folder')
            sys.exit()

        try:
            layers = sys.argv[3]
            layerstest = list(map(int,sys.argv[3].split(',')))
            print(layers)
            print('number of layers OK')
            del layerstest
        except ValueError:
            print('invalid argument in layers')
            sys.exit()

        try:
            max_seq_length = sys.argv[5]
            layerstest = int(sys.argv[5])
            print('max sequence length OK : ',max_seq_length)
            del layerstest
        except ValueError:
            print('invalid arg in max sequence length')
            sys.exit()

        try:
            batch_size = sys.argv[6]
            layerstest = int(sys.argv[6])
            print('batch size OK : ',batch_size)
            del layerstest
        except ValueError:
            print('invalid arg in batch size')
            sys.exit()
        
        ###  Create temp directory
        dirName = 'temp'
        try:
            os.mkdir(dirName)
            print("temporal directory created successfully") 
        except FileExistsError:
            print("Directory " , dirName ,  " already exists")
        ### SET STOPWORD LIST AND  ENGLISH TOKENIZER
        stop_words = set(stopwords.words('english'))
        sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        for text in os.listdir(doc_list):
            print("Reading '{0}'...".format(text))
            with codecs.open(doc_list + text, "r", "utf-8") as txt:
                buffer = (txt.read().lower()) # MODEL REQUIRES LOWER CASE LETTERS
                word_tokens = sentence_tokenizer.tokenize(buffer) # TOKENIZE EACH DOC
                filtered_buffer = []
                # REMOVE STOPWORDS
                for w in word_tokens: 
                    if w not in stop_words: 
                        filtered_buffer.append(w)
                with open(path_app+'/'+dirName+'/'+ text,"w") as temp_file:
                    for i in filtered_buffer:
                        temp_file.write(i+os.linesep)
        print('Reading OK')

        BERT_BASE_DIR = bert_dir

        for item in os.listdir(path_app+'/'+dirName+'/'):
            item = item.replace('.txt','')
            os.system('python '+path_app+'/'+'bert-master'+'/'+'extract_features.py \
            --input_file='+path_app+'/'+dirName+'/'+item+'.txt'+' \
            --output_file='+output_txt+item+'.json1'+' \
            --vocab_file='+BERT_BASE_DIR+'/vocab.txt \
            --bert_config_file='+BERT_BASE_DIR+'/bert_config.json \
            --init_checkpoint='+BERT_BASE_DIR+'/bert_model.ckpt \
            --layers='+layers+' \
            --max_seq_length='+max_seq_length+' \
            --batch_size='+batch_size)
        shutil.rmtree(path_app+'/'+dirName)
    else:
        print('invalid number of arguments, please use the following template:')
        print('python '+sys.argv[0]+prompt)
        sys.exit()
