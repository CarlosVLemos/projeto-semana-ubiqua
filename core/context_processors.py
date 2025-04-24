from urllib import request

from django.urls import reverse


def menu_items(request):
    items = [
        {
            "label": "Menu Principal",
            "url_name": "bi:index",
            "icon": "bx bx-home-circle",
            "section": "Início",
            "header": True,
        },
        {
            "label": "Reciclagem",
            "icon": "bx bx-recycle",
            "section": "Ser Recicla",
            "permission": "reciclagem.view_reciclagem",
            "sub_items": [
                {
                    "label": "Reciclagem",
                    "url_name": "reciclagem:reciclagem_list",
                    "permission": "reciclagem.view_reciclagem",
                },
                {
                    "label": "Tipo Residuos",
                    "url_name": "reciclagem:tiporesiduos_list",
                    "permission": "reciclagem.view_tiporesiduos",
                },
            ],
        },
        {
            "label": "Cadastros",
            "icon": "bx bx-book",
            "section": "Institucional",
            "permission": "reciclagem.view_reciclagem",
            "sub_items": [
                {
                    "label": "Unidades",
                    "url_name": "reciclagem:unidade_list",
                    "permission": "reciclagem.view_unidade",
                },
                {
                    "label": "Cursos",
                    "url_name": "reciclagem:curso_list",
                    "permission": "reciclagem.view_curso",
                },
                {
                    "label": "Turmas",
                    "url_name": "reciclagem:turma_list",
                    "permission": "reciclagem.view_turma",
                },
                {
                    "label": "Alunos",
                    "url_name": "reciclagem:aluno_list",
                    "permission": "reciclagem.view_aluno",
                },
            ],
        }
    ]
  

    current_path = request.path


    filtered_items = []
    sections = {}

    for item in items:
        item['active'] = False
        if 'sub_items' in item:
            visible_sub_items = []
            for sub_item in item['sub_items']:
                sub_item['url'] = reverse(sub_item['url_name'])
                if sub_item.get('permission') in request.user.get_all_permissions():
                    visible_sub_items.append(sub_item)
                    if sub_item['url'] == current_path:
                        item['active'] = True
                        sub_item['active'] = True
                    else:
                        sub_item['active'] = False
            item['sub_items'] = visible_sub_items
            if visible_sub_items:
                filtered_items.append(item)
        else:
            item['url'] = reverse(item['url_name']) if 'url_name' in item else None
            if item.get('permission') in request.user.get_all_permissions():
                filtered_items.append(item)
                if item['url'] == current_path:
                    item['active'] = True
            elif 'header' in item:
                filtered_items.append(item)


    for item in filtered_items:
        section = item['section']
        if section not in sections:
            sections[section] = []
        sections[section].append(item)


    return {'menu_items': sections}
