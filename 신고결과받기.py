from collections import defaultdict

def solution(id_list, report, k):
    warnings=defaultdict(set)
    # warnings=dict().fromkeys(id_list,set())
    answer_dict=dict().fromkeys(id_list,0)

    for warning in report:
        accuser,accused=warning.split(' ')
        warnings[accused].add(accuser)

    for accused in warnings:
        if len(warnings[accused])>=k:
            for accuser in warnings[accused]:
                answer_dict[accuser]+=1

    return list(answer_dict.values())
