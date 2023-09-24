{'version': '3.44.4', 'mode': 'interface', 'app_id': 1839905737797421627, 'dev_mode': False, 'analytics_enabled': True, 'components': [{'id': 8, 'type': 'row', 'props': {'variant': 'default', 'visible': True, 'equal_height': False, 'name': 'row'}}, {'id': 9, 'type': 'column', 'props': {'scale': 1, 'min_width': 320, 'variant': 'panel', 'visible': True, 'name': 'column'}}, {'id': 10, 'type': 'column', 'props': {'scale': 1, 'min_width': 320, 'variant': 'default', 'visible': True, 'name': 'column'}}, {'id': 0, 'type': 'dropdown', 'props': {'choices': [('first', 'first'), ('second', 'second'), ('third', 'third')], 'type': 'index', 'allow_custom_value': False, 'filterable': True, 'label': 'passenger_class', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'name': 'dropdown', 'server_fns': ['ls'], 'selectable': False}, 'serializer': 'SimpleSerializable', 'api_info': {'info': {'type': 'string', 'description': "Option from: [('first', 'first'), ('second', 'second'), ('third', 'third')]"}, 'serialized_info': False}, 'example_inputs': {'raw': ('first', 'first'), 'serialized': ('first', 'first')}}, {'id': 6, 'type': 'checkbox', 'props': {'value': False, 'label': 'is_male', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'name': 'checkbox', 'server_fns': ['ls'], 'selectable': False}, 'serializer': 'BooleanSerializable', 'api_info': {'info': {'type': 'boolean'}, 'serialized_info': False}, 'example_inputs': {'raw': True, 'serialized': True}}, {'id': 1, 'type': 'slider', 'props': {'minimum': 0, 'maximum': 80, 'value': 25, 'step': 0.1, 'label': 'age', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'name': 'slider', 'server_fns': ['ls']}, 'serializer': 'NumberSerializable', 'api_info': {'info': {'type': 'number', 'description': 'numeric value between 0 and 80'}, 'serialized_info': False}, 'example_inputs': {'raw': 0, 'serialized': 0}}, {'id': 2, 'type': 'checkboxgroup', 'props': {'choices': [('Sibling', 'Sibling'), ('Child', 'Child')], 'value': [], 'type': 'value', 'label': 'Travelling with (select all)', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'name': 'checkboxgroup', 'server_fns': ['ls'], 'selectable': False}, 'serializer': 'ListStringSerializable', 'api_info': {'info': {'type': 'array', 'items': {'type': 'string'}}, 'serialized_info': False}, 'example_inputs': {'raw': ['Sibling'], 'serialized': ['Sibling']}}, {'id': 3, 'type': 'number', 'props': {'value': 20.0, 'label': 'fare', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'step': 1, 'name': 'number', 'server_fns': ['ls']}, 'serializer': 'NumberSerializable', 'api_info': {'info': {'type': 'number'}, 'serialized_info': False}, 'example_inputs': {'raw': 5, 'serialized': 5}}, {'id': 4, 'type': 'radio', 'props': {'choices': [('S', 'S'), ('C', 'C'), ('Q', 'Q')], 'type': 'index', 'label': 'embark_point', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'name': 'radio', 'server_fns': ['ls'], 'selectable': False}, 'serializer': 'StringSerializable', 'api_info': {'info': {'type': 'string'}, 'serialized_info': False}, 'example_inputs': {'raw': 'S', 'serialized': 'S'}}, {'id': 11, 'type': 'form', 'props': {'scale': 0, 'min_width': 0, 'name': 'form'}}, {'id': 12, 'type': 'row', 'props': {'variant': 'default', 'visible': True, 'equal_height': True, 'name': 'row'}}, {'id': 13, 'type': 'button', 'props': {'value': 'Clear', 'variant': 'secondary', 'visible': True, 'interactive': True, 'name': 'button', 'server_fns': ['ls']}, 'serializer': 'StringSerializable', 'api_info': {'info': {'type': 'string'}, 'serialized_info': False}, 'example_inputs': {'raw': 'Howdy!', 'serialized': 'Howdy!'}}, {'id': 14, 'type': 'column', 'props': {'scale': 1, 'min_width': 320, 'variant': 'panel', 'visible': True, 'name': 'column'}}, {'id': 7, 'type': 'label', 'props': {'value': {}, 'label': 'output', 'show_label': True, 'container': True, 'min_width': 160, 'visible': True, 'name': 'label', 'server_fns': ['ls'], 'selectable': False}, 'serializer': 'JSONSerializable', 'api_info': {'info': {'type': {}, 'description': 'any valid json'}, 'serialized_info': True}, 'example_inputs': {'raw': {'a': 1, 'b': 2}, 'serialized': None}}, {'id': 15, 'type': 'row', 'props': {'variant': 'default', 'visible': True, 'equal_height': True, 'name': 'row'}}, {'id': 16, 'type': 'button', 'props': {'value': 'Flag', 'variant': 'secondary', 'visible': True, 'interactive': True, 'name': 'button', 'server_fns': ['ls']}, 'serializer': 'StringSerializable', 'api_info': {'info': {'type': 'string'}, 'serialized_info': False}, 'example_inputs': {'raw': 'Howdy!', 'serialized': 'Howdy!'}}, {'id': 17, 'type': 'dataset', 'props': {'samples': [['first', True, 30, [], 50, 'S'], ['second', False, 40, ['Sibling', 'Child'], 10, 'Q'], ['third', True, 30, ['Child'], 20, 'S']], 'headers': ['passenger_class', 'is_male', 'age', 'Travelling with (select all)', 'fare', 'embark_point'], 'type': 'index', 'samples_per_page': 10, 'visible': True, 'container': True, 'min_width': 160, 'name': 'dataset', 'server_fns': ['ls'], 'selectable': False, 'components': ['dropdown', 'checkbox', 'slider', 'checkboxgroup', 'number', 'radio']}, 'serializer': 'StringSerializable', 'api_info': {'info': {'type': 'string'}, 'serialized_info': False}, 'example_inputs': {'raw': 'Howdy!', 'serialized': 'Howdy!'}}], 'css': None, 'title': 'Gradio', 'space_id': None, 'enable_queue': False, 'show_error': False, 'show_api': True, 'is_colab': False, 'stylesheets': ['https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600&display=swap', 'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap'], 'theme': 'default', 'layout': {'id': 5, 'children': [{'id': 8, 'children': [{'id': 9, 'children': [{'id': 10, 'children': [{'id': 11, 'children': [{'id': 0}, {'id': 6}, {'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]}]}, {'id': 12, 'children': [{'id': 13}]}]}, {'id': 14, 'children': [{'id': 7}, {'id': 15, 'children': [{'id': 16}]}]}]}, {'id': 17}]}, 'dependencies': [{'targets': [0], 'trigger': 'change', 'inputs': [0, 6, 1, 2, 3, 4], 'outputs': [7], 'backend_fn': True, 'js': None, 'queue': None, 'api_name': 'predict', 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [6], 'trigger': 'change', 'inputs': [0, 6, 1, 2, 3, 4], 'outputs': [7], 'backend_fn': True, 'js': None, 'queue': None, 'api_name': 'predict_1', 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [1], 'trigger': 'change', 'inputs': [0, 6, 1, 2, 3, 4], 'outputs': [7], 'backend_fn': True, 'js': None, 'queue': None, 'api_name': 'predict_2', 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [2], 'trigger': 'change', 'inputs': [0, 6, 1, 2, 3, 4], 'outputs': [7], 'backend_fn': True, 'js': None, 'queue': None, 'api_name': 'predict_3', 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [3], 'trigger': 'change', 'inputs': [0, 6, 1, 2, 3, 4], 'outputs': [7], 'backend_fn': True, 'js': None, 'queue': None, 'api_name': 'predict_4', 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [4], 'trigger': 'change', 'inputs': [0, 6, 1, 2, 3, 4], 'outputs': [7], 'backend_fn': True, 'js': None, 'queue': None, 'api_name': 'predict_5', 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [13], 'trigger': 'click', 'inputs': [], 'outputs': [0, 6, 1, 2, 3, 4, 7], 'backend_fn': False, 'js': '() => [null, null, 0, [], null, null, {}]', 'queue': False, 'api_name': None, 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [13], 'trigger': 'click', 'inputs': [], 'outputs': [10], 'backend_fn': False, 'js': '() => [{"variant": null, "visible": true, "__type__": "update"}]\n            ', 'queue': False, 'api_name': None, 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [16], 'trigger': 'click', 'inputs': [], 'outputs': [16], 'backend_fn': True, 'js': None, 'queue': False, 'api_name': None, 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [16], 'trigger': 'click', 'inputs': [0, 6, 1, 2, 3, 4, 7], 'outputs': [16], 'backend_fn': True, 'js': None, 'queue': False, 'api_name': None, 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [13], 'trigger': 'click', 'inputs': [], 'outputs': [16], 'backend_fn': True, 'js': None, 'queue': False, 'api_name': None, 'scroll_to_output': False, 'show_progress': 'full', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}, {'targets': [17], 'trigger': 'click', 'inputs': [17], 'outputs': [0, 6, 1, 2, 3, 4], 'backend_fn': True, 'js': None, 'queue': False, 'api_name': False, 'scroll_to_output': False, 'show_progress': 'hidden', 'every': None, 'batch': False, 'max_batch_size': 4, 'cancels': [], 'types': {'continuous': False, 'generator': False}, 'collects_event_data': False, 'trigger_after': None, 'trigger_only_on_success': False}], 'root': ''}