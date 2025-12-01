from django.shortcuts import render
from post.models import Post
from categories.models import Category

def home(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        # ei slug field ta kon object er ekta part, se object ta ke first e get kore ber kore niye ashlam
        data = Post.objects.filter(category = category)
        # je object ta pelam, ei catgory object ta ekhon pass kore dilam category = category te
    categories = Category.objects.all()
    
    return render(request, 'home.html', {'data' : data, 'category' : categories})


# eta complex ekta jinish. Tai eta use na kore simple kichu ekta use korbo. (etar poriborte ei line ta use korechi "data = Post.objects.filter(category = category)")
# data = Post.objects.filter(category__category_slug)
    # category__ er mane holo, category_ (1 ta underscore) er mane holo ami category theke category model e gelam. Mane 1 ta _ diye ami post er moddhe chilam, categry__ (2nd underscore) 2nd _ diye amra post theke category te chole gechi. Tarpor amra dibo category_slug





# from django.shortcuts import render
# from post.models import Post
# from categories.models import Category
# def home(request, category_slug = None): # initially dhore nicchi je category_slug None thakbe karon hocche user first time home page e asle se normal page dekhbe, se filter korte chaile category te click korlei sei category er slug ta capture korbo ar seta tokhn ar None thakbe na
    
#     data = Post.objects.all() # sob post gula ke niye aslam
#     if category_slug is not None: # ekhn category slug jodi None na hoy tar mane sekhane value ache
#         category = Category.objects.get(slug = category_slug) # slug je field model e likhechilam seta = amader category slug kore dilam taile ekhn kon category er slug sei category object peye jabo
#         data = Post.objects.filter(category  = category) # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
#     categories = Category.objects.all() # sob category dekhabo
#     return render(request, 'home.html', {'data' : data, 'category' : categories})