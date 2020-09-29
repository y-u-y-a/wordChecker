# import csv, copy
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST

# from core.views.libs import scrap


# #######################################
# # Customs
# #######################################
# @csrf_exempt
# @require_POST
# def check(request):
#     """check by keywordplaner"""
#     # [input]
#     file = request.FILES['keywords_file'] # 'InMemoryUploadedFile'
#     content: str = file.read().decode('utf-8')
#     keywords: list = content.split()
#     keywords: list = [{'word': kw, 'count': 0} for kw in keywords]
#     url_list: list = [
#         str(request.POST.get('url_1')),
#         str(request.POST.get('url_2')),
#         str(request.POST.get('url_3')),
#         str(request.POST.get('url_4')),
#         str(request.POST.get('url_5')),
#     ]
#     # [start]
#     result_list: list = []
#     for url in url_list:
#         if url:
#             init_kw_list: list = copy.deepcopy(keywords) # 値渡し(multi ary)
#             result_list.append(check_url(url, init_kw_list))

#     # [output]
#     return JsonResponse({
#         'data': result_list
#     })


# def check_url(url: str, keyword_list: list) -> dict:
#     """extract page info per url"""
#     # [input]
#     article_list: list = []

#     # [start]
#     html = scrap.get_html(url)
#     # get page info
#     article: dict = {
#         'url': url,
#         'h1': scrap.get_h1(html),
#         'h2': scrap.get_text_list(html, 'h2'),
#         'h3': scrap.get_text_list(html, 'h3')
#     }
#     # count
#     keyword_list: list = count_keyword(article['h2'], keyword_list)
#     keyword_list: list = count_keyword(article['h3'], keyword_list)
#     article_list.append(article)

#     # [output]
#     return {
#         'article_list': article_list,
#         'keyword_list': keyword_list
#     }


# def count_keyword(word_list: list, keyword_list: list) -> list:
#     """count keyword list if it includes word"""
#     for word in word_list:
#         # include in keywords?
#         for i, kw in enumerate(keyword_list):
#             if kw['word'] in word:
#                 keyword_list[i]['count'] += 1
#     return keyword_list
