### PROBLEM DESCRIPTION
Our model seeks to generate ten recommendations of strains of cannabis for new cannabis users based on their medical needs and desired positive effects. 

### HOW THE MODEL WORKS:

1. The model takes in two inputs from the user: 
    1. Medical symptoms 
    2. Desired positive effects

2. The input is pre-processed before being fed into the model so that it becomes a list with one string variable:

        ["alcohol, depressed, fat, high, happy"]

3. The model returns a jsonified file of the ten top-rated strains of cannabis. The data included are the index number, rating, medical needs, positive effects, negative effects, type, and description. The results are sorted in descending order by rating. 

4. The output is post-processed so that stringified arrays are returned as lists (lists for python, arrays in javascript). 

### WHERE TO FIND THE APPLICATION: 

1. Flask app deployed; routes can be found by running "flask run" in the terminal.

2. Heroku up deployed with two live routes:
    1. Takes input to recommend different cannabis strains based on medical symptoms and preferred positive effects: https://bestmedcab1.herokuapp.com/recommender
    2. Contains a JSON-formatted result set: https://bestmedcab1.herokuapp.com/dummy_data

### SAMPLE INPUT AND OUTPUT:

Sample data that can be fed as input:

```
{
    "medical": [
        "alcholic",
        "depressed",
        "fat"
    ],
    "effects": [
        "high",
        "happy"
    ]
}
```

Sample output from the sample input: 


