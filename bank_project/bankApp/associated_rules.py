import json
import apyori
from apyori import apriori
import io


def recommendation_items(transactions_list, service_client):
    #результат алгоритма apriori()
    rules = list(apriori(transactions_list, min_support=0.004, min_confidence=0.2, min_lift=5, min_length=2,
                         max_length=3))
    results = list(rules)
    output = []
    for RelationRecord in results:
        o = io.StringIO()
        apyori.dump_as_json(RelationRecord, o)
        output.append(json.loads(o.getvalue()))
    rules_with_input = []
    for record in output:  # собираем наборы в которых есть выбранная услуга
        if service_client in record['items']:
            rules_with_input.append(record)
    max_lift_list = []
    confidence_list = []
    for record in rules_with_input:
        max_lift = 0
        confidence = 0
        for order_stat in record['ordered_statistics']:
            if order_stat['lift'] > max_lift:
                max_lift = order_stat['lift']
                confidence = order_stat['confidence']
        max_lift_list.append(max_lift)
        confidence_list.append(confidence)
    result_items = []
    indexes = [i for i in range(len(max_lift_list)) if max_lift_list[i] == max(max_lift_list)]
    for i in indexes:
        item_dict = {
            'items': rules_with_input[i]['items'],
            'confidence': int(confidence_list[i] * 100),
            'support': int(rules_with_input[i]['support'] * 100),
            'lift': int(max_lift_list[i])
        }
        result_items.append(item_dict)
    for item in result_items:
        item['items'].remove(service_client)
    return result_items
