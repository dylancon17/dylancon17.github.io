from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from.models import HomePageWriting, AboutPageWriting, ToppersWriting, CakesWriting, CakesPageInitialImages, CakesPageAdditionalImages, ToppersPageInitialImages, ToppersPageAdditionalImages, CurrentToppersForSale
from django.views.generic import ListView

# Create your views here.

    # Overall_website_description = models.TextField(null=True, max_length=400)
    # Cakes_Title = models.CharField(max_length=50, null=True)
    # Cakes_More_Info = models.TextField(null=True, max_length=300)
    # Toppers_Title = models.CharField(max_length=50, null=True)
    # Toppers_More_Info = models.TextField(null=True, max_length=300)

def home(request):
    information = HomePageWriting.objects.get(pk=1)
    context = {'information': information}
    return render(request, 'base/home.html', context)

def about(request):
    information = AboutPageWriting.objects.get(pk=1)
    context = {'information': information}
    return render(request, 'base/about.html', context)

def cakes(request):
    information = CakesWriting.objects.get(pk=2)
    images_initial = CakesPageInitialImages.objects.get(pk=1)
    images_extended = CakesPageAdditionalImages.objects.all()
    context = {'information': information, 'images_initial': images_initial, 'images_extended':images_extended}
    return render(request, 'base/cakes.html', context)

def toppers(request):
    information = ToppersWriting.objects.get(pk=1)
    images_initial = ToppersPageInitialImages.objects.get(pk=1)
    images_extended = ToppersPageAdditionalImages.objects.all()
    for_sale = CurrentToppersForSale.objects.all()
    context = {'information': information, 'images_initial': images_initial, 'images_extended':images_extended, 'for_sale':for_sale}
    return render(request, 'base/toppers.html', context)


# Use below to update toppers 4 sale.
# # Define class for inserting multiple data

# class BulkInsert(ListView):

#     # Define model

#     model = CurrentToppersForSale

#     # Define template

#     template_name = 'toppers.html'

#    # Read all existing records of books table

#     queryset = CurrentToppersForSale.objects.all()

#     # Check the books table is empty or not

#     if queryset.exists() == False:

#        # Insert 5 records in the books table at a time

