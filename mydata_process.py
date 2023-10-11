import json


def from_cmeiev2_2_train():
    wf = open("C:/Users/ZL/Desktop/json_out.json", "w", encoding='utf-8')
    with open("H:/CMeIE-V2/CMeIE-V2_train.jsonl", "r", encoding='utf-8') as rf:
        for line in rf.readlines():
            source = json.loads(line)
            output_str = ""
            spo_list = source['spo_list']
            relation_list = []

            for d in spo_list:
                subject_str = d['subject']
                object_str = d['object']['@value']
                predicate = d['predicate']
                if len(output_str) == 0:
                    relation = subject_str + "_" + predicate + "_" + object_str
                else:
                    relation = "\n" + subject_str + "_" + predicate + "_" + object_str
                output_str += relation

            data = {
                "instruction": "你现在是一个信息抽取模型，请你帮我抽取出关系内容为\"预防\", \"阶段\", \"就诊科室\", \"同义词\", \"辅助治疗\", \"化疗\", \"放射治疗\", \"实验室检查\", \"影像学检查\", \"手术治疗\", \"辅助检查\", \"组织学检查\", \"内窥镜检查\", \"筛查\", \"多发群体\", \"发病率\", \"发病年龄\", \"多发地区\", \"发病性别倾向\", \"死亡率\", \"多发季节\", \"传播途径\", \"并发症\", \"病理分型\", \"相关（导致）\", \"鉴别诊断\", \"相关（转化）\", \"相关（症状）\", \"临床表现\", \"治疗后症状\", \"侵及周围组织转移的症状\", \"病因\", \"高危因素\", \"风险评估因素\", \"病史\", \"遗传因素\", \"发病机制\", \"病理生理\", \"药物治疗\", \"发病部位\", \"转移部位\", \"外侵部位\", \"预后状况\", \"预后生存率\"的相关三元组，三元组内部用\"_\"连接，三元组之间用\\n分割。文本：",
                "input": source['text'],
                "output": output_str
            }
            wf.write(json.dumps(data, ensure_ascii=False) + "\n")



if __name__ == '__main__':
    from_cmeiev2_2_train()

