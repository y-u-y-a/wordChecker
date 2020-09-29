# import time
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST

# from core.models import Word
# from core.views.libs import Chrome



# #######################################
# # Customs
# #######################################
# @csrf_exempt
# @require_POST
# def search(request):
#     """auto search on chrome"""

#     # [input]
#     keyword: str = request.POST.get('keyword')
#     url: str = 'https://google.com/'
#     chrome_form_name: str = 'q'
#     article_xpath: str = "//div[@id='rso']//div[@class='g']"
#     result_list: list = []

#     # [start]
#     ch = Chrome(url)
#     chrome_search = ch.get_element_by_name(chrome_form_name)
#     chrome_search.send_keys(keyword)
#     chrome_search.submit()
#     time.sleep(1)
#     # get searched list
#     elements = ch.get_elements_by_xpath(article_xpath)
#     for el in elements:
#         title: str = el.find_element_by_tag_name('h3').text
#         link: str = ch.get_link(el)
#         article: dict = {
#             'title': title,
#             'link': link
#         }
#         result_list.append(article)
#     # end
#     ch.end()
#     # [output]
#     return JsonResponse({
#         'data': result_list
#     })