```
[
    {
        "description": "Huckleberry Hound is an obscure hybrid that has alleged roots in Blueberry and Chemdawg families. With notes of berry intermixed with a palatable melange of chemicals, this flower's bouquet is challenging but worthwhile. Expect airy body effects that take on more weight with time and cerebral effects that remind many of Sour Diesel's type of mental stimuli. Most Chemdawg lineage is potent, so be aware, as this strain is a howler. ",
        "flavors": [
            "Blueberry",
            "Chemical",
            "Skunk"
        ],
        "index": 706,
        "medical": [],
        "negative": [],
        "positive": [
            "Relaxed",
            "Euphoric",
            "Happy",
            "Creative"
        ],
        "rating": 5.0,
        "strain": "Huckleberry Hound",
        "type": "hybrid"
    },
    {
        "description": "The Ooze is an 80/20 indica-dominant cross of Green Crack and White Fire Alien OG. With effects that sedate and relax, The Ooze takes its title seriously. Employ this heavyweight in the evening to stimulate appetite and encourage rest, or look to this strain for contending with strong social anxiety. Just don't plan on doing too much too fast. ",
        "flavors": [
            "Apple",
            "Spicy/Herbal",
            "Sweet"
        ],
        "index": 1359,
        "medical": [],
        "negative": [],
        "positive": [
            "Relaxed",
            "Euphoric",
            "Happy",
            "Creative",
            "Focused"
        ],
        "rating": 5.0,
        "strain": "The Ooze",
        "type": "indica"
    },
    {
        "description": "Tangerine Haze and Gupta Kush come together in this outstanding hybrid by Colorado Seed Inc. With sweet and stimulating effects brought forward by Tang's NYC Diesel x G13 Haze parentage and a yield and potency boost from Gupta Kush, Gupta Haze is mentally clarifying with a generous body buzz. Expect plants with an average THC content of no less than 21% that finishes is about 10 weeks.  ",
        "flavors": [
            "Earthy",
            "Citrus",
            "Lemon"
        ],
        "index": 643,
        "medical": [],
        "negative": [
            "Dry Mouth"
        ],
        "positive": [
            "Relaxed",
            "Euphoric",
            "Happy",
            "Giggly"
        ],
        "rating": 5.0,
        "strain": "Gupta Haze",
        "type": "hybrid"
    },
    {
        "description": "Wookies (not to be confused with the strain "Wookie" or the enormous, sentient space-bears of Star Wars) is an indica-dominant cross of White 91 (The White x Chemdawg 91) and Girl Scout Cookies. Known for its loud terpene profile and high-THC percentage, Wookies grows the Cookies genetic line while standing firmly on its own in terms of effects. It combines the generous trichome production of White 91 with the minty, musky aroma of the GSC "Forum Cut" to create a strain that is potent and pleasing to the senses.    ",
        "flavors": [
            "Minty"
        ],
        "index": 1484,
        "medical": [
            "Depression",
            "Insomnia",
            "Stress"
        ],
        "negative": [],
        "positive": [
            "Relaxed",
            "Euphoric",
            "Happy",
            "Uplifted"
        ],
        "rating": 4.8,
        "strain": "Wookies",
        "type": "hybrid"
    },
    {
        "description": "Flo Walker from award-winning breeder, The Vault Genetics, is an exceptional indica-dominant cross with potency and flavor. By combining the legendary likes of Skywalker OG and DJ Short's Flo, Flo Walker takes on the calming sedative body of its Afghani parentage while commingling with Flo's brilliant flavor and clear mental state. Enjoy this strain in the evening to temper physical pain and restlessness.",
        "flavors": [
            "Citrus",
            "Earthy",
            "Lemon"
        ],
        "index": 525,
        "medical": [],
        "negative": [
            "Dry Mouth"
        ],
        "positive": [
            "Euphoric",
            "Happy",
            "Creative",
            "Energetic"
        ],
        "rating": 4.8,
        "strain": "Flo Walker",
        "type": "hybrid"
    },
    {
        "description": "Thelonious Skunk, named for Colorado Seed Inc.'s favorite jazz musician, Thelonious Monk, is the funky lovechild of Island Sweet Skunk and Nina Limone. This upbeat, bebopping combo exhibits tropical flavors like citrus trees and sweet earth, mixed with a distinct skunky undertone. Its bouquet of diverse smells aligns well with its energizing effects, which wrap the consumer in a pleasant, upbeat haze that helps combat depression and lethargy.   ",
        "flavors": [
            "Skunk",
            "Citrus",
            "Pungent"
        ],
        "index": 1368,
        "medical": [
            "Depression",
            "Insomnia",
            "Pain",
            "Stress"
        ],
        "negative": [
            "Dry Eyes"
        ],
        "positive": [
            "Relaxed",
            "Euphoric",
            "Happy",
            "Uplifted"
        ],
        "rating": 4.8,
        "strain": "Thelonious Skunk",
        "type": "hybrid"
    },
    {
        "description": "Elphinstone is a sativa-dominant strain that combines stimulating genetics and pungent terpenes. This strain is a cross of Sweet Skunk and Appalachia. This pungent pairing imbues the consumer with a giggly, uplifted mental state juxtaposed with mildly focused and relaxing physical effects. The flavors are a mixture of skunk and sweet 7-Up-like notes. ",
        "flavors": [
            "Citrus",
            "Pine",
            "Pungent"
        ],
        "index": 502,
        "medical": [
            "Stress"
        ],
        "negative": [
            "Dry Mouth"
        ],
        "positive": [
            "Relaxed",
            "Happy",
            "Creative",
            "Focused"
        ],
        "rating": 4.5,
        "strain": "Elphinstone",
        "type": "sativa"
    },
    {
        "description": "Lemon Cake by Heavyweight Seeds is a potent sativa-dominant strain with sweet and musky aromas. Also known as Lemon Cheesecake, Lemon Cake is the cross of Lemon Skunk and a "dangerously powerful Cheese," according to HS. With a nine to ten week flowering time, squat morphology, and abundant yield, Lemon Cake is kind to growers, especially those outdoors. This strain emits a pungent citrus aroma with a musky Cheese undertone. Heavyweight Seeds recommends consuming this strain to combat stress, loss of appetite, and minor physical discomfort.",
        "flavors": [
            "Cheese",
            "Lemon",
            "Spicy/Herbal"
        ],
        "index": 832,
        "medical": [
            "Stress"
        ],
        "negative": [],
        "positive": [
            "Relaxed",
            "Euphoric",
            "Happy",
            "Creative",
            "Energetic"
        ],
        "rating": 4.3,
        "strain": "Lemon Cake",
        "type": "sativa"
    },
    {
        "description": "Tigermelon is a mysterious strain of unknown origin that has been used by the breeder Bodhi Seeds to create some spectacular hybrids such as Snow Leopard. It is thought to be a three-way cross of Chemdawg, Apollo 11 (Genius cut) and an Uzbekistani indica, and the smell has been described by Bodhi as "sandalwood mango lassi."",
        "flavors": [
            "Sweet"
        ],
        "index": 1375,
        "medical": [],
        "negative": [],
        "positive": [
            "Relaxed",
            "Happy"
        ],
        "rating": 3.0,
        "strain": "Tigermelon",
        "type": "indica"
    },
    {
        "description": "White Strawberry is the flavorful cross of The White and Strawberry Cough. This all-day hybrid blends The White's relaxing physical effects and tertiary gastrointestinal benefits with Strawberry Cough's cerebral stimulation to create a potent hybrid with medicinal utility. The cerebral effects can be rather spacey, making this strain perfect for repetitive tasks, but with continued consumption it supplies a euphoric mental aloofness that can help one shrug off stress and depression.  ",
        "flavors": [
            "Citrus",
            "Sweet"
        ],
        "index": 1470,
        "medical": [
            "Depression",
            "Stress",
            "Headache",
            "Headaches"
        ],
        "negative": [
            "Dry Mouth",
            "Paranoid",
            "Anxious"
        ],
        "positive": [
            "Happy"
        ],
        "rating": 3.0,
        "strain": "White Strawberry",
        "type": "hybrid"
    }
]
```

