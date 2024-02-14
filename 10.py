
#----------------- დავალება 10 -----------------

# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით 
# "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები

# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ

# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით

# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით

import json
import requests
def getData(assignmentNumber):
    url = "https://fakestoreapi.com/products" 
    response = requests.get(url) 
    if response.status_code != 200:
        return False
    else:
        data = response.json()
        if assignmentNumber == 'a':
            prices = list()
            maxPriceId = ''
            maxPrice = data[0]['price']
            minPriceId = ''
            minPrice = data[0]['price']
            averagePrice = 0
            for item in data:
                prices.append({'id':item['id'],'price':item['price']})
                if item['price'] > maxPrice:
                    maxPriceId = item['id']
                    maxPrice = item['price']
                if item['price'] < minPrice:
                    minPriceId = item['id']
                    minPrice = item['price']
                averagePrice += item['price']
            prices.append({'maxPriceId':maxPriceId,'maxPrice':maxPrice,'minPriceId':minPriceId,'minPrice':minPrice,'averagePrice':(averagePrice / len(data))})
            return prices
        if assignmentNumber == 'b':
            categries = []
            for item in data:
                if item['category'] not in categries:
                    categries.append(item['category'])
            return(sorted(categries))
        if assignmentNumber == 'c':
            titles = []
            for item in data:
                titles.append({'id':item['id'],'title':item['title']})
            sortedTitles = sorted(titles, key=lambda d: d['title']) 
            return(sortedTitles)
        if assignmentNumber == 'd':
            rates = []
            for item in data:
                rates.append({'id':item['id'],'rate':item['rating']['rate']})
            sortedRates = sorted(rates, key=lambda d: d['rate']) 
            return(sortedRates)

print(' '*5000)
print(' ა = ',getData('a'), end = ('\n')*5)
print(' ბ = ',getData('b'), end = ('\n')*5)
print(' გ = ',getData('c'), end = ('\n')*5)
print(' დ = ',getData('d'), end = ('\n')*5)
    
#/----------------- დავალება 10 -----------------