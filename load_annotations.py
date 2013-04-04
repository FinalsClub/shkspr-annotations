import json
import sys

import annotateit
from annotateit import model

app = annotateit.create_app()
app.test_request_context().push()

annotations = json.load(sys.stdin)

for annotation in annotations:
    annotation['finalsclub_id'] = annotation.pop('id')
    annotation['permissions'] = {'read': ['group:__world__']}
    annotation['ranges'] = [annotation['ranges']]
    ann = model.Annotation()
    ann.update(annotation)
    ann.save()
