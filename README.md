# cf-pro-crawler-app  

A basic product crawler integrated for carrefoursa.com for product images and csv file output. Project based on Scrapy.  

## File Tree  
GitHub project -> https://github.com/eemektas/cf-pro-crawler-app  
>.cf-pro-crawler-app  
├── cf_pro_crawler  
│   ├── cf_pro_crawler  
│   │   ├── __init__.py  
│   │   ├── __init__.pyc  
│   │   ├── items.py  
│   │   ├── items.pyc  
│   │   ├── middlewares.py  
│   │   ├── pipelines.py  
│   │   ├── pipelines.pyc  
│   │   ├── __pycache__  
│   │   │   ├── __init__.cpython-36.pyc  
│   │   │   ├── items.cpython-36.pyc  
│   │   │   ├── pipelines.cpython-36.pyc  
│   │   │   └── settings.cpython-36.pyc  
│   │   ├── settings.py  
│   │   ├── settings.pyc  
│   │   └── spiders  
│   │       ├── __init__.py  
│   │       ├── __init__.pyc  
│   │       ├── product.py  
│   │       ├── product.pyc  
│   │       └── __pycache__  
│   │           ├── __init__.cpython-36.pyc  
│   │           └── product.cpython-36.pyc  
│   ├── images_test  
│   │   └── full  
│   │       ├── 30027760_1.jpg  
│   │       ├── 30089983_1.jpg  
│   │       ├── 30089983_2.jpg  
│   │       ├── 30138247_1.jpg  
│   │       ├── 30138247_2.jpg  
│   │       ├── 30202211_1.jpg  
│   │       ├── 30217098_1.jpg  
│   │       ├── 30217098_2.jpg  
│   │       ├── 30248468_1.jpg  
│   │       ├── 30248468_2.jpg  
│   │       └── 30256481_1.jpg  
│   ├── products_test.csv  
│   └── scrapy.cfg  
├── LICENSE  
└── README.md  

## App Requirements  

- Scrapy  
	You can install Scrapy using `pip` with:  
	`pip install Scrapy`  
	Or install Scrapy using setuptools‘s `easy_install` with:  
	`easy_install -U Scrapy`  
	For more detailed guide: https://docs.scrapy.org/en/latest/intro/install.html  

- Pillow  
	Install Pillow with `pip`:  
	`pip install Pillow`  
	Or:  
	`python -m pip install Pillow`  
	For more detailed guide: https://pillow.readthedocs.io/en/latest/installation.html  

## cf_pro_crawler Using Guide  

1. Download the project from https://github.com/eemektas/cf-pro-crawler-app or Clone it to your directory by:  
	`git clone https://github.com/eemektas/cf-pro-crawler-app.git`  

2. Direct to cf_pro_crawler folder in the project on cmd/terminal:  
	`cd ~/<your project directory>/cf-pro-crawler-app/cf_pro_crawler`  

3. Define the path for product_images folder to be saved in by your specific system features. Folder path should be defined in 2 different parts in the project. Linux based definitions defined below here. **Be careful while defining your path if you are a Windows or Mac user.**  
	- First pathway is in the **pipelines.py** file. Find the similar code in your project and, then modify for your specific system path.  
    		os.chdir('/home/zx/Desktop/cf-pro-crawler-app/cf_pro_crawler/product_images')  
	- Second one is in the **settings.py** file.  
    		IMAGES_STORE = '/home/zx/Desktop/cf-pro-crawler-app/cf_pro_crawler/product_images'  

4. Specify the product url to be crawled as below and use the Scrapy command to extract product image(s) folder and csv output.  
	`scrapy crawl product -a start_urls="https://www.carrefoursa.com/tr/pinar-ac-bitir-buyuk-dilim-hindi-salam-60-g-p-30202211"`  

5. Then image(s) folder and csv output will be appear in the cf-product-crawler-app project folder named as **product_images** and **products.csv** if you defined the folder path similar as explaned above.  
>.cf-pro-crawler-app  
├── **images_test**  
│   └── full  
│       ├── 30027760_1.jpg  
│       ├── 30089983_1.jpg  
│       ├── 30089983_2.jpg  
│       ├── 30138247_1.jpg  
│       ├── 30138247_2.jpg  
│       ├── 30202211_1.jpg  
│       ├── 30217098_1.jpg  
│       ├── 30217098_2.jpg  
│       ├── 30248468_1.jpg  
│       ├── 30248468_2.jpg  
│       └── 30256481_1.jpg  
├── **products_test.csv**  


## ~Optional~   
- Multiple products can be crawled if desired. To do that, seperate the product urls with comma(,) and no space around commas. e.g:  
	`scrapy crawl product -a start_urls="https://www.carrefoursa.com/tr/pinar-ac-bitir-buyuk-dilim-hindi-salam-60-g-p-30202211,https://www.carrefoursa.com/tr/johnson-s-baby-shampoo-200-ml-p-30027760,https://www.carrefoursa.com/tr/schweppes-mandarin-mandalina-aromali-gazli-icecek-sise-6x250-ml-p-30089983,https://www.carrefoursa.com/tr/gagoz-sise-250-ml-p-30138247,https://www.carrefoursa.com/tr/sprite-ml-kutu-6x250-p-30217098,https://www.carrefoursa.com/tr/carrefour-gezen-tavuk-yumurtasi-10-adet-m-boy-p-30248468,https://www.carrefoursa.com/tr/steps-sports-soguk-sicak-termojel-medium-p-30256481"`  

- Output file format can be changed to json/xml with the Scrapy -o and -t code below. Just change `-o productsAsXml.xml -t xml` to extract xml file in the code snippet.  
	`scrapy crawl product -a start_urls="https://www.carrefoursa.com/tr/pinar-ac-bitir-buyuk-dilim-hindi-salam-60-g-p-30202211,https://www.carrefoursa.com/tr/johnson-s-baby-shampoo-200-ml-p-30027760,https://www.carrefoursa.com/tr/schweppes-mandarin-mandalina-aromali-gazli-icecek-sise-6x250-ml-p-30089983,https://www.carrefoursa.com/tr/gagoz-sise-250-ml-p-30138247,https://www.carrefoursa.com/tr/sprite-ml-kutu-6x250-p-30217098,https://www.carrefoursa.com/tr/carrefour-gezen-tavuk-yumurtasi-10-adet-m-boy-p-30248468,https://www.carrefoursa.com/tr/steps-sports-soguk-sicak-termojel-medium-p-30256481" -o productsAsJson.json -t json`  
  