#         CurrentToppersForSale.objects.bulk_create([
#             CurrentToppersForSale(Name='Disney Ariel Cake Topper Fondant Gumpaste', Cost='100.00', Image='https://i.etsystatic.com/29295265/c/3000/2384/0/525/il/ed14a8/3834513954/il_340x270.3834513954_37p7.jpg', Url='https://www.etsy.com/ca/listing/1221828985/disney-ariel-cake-topper-fondant?click_key=6585c3abd9ec4aa11a5987e539b21b082f6f1e27%3A1221828985&click_sum=2b9d68f8&ref=shop_home_active_1&frs=1'),
#             CurrentToppersForSale(Name='Toy Story Cake Toppers', Cost='75.00', Image='https://i.etsystatic.com/29295265/c/3000/2384/0/448/il/dbecee/3629504284/il_340x270.3629504284_4qjt.jpg', Url='https://www.etsy.com/ca/listing/1154820022/toy-story-cake-toppers?click_key=29ca380689d991cb6262b456578720402e971905%3A1154820022&click_sum=6d74effa&ref=shop_home_active_2&frs=1'),    
#             CurrentToppersForSale(Name='Paw Patrol Fondant/ Gum Paste Cake Toppers', Cost='70.00', Image='https://i.etsystatic.com/29295265/c/2250/1788/0/28/il/4e5071/3039143998/il_340x270.3039143998_m2z0.jpg', Url='https://www.etsy.com/ca/listing/993742366/paw-patrol-fondant-gum-paste-cake?click_key=c9c781afad8542ad31a9650613b0cfbc08de0fad%3A993742366&click_sum=fa754933&ref=shop_home_active_3&frs=1'),
#             CurrentToppersForSale(Name='UP Characters Fondant/ Gum Paste Cake Toppers', Cost='60.00', Image='https://i.etsystatic.com/29295265/c/3000/2384/0/448/il/9b8b90/3563232306/il_340x270.3563232306_cvtz.jpg', Url='https://www.etsy.com/ca/listing/1151157749/up-characters-fondant-gum-paste-cake?click_key=f05e9b9bae53cea60f790f46433ab21dbc18d04e%3A1151157749&click_sum=c43bc8cd&ref=shop_home_active_4&frs=1'),
#             CurrentToppersForSale(Name='Baby Yoda Fondant Cake Toppers Mandalorian Grogu', Cost='60.00', Image='https://i.etsystatic.com/29295265/r/il/0a1e07/3398733571/il_340x270.3398733571_8ozq.jpg', Url='https://www.etsy.com/ca/listing/1006056252/baby-yoda-fondant-cake-toppers?click_key=cc12522fec4569526253341f06bb2817595ee6bb%3A1006056252&click_sum=0b794db3&ref=shop_home_active_5&frs=1'),
#             CurrentToppersForSale(Name='Magical Unicorn Fondant/ Gumpaste Cake Topper', Cost='30.00', Image='https://i.etsystatic.com/29295265/r/il/bc24c9/3170731249/il_340x270.3170731249_eu2w.jpg', Url='https://www.etsy.com/ca/listing/993718762/magical-unicorn-fondant-gumpaste-cake?click_key=4c025d89a49649a0e749d7c5af251a2bfe455f5a%3A993718762&click_sum=8df88334&ref=shop_home_active_6&frs=1'),
#             CurrentToppersForSale(Name='Doll Fondant/ Gum Paste Cake Topper', Cost='60.00', Image='https://i.etsystatic.com/29295265/r/il/9faef2/3610975943/il_340x270.3610975943_ai9n.jpg', Url='https://www.etsy.com/ca/listing/1151195209/doll-fondant-gum-paste-cake-topper?click_key=1b9b9dddf3845e06e715f7e827427a23f4451084%3A1151195209&click_sum=d59d7f06&ref=shop_home_active_7&frs=1'),
#             CurrentToppersForSale(Name='Mario and Luigi Fondant/ Gum Paste Cake Toppers', Cost='65.00', Image='https://i.etsystatic.com/29295265/r/il/b36b79/3086833233/il_340x270.3086833233_bjj7.jpg', Url='https://www.etsy.com/ca/listing/1007695445/mario-and-luigi-fondant-gum-paste-cake?click_key=b89c754c5cbcfba10b6a575d90f6f11e36f67bd2%3A1007695445&click_sum=f36dbfe3&ref=shop_home_active_8&frs=1'),
#             CurrentToppersForSale(Name='Wreck It Ralph and Vanellope Fondant Cake Toppers', Cost='70.00', Image='https://i.etsystatic.com/29295265/r/il/578c6f/3295904596/il_340x270.3295904596_rgyq.jpg', Url='https://www.etsy.com/ca/listing/1076059615/wreck-it-ralph-and-vanellope-fondant?click_key=cea699d830d8900b5861c4347efe971e1cd79910%3A1076059615&click_sum=550eb13e&ref=shop_home_active_9&frs=1'),
#             CurrentToppersForSale(Name='Corpse Bride Fondant/ Gumpaste Cake Topper', Cost='100.00', Image='https://i.etsystatic.com/29295265/r/il/59de46/3610824791/il_340x270.3610824791_qp16.jpg', Url='https://www.etsy.com/ca/listing/1137204514/corpse-bride-fondant-gumpaste-cake?click_key=97ffe78edf1556d0fca2615f21da570ca03e892a%3A1137204514&click_sum=637361d2&ref=shop_home_active_10&frs=1'),
#             CurrentToppersForSale(Name='Spider-Man Fondant/ Gum Paste Cake Topper', Cost='60.00', Image='https://i.etsystatic.com/29295265/c/3000/2384/0/487/il/4344da/3610867671/il_340x270.3610867671_8o3t.jpg', Url='https://www.etsy.com/ca/listing/1151161043/spider-man-fondant-gum-paste-cake-topper?click_key=baad2616e0cc7f5b0b70bac656fa191b02c28701%3A1151161043&click_sum=a692842c&ref=shop_home_active_11&frs=1'),
#             CurrentToppersForSale(Name='Mandalorian and Baby Yoda Fondant Gumpaste Cake Topper', Cost='70.00', Image='https://i.etsystatic.com/29295265/r/il/40d9a2/3112896384/il_340x270.3112896384_bfma.jpg', Url='https://www.etsy.com/ca/listing/1013476222/mandalorian-and-baby-yoda-fondant?click_key=c2b3db176acee564aebb905fb3045a28a41dfb38%3A1013476222&click_sum=3feeda6f&ref=shop_home_active_12&frs=1'),
#             CurrentToppersForSale(Name='Baby Groot Fondant/ Gumpaste Cake Topper', Cost='60.00', Image='https://i.etsystatic.com/29295265/c/3000/2384/0/51/il/df87e1/3194330318/il_340x270.3194330318_9wui.jpg', Url='https://www.etsy.com/ca/listing/1048756385/baby-groot-fondant-gumpaste-cake-topper?click_key=da5730468bb4db4273303ed128c7f2425c81e73f%3A1048756385&click_sum=99444561&ref=shop_home_active_13&frs=1'),
#             CurrentToppersForSale(Name='Wedding Toppers Bride Groom Fondant', Cost='120.00', Image='https://i.etsystatic.com/29295265/c/2250/1788/0/67/il/8a7b34/3295945800/il_340x270.3295945800_2jy5.jpg', Url='https://www.etsy.com/ca/listing/1076068777/wedding-toppers-bride-groom-fondant?click_key=cd622262cefe27ccb764c0a691aadae7b0257e30%3A1076068777&click_sum=a80f422a&ref=shop_home_active_14&frs=1'),
#             CurrentToppersForSale(Name='Star Wars Yoda Fondant/ Gum Paste Cake Topper', Cost='60.00', Image='https://i.etsystatic.com/29295265/c/1680/1335/0/0/il/d56f09/3039101770/il_340x270.3039101770_6klq.jpg', Url='https://www.etsy.com/ca/listing/1007691517/star-wars-yoda-fondant-gum-paste-cake?click_key=e23d5fa131091e6e24ddcda05048337b896ea166%3A1007691517&click_sum=321f5b26&ref=shop_home_active_15&frs=1'),
#             CurrentToppersForSale(Name='Stitch Fondant/ Gum Paste Cake Topper', Cost='70.00', Image='https://i.etsystatic.com/29295265/c/1440/1144/0/61/il/19a6c6/3086858343/il_340x270.3086858343_6645.jpg', Url='https://www.etsy.com/ca/listing/1007700779/stitch-fondant-gum-paste-cake-topper?click_key=deeacd319855bf299333669b2069d4cc79e3c458%3A1007700779&click_sum=0ef54e14&ref=shop_home_active_16&frs=1'),
#             CurrentToppersForSale(Name='Man Sleeping In Chair Fondant/ Gum Paste Cake Topper', Cost='100.00', Image='https://i.etsystatic.com/29295265/c/2298/1826/0/756/il/1cf961/3086796399/il_340x270.3086796399_8mq1.jpg', Url='https://www.etsy.com/ca/listing/1007683979/man-sleeping-in-chair-fondant-gum-paste?click_key=38e0a4d27be4204e6f87bc4adfc2fa00e9e89449%3A1007683979&click_sum=25ba38c4&ref=shop_home_active_17&frs=1'),
#             CurrentToppersForSale(Name='Adorable Grumpy Children Fondant/ Gum Paste Cake Toppers', Cost='55.00', Image='https://i.etsystatic.com/29295265/r/il/6b8fa4/3147131060/il_340x270.3147131060_o34c.jpg', Url='https://www.etsy.com/ca/listing/993705498/adorable-grumpy-children-fondant-gum?click_key=f27fb74d4c5c557b3b2a13a0d894da0666ce469d%3A993705498&click_sum=075982ec&ref=shop_home_active_18&frs=1'),
#             CurrentToppersForSale(Name='Mermaid Tail Fondant/ Gum Paste Cake Topper', Cost='30.00', Image='https://i.etsystatic.com/29295265/c/3000/2384/0/128/il/3ad309/3039123726/il_340x270.3039123726_5rma.jpg', Url='https://www.etsy.com/ca/listing/993736748/mermaid-tail-fondant-gum-paste-cake?click_key=5e2bae02f719b087e877c2c88e292a7efb7e69bd%3A993736748&click_sum=a2bc5975&ref=shop_home_active_19&frs=1'),
#             CurrentToppersForSale(Name='Animals Fondant/ Gum Paste Cake Topper', Cost='60.00', Image='https://i.etsystatic.com/29295265/r/il/7c8563/3086710929/il_340x270.3086710929_g5t7.jpg', Url='https://www.etsy.com/ca/listing/1007659855/animals-fondant-gum-paste-cake-topper?click_key=e9a23b16fc03b5c5ac57b1a8a4166cf5070aa743%3A1007659855&click_sum=028720e3&ref=shop_home_active_20&frs=1'),
#             CurrentToppersForSale(Name='Snuggled Up For Winter Penguin and Baby Fondant Cake Topper', Cost='55.00', Image='https://i.etsystatic.com/29295265/r/il/c38c1c/3086723077/il_340x270.3086723077_86iz.jpg', Url='https://www.etsy.com/ca/listing/1007663117/snuggled-up-for-winter-penguin-and-baby?click_key=b902930dc8729ad975d36f647767ba9f386812a0%3A1007663117&click_sum=1f43a235&ref=shop_home_active_21&frs=1'),
#         ])
   

#     # Return all records of the books table

#     def get_queryset(self):

#         # Set the default query set

#         return CurrentToppersForSale.objects.all()