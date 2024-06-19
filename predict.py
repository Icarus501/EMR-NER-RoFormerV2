#  -*-coding:utf8 -*-
import os
import pickle

from model import BERT
from path import BASE_CONFIG_NAME, BASE_CKPT_NAME, BASE_MODEL_DIR, label_dict_path, weights_path
from preprocess import NamedEntityRecognizer
from utils.tokenizers import Tokenizer

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from utils.backend import K

# bert配置
config_path = BASE_CONFIG_NAME
checkpoint_path = BASE_CKPT_NAME
dict_path = '{}/vocab.txt'.format(BASE_MODEL_DIR)


def predict(txt, weights_path, label_dict_path, trans_path):
    with open(label_dict_path, 'rb') as f:  # 打开文件
        categories = pickle.load(f)
    
    # 建立分词器
    
    tokenizer = Tokenizer(dict_path, do_lower_case = True)
    
    bert = BERT(config_path,
                checkpoint_path,
                categories,
                summary = False)
    model = bert.get_model()
    model.load_weights(weights_path)
    # CRF = bert.get_CRF()
    NER = NamedEntityRecognizer(tokenizer, model, categories, trans = pickle.load(open(trans_path, 'rb')), starts = [0],
                                ends = [0])
    NER.trans = pickle.load(open(trans_path, 'rb'))
    entities = []
    for start, end, tag in set(NER.recognize(txt)):
        entities.append((txt[start:end + 1], tag, start, end))
    return sorted(entities, key = lambda d: d[2])


if __name__ == '__main__':
    # segment_ids后长于512的部分将被截断，无法预测
    txt="左侧乳腺术后改变。右侧颈部Ⅳ区、左侧颈部Ⅴ区、右侧腋窝、纵隔内气管旁、右颈总动脉旁、血管前间隙、左侧后胸壁肩胛上肌深面多发大小不等淋巴结，不同程度代谢增高，SUVmax为6.9，考虑肿瘤下述淋巴结转移；②两侧斜裂胸膜及左侧水平裂胸膜及胸膜上区多个小结节、中下肺野肺内多个小结节，未见代谢增高，考虑肿瘤胸膜及肺内转移可能性大，请结合临床随诊"
    for i in predict(txt = txt,
                     weights_path = weights_path + '/yidu_roformer_v2_base.h5',
                     label_dict_path = label_dict_path,
                     trans_path = "./weights/yidu_roformer_v2_crf_trans.pkl"):
        print(i)
